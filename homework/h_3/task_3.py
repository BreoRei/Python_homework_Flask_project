from random import choice, randint
from flask import Flask, render_template
from homework.h_3.models_3 import db, Student, Grade
from faker import Faker

WORSHOP = ['математика', 'биология', 'русский', 'история']
GROUPS = ['8A', '8B', '8C', '8D', '8E', '8F']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db.init_app(app)
fake = Faker()


@app.route('/')
def index():
    students = Student.query.all()
    greads = Grade.query.all()
    context = {
        'students': students,
        'greads': greads
    }
    print('John add in DB!')
    return render_template('task_3_index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')


@app.cli.command('fill-db')
def fill_db():
    for _ in range(10):
        student = Student(
            name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            group=choice(GROUPS),
        )
        db.session.add(student)
        for work in WORSHOP:
            grade = Grade(
                lesson_title=work,
                grade=randint(1, 5),
                student=student
            )
            db.session.add(grade)
    db.session.commit()
    print('DB Filled!')


if __name__ == '__main__':
    app.run(debug=True)
