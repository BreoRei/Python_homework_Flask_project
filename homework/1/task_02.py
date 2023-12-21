from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task_02_index.html')


@app.route('/одежда/')
@app.route('/cloth/')
def cloth():
    return render_template('task_02_cloth.html')


@app.route('/обувь/')
@app.route('/shoes/')
def shoes():
    return render_template('task_02_shoes.html')


@app.route('/куртка/')
@app.route('/jacket/')
def jacket():
    return render_template('task_02_jacket.html')


if __name__ == '__main__':
    app.run(debug=True)