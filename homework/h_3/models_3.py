from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    student_id = db.relationship('Grade', backref='student')

    def __repr__(self) -> str:
        return f'Student({self.name}, {self.last_name}, {self.email}, {self.group})'

    def __str__(self) -> str:
        return self.name


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_title = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Student({self.lesson_title}, {self.grade})'

