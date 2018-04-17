from flask import jsonify, request
from dao.chat import ChatDAO

class ChatHandler:

    def mapToDict(self, row):
        result = {}
        result['cgid'] = row[0]
        result['cgname'] = row[1]
        return result

    def mapUserMsgsToDict(self,row):
        result = {}
        result['cgname'] = row[0]
        result['mtext'] = row[3]

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
        return jsonify(Hashtag=mapped_result)
