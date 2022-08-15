from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/<name>')
def read_name(name):
    return render_template('index.html', name="Hello, " + name)


@app.route('/results/<grade>')
def read_mark(grade):
    grade = int(grade)
    if grade > 80:
        mark = "A"
    else:
        mark = "B"
    return render_template('index.html', mark="You have got a grade of: " + mark)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
