
from handler.users import UserHandler
from handler.messages import MessageHandler
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

@app.route('/login/')
def log():
    return "No logging!"

@app.route('/ChatApp/users')
def getAllUsers():
    return UserHandler().getAllUsers()
        
@app.route('/ChatApp/users/<int:uid>')
def getUserById(uid):
    return UserHandler().getUserById(uid)

@app.route('/ChatApp/users/<int:uid>/contacts')
def getContactsById(uid):  
    return UserHandler().getContactsById(uid)

@app.route('/ChatApp/messages')
def getAllMessages():
    return MessageHandler().getAllMessages()

@app.route('/ChatApp/messages/<int:mid>')
def getMessageById(mid):
    return MessageHandler().getMessageById(mid)

@app.route('/ChatApp/messages/<int:uid>')
def getAllMessagesByUId(uid):
    return MessageHandler().getAllMessagesByUId(uid)



if __name__ == '__main__':
    app.run(debug=True)





