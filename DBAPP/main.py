from handler.users import UserHandler
from handler.messages import MessageHandler
from handler.hashtags import HashtagHandler
from handler.chats import ChatHandler

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

@app.route('/ChatApp/login/')
def log():
    return "No logging!"


##### Routes for Users #####

@app.route('/ChatApp/users')
def getAllUsers():
    return UserHandler().getAllUsers()
        
@app.route('/ChatApp/user/<int:uid>')
def getUserByID(uid):
    return UserHandler().getUserByID(uid)

@app.route('/ChatApp/user/<int:uid>/contacts')
def getAllContactsByID(uid):
    return UserHandler().getAllContactsByID(uid)


##### Routes for Messages #####

@app.route('/ChatApp/messages')
def getAllMessages():
    return MessageHandler().getAllMessages()

@app.route('/ChatApp/messages/<int:mid>')
def getMessageByID(mid):
    return MessageHandler().getMessageByID(mid)

@app.route('/ChatApp/messages/user/<int:uid>')
def getAllMessagesByUser(uid):
    return MessageHandler().getAllMessagesByUser(uid)

@app.route('/ChatApp/messages/<int:mid>/likes')
def getAllMessageLikesByMID(mid):
    return MessageHandler().getAllMessageLikesByMID(mid)

@app.route('/ChatApp/messages/<int:mid>/likes/number')
def getNumberOfLikesByMID(mid):
    return MessageHandler().getNumberOfLikesByMID(mid)

@app.route('/ChatApp/messages/<int:mid>/dislikes')
def getAllMessageDislikesByMID(mid):
    return MessageHandler().getAllMessageDislikesByMID(mid)

@app.route('/ChatApp/messages/<int:mid>/dislikes/number')
def getNumberOfDislikesByMID(mid):
    return MessageHandler().getNumberOfDislikesByMID(mid)


##### Routes for Hashtags #####

@app.route('/ChatApp/hashtags')
def getAllHashtags():
    return HashtagHandler().getAllHashtags()

@app.route('/ChatApp/hashtag=<int:hid>')
def getHashtagByID(hid):
    return HashtagHandler().getHashtagByID(hid)

@app.route('/ChatApp/hashtag/text=<text>')
def getAllHashtagsByText(text):
    return HashtagHandler().getHashtagByText(text)

@app.route('/ChatApp/hashtags/top10')
def getTop10Hashtags():
    return HashtagHandler().getTop10Hashtags()

### Routes For Chats ####

@app.route('/ChatApp/chats')
def getAllChats():
    return ChatHandler().getAllChatGroups()

@app.route('/ChatApp/chat/<int:cgid>')
def getChatbyID(cgid):
    return ChatHandler().getChatByID(cgid)

@app.route('/ChatApp/chats/user/<int:uid>')
def getChatbyUser(uid):
    return ChatHandler().getChatGroupsByUserId(uid)

@app.route('/ChatApp/chats/<int:cgid>/user/<int:uid>/messages')
def getChatbyName(cgid,uid):
    return ChatHandler().getChatMsgsByUserId(cgid,uid)


if __name__ == '__main__':
    app.run(debug=True)
