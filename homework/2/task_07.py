from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('task_07_form.html')


@app.post('/form/')
def index_post():
    number = request.form.get('number')
    return redirect(url_for('result', number=number))


@app.get('/result/<number>')
def result(number: str):
    square_number = int(number)**2

    context = {
        'number': number,
        'square_number': square_number
    }
    return render_template('task_07_result.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
