from dao.message import MessageDAO
from flask import jsonify

class MessageHandler:

    # Maps a MessageDAO to a dictionary
    def mapToDict(self,row):
        result = {}
        result['mid'] = row[0]
        result['mauthor'] = row[1]
        result['mtext'] = row[2]
        result['mtimestamp'] = row[3]
        result['mrepliedmid'] = row[4]
        return result
    def mapUserMsgToDict(self,row):
        result = {}
        result['ufirstname'] = row[0]
        result['ulastname'] = row[1]
        result['mtext'] = row[2]
        result['mtimestamp'] = row[3]
        result['mrepliedmid'] = row[4]
        return result


    ##### Handlers #####

    def getAllMessages(self):
         dao = MessageDAO()
         result = dao.getAllMessages()
         mapped_result = []
         for r in result:
            mapped_result.append(self.mapToDict(r))
         return jsonify(Message = mapped_result)

    def getMessageByID(self, mid):
        dao = MessageDAO()
        result = dao.getMessageByID(mid)
        if result == None:
            return jsonify(Error="Not Found"), 404
        return jsonify(Message=result)    

    def getAllMessagesByUser(self, uid):
        dao = MessageDAO()
        result = dao.getAllMessagesByUser(uid)
        mapped_result = []
        if len(result) == 0:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapUserMsgToDict(r))
        return  jsonify(Messages = mapped_result)