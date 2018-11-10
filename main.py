from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    import pdb; pdb.set_trace()
    return 'Hello, World!'

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    data = request.form
    for key, value in data.items():
        print('{}: {}'.format(key, value))
    return 'got here'


if __name__ == '__main__':
    pass
    

