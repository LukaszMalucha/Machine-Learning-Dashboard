from flask import render_template, redirect, url_for, send_file, session, request, Blueprint
from io import BytesIO

## Blueprint Init

library_blueprint = Blueprint(
    'library', __name__,
    template_folder="templates"
)

from .models import *
from project.algorithms.models import *

## Define file upload allowed extensions

ALLOWED_EXTENSIONS = set(['py'])


########################################################################## MAIN DASHBOARD ###################################################################################################################    


## MAIN DASHBOARD - "LIBRARY" #######################################################

@library_blueprint.route('/')
def library():
    codes = CodeRepo.query.all()
    types = TypeModel.query.all()
    current_user = session.get('current_user') or 'Guest'

    return render_template("library.html", codes=codes, types=types
                           , current_user=current_user)


## DOWNLOAD TEMPLATE ################################################################

@library_blueprint.route('/download_code/<code_id>', methods=['GET'])
def download_code(code_id):
    the_code = CodeRepo.query.filter_by(id=code_id).first()
    click = the_code.downloads + 1  ## downloads counter
    the_code.downloads = click
    db.session.commit()

    return send_file(BytesIO(the_code.file),
                     attachment_filename='{}.py'.format(the_code.name),  ## return file
                     as_attachment=True)


## INITIATE TEMPLATE UPLOAD ######################################################### 

@library_blueprint.route('/add_request')
def add_request():
    types = TypeModel.query.all()
    complexities = ComplexityModel.query.all()
    methods = MethodModel.query.all()
    current_user = session.get('current_user') or 'Guest'

    return render_template('add_request.html', types=types, complexities=complexities,
                           methods=methods, current_user=current_user)


## DEFINE ALLOWED TEMPLATE FILE FORMAT ##############################################   

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


## UPLOAD NEW TEMPLATE HANDLING #####################################################   

@library_blueprint.route('/new_code', methods=['POST'])
def new_code():
    codes = CodeRepo.query.all()
    current_user = session.get('current_user') or 'Guest'

    ## Exceptions handling:

    if not 'inputFile' in request.files:
        return render_template('error.html', current_user=current_user)

    if not 'type_of_algorithm' in request.form or not 'complexity' in request.form:
        return render_template('error.html', current_user=current_user)
    if not 'method' in request.form:
        return render_template('error.html', current_user=current_user)
    if request.form['name'] == '' or request.form['author'] == '':
        return render_template('error.html', current_user=current_user)

    ## All good
    else:
        code_file = request.files['inputFile']  ## check file format
        if code_file and allowed_file(code_file.filename):
            code_file = code_file.read()
        else:
            return render_template('error.html', current_user=current_user)

        code = CodeRepo(name=request.form['name'],
                        type_of_algorithm=request.form['type_of_algorithm'],
                        complexity=request.form['complexity'],
                        method=request.form['method'],
                        author=request.form['author'],
                        file=code_file,
                        downloads=0)
        db.session.add(code)
        db.session.commit()
        return redirect(url_for("library.library"))


## EDITING TEMPLATE INITIATION ######################################################

@library_blueprint.route('/edit_code/<code_id>')
def edit_code(code_id):
    the_code = CodeRepo.query.filter_by(id=code_id).first()
    types = TypeModel.query.all()
    complexities = ComplexityModel.query.all()
    methods = MethodModel.query.all()
    current_user = session.get('current_user') or 'Guest'

    return render_template('edit_code.html', code=the_code, types=types,
                           complexities=complexities, methods=methods,
                           current_user=current_user)


## UPDATE TEMPLATE HANDLING #########################################################

@library_blueprint.route('/update_code/<code_id>', methods=["POST"])
def update_code(code_id):
    current_user = session.get('current_user') or 'Guest'
    the_code = CodeRepo.query.filter_by(id=code_id).first()

    the_code.name = request.form['name']
    the_code.type_of_algorithm = request.form['type_of_algorithm']
    the_code.complexity = request.form['complexity']
    the_code.method = request.form['method']
    the_code.author = request.form['author']

    ## Exceptions

    if request.form['name'] == '' or request.form['author'] == '':
        return render_template('error.html', current_user=current_user)
    if 'inputFile' in request.files:
        code_file = request.files['inputFile']
        if code_file and allowed_file(code_file.filename):
            code_file = code_file.read()
            the_code.file = code_file
            db.session.commit()
            return redirect(url_for("library.library"))
        else:
            return render_template('error.html', current_user=current_user)

    ## All good

    else:
        db.session.commit()
        return redirect(url_for("library.library"))


## DELETE TEMPLATE HANDLING #########################################################    

@library_blueprint.route('/delete_code/<code_id>')
def delete_code(code_id):
    the_code = CodeRepo.query.filter_by(id=code_id).first()
    db.session.delete(the_code)
    db.session.commit()
    return redirect(url_for("library.library"))


## MANAGE DB VIEWS #################################################################


@library_blueprint.route('/manage_db')
def manage_db():
    current_user = session.get('current_user') or 'Guest'

    types = AlgorithmModel.query.all()

    return render_template('manage_db.html', current_user=current_user, types=types)


@library_blueprint.route('/add_algorithm_type', methods=['POST'])
def add_algorithm_type():
    algo_type = request.form['type']
    new_type = TypeModel(type_of_algorithm=algo_type)
    new_type.save_to_db()
    return redirect(url_for("library.manage_db"))


@library_blueprint.route('/add_complexity', methods=['POST'])
def add_complexity():
    complexity = request.form['complexity']
    new_complexity = ComplexityModel(complexity=complexity)
    new_complexity.save_to_db()
    return redirect(url_for("library.manage_db"))


@library_blueprint.route('/add_method', methods=['POST'])
def add_method():
    method = request.form['method']
    new_method = MethodModel(method=method)
    new_method.save_to_db()
    return redirect(url_for("library.manage_db"))


@library_blueprint.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algorithm_type = request.form['algorithm_type']
    algorithm_preprocessors = request.form['algorithm_preprocessors']
    algorithm_issues = request.form['algorithm_issues']
    new_algorithm = AlgorithmModel(algorithm_type=algorithm_type, algorithm_preprocessors=algorithm_preprocessors,
                                   algorithm_issues=algorithm_issues)
    new_algorithm.save_to_db()
    return redirect(url_for("library.manage_db"))
