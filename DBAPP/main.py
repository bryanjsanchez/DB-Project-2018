
from handler.users import UserHandler
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

@app.route('/login/')
def log():
    return "No logging!"
@app.route('/ChatApp/users/<int:uid>')
def getUserById(uid):
    return UserHandler().getUserById(uid)

@app.route('/ChatApp/users/<int:uid>/contacts')
def getContactsById(uid):  
    return UserHandler().getContactsById(uid)

if __name__ == '__main__':
    app.run(debug=True)





