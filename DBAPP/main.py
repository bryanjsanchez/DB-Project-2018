from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

@app.route('/login/')
def log():
    return "No logging!"

if __name__ == '__main__':
    app.run(debug=True)





