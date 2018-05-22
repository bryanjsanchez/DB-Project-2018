from flask import jsonify, request
from dao.chat import ChatDAO

class ChatHandler:

    def mapToDict(self, row):
        result = {}
        result['Owner'] = row[0]
        result['cgname'] = row[1]
        result['cgid'] = row[2]
        return result

    def mapUserMsgsToDict(self,row):
        result = {}
        result['cgname'] = row[0]
        result['mtext'] = row[3]
        return result

    def mapChatMessageToDict(self, row):
        result = {}
        result['chatname'] = row[0]
        result['mid'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['username'] = row[4]
        result['uid'] = row[5]
        result['text'] = row[6]
        result['date'] = row[7]
        result['time'] = row[8]
        result['likes'] = row[9]
        result['dislikes'] = row[10]
        return result

    def mapOwnersToDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uusername'] = row[1]
        result['cgname'] = row[2]
        return result

    def mapMembersToDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uusername'] = row[1]
        result['cgname'] = row[2]
        return result

    def buildChat(self, cgid, chatname):
        result = {}
        result['cgid'] = cgid
        result['cgname'] = chatname
        return result

    def getAllChatGroups(self):
        dao = ChatDAO()
        result = dao.getAllChatGroups()
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chat=mapped_result)

    def getChatGroupsByUserId(self,uid):
        dao = ChatDAO()
        result = dao.getChatGroupsByUserId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404        
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(ChatGroups=mapped_result)

    def getAllMessagesByChat(self, cgid):
        dao = ChatDAO()
        result = dao.getAllMessagesByChat(cgid)
        mapped_result = []
        if len(result) == 0:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapChatMessageToDict(r))
        return jsonify(Messages=mapped_result)
    
    def getChatMsgsByUserId(self,cgid, uid):
        dao = ChatDAO()
        result = dao.getChatMsgsByUserId(cgid,uid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapUserMsgsToDict(r))
        return jsonify(Messages=mapped_result)

    def getChatByID(self, cgid):
        dao = ChatDAO()
        result = dao.getChatByID(cgid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chat=mapped_result)

    def getChatOwner(self, cgid ):
        dao = ChatDAO()
        result = dao.getChatOwner(cgid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapOwnersToDict(r))
        return jsonify(Chat=mapped_result)

    def getChatMembers(self, cgid):
        dao = ChatDAO()
        result = dao.getChatUsers(cgid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapMembersToDict(r))
        return jsonify(Members=mapped_result)

    def newChat(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            print(form)
            chatname = form['chatname']
            if chatname:
                dao = ChatDAO()
                cgid = dao.newChat(chatname)
                result = self.buildChat(cgid, chatname)
                return jsonify(Chat=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
