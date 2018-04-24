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
        return result

    def mapChatMessageToDict(self, row):
        result = {}
        result['ChatName'] = row[0]
        result['mid'] = row[1]
        result['uid'] = row[2]
        result['text'] = row[3]
        result['date'] = row[4]
        result['time'] = row[5]
        result['likes'] = row[6]
        result['dislikes'] = row[7]
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


