from flask import Flask, render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/receive', methods=['GET', 'POST'])
def receive():
    data = request.form
    for key, value in data.items():
        print('{}: {}'.format(key, value))
    return 'got here'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
