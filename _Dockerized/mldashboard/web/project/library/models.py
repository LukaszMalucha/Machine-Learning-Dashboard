from db import db


## Code Main Repository

class CodeRepo(db.Model):
    __searchable__ = ['name', 'type_of_algorithm', 'complexity', 'method', 'author']
    __tablename__ = 'CodeRepo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    type_of_algorithm = db.Column(db.String(300))
    complexity = db.Column(db.String(300))
    method = db.Column(db.String(300))
    author = db.Column(db.String(300))
    file = db.Column(db.LargeBinary)
    downloads = db.Column(db.Integer)

    def __init__(self, name, type_of_algorithm, complexity, method, author, file, downloads):
        self.name = name
        self.type_of_algorithm = type_of_algorithm
        self.complexity = complexity
        self.method = method
        self.author = author
        self.file = file
        self.downloads = downloads

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(type_of_algorithm=name).first()

    @classmethod
    def find_by_type(cls, type_of_algorithm):
        return cls.query.filter_by(type_of_algorithm=type_of_algorithm).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


## Algorithm types

class TypeModel(db.Model):
    __tablename__ = 'Types'
    id = db.Column(db.Integer, primary_key=True)
    type_of_algorithm = db.Column(db.String(300))

    def __init__(self, type_of_algorithm):
        self.type_of_algorithm = type_of_algorithm

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_type(cls, type_of_algorithm):
        return cls.query.filter_by(type_of_algorithm=type_of_algorithm).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


## Algorithm complexity    

class ComplexityModel(db.Model):
    __tablename__ = 'Complexity'
    id = db.Column(db.Integer, primary_key=True)
    complexity = db.Column(db.String(300))

    def __init__(self, complexity):
        self.complexity = complexity

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_complexity(cls, complexity):
        return cls.query.filter_by(complexity=complexity).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


## Methods of learning

class MethodModel(db.Model):
    __tablename__ = 'Methods'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(300))

    def __init__(self, method):
        self.method = method

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_method(cls, method):
        return cls.query.filter_by(method=method).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
