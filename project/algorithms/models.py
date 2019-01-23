from db import db


## Preprocessing tasks

class PreprocessingModel(db.Model):
    __tablename__ = 'Preprocessing'
    preprocess_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_preprocess_id(cls, preprocess_id):
        return cls.query.filter_by(preprocess_id=preprocess_id).first()

##  Potential issues

class RedFlagModel(db.Model):
    __tablename__ = 'RedFlags'
    issue_id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.String(300))

    def __init__(self, issue):
        self.issue = issue

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_issue(cls, issue):
        return cls.query.filter_by(issue=issue).first()

    @classmethod
    def find_by_issue_id(cls, issue_id):
        return cls.query.filter_by(issue_id=issue_id).first()


## Types of algorithms

class AlgorithmModel(db.Model):
    __tablename__ = 'Algorithms'
    algorithm_id = db.Column(db.Integer, primary_key=True)
    algorithm_type = db.Column(db.String(300))
    algorithm_preprocessors = db.Column(db.String(300))
    algorithm_issues = db.Column(db.String(300))

    def __init__(self, algorithm_type, algorithm_preprocessors, algorithm_issues):
        self.algorithm_type = algorithm_type
        self.algorithm_preprocessors = algorithm_preprocessors
        self.algorithm_issues = algorithm_issues

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_algorithm_type(cls, algorithm_type):
        return cls.query.filter_by(algorithm_type=algorithm_type).first()