from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('task_06_form.html')


@app.post('/login/')
def index_post():
    login = request.form.get('username').capitalize()
    age = request.form.get('age')

    return redirect(url_for('adult', age=age, login=login))


@app.get('/success/<age>/<login>')
def adult(age: str, login: str):
    if int(age) > 17:
        return render_template('age_big.html', login=login, age=age)
    else:
        return render_template('age_small.html', login=login, age=age)


if __name__ == '__main__':
    app.run(debug=True)
