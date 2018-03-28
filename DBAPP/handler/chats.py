from flask import jsonify, request
from dao.chat import chatDAO

class chatHandler:

    def mapToDict(self, row):
        result = {}
        result['cid'] = row[0]
        result['uid'] = row[1]
        result['cname'] = row[2]
        return result

    def getAllChats(self):
        dao = chatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chat=mapped_result)

    def getChatByName(self, text):
        dao = chatDAO()
        result = dao.getChatByNames(text)
        print(result)
        mapped_result = []
        if result is None:
            return jsonify(Error="Not Found"), 404
        # for r in result:
        #     mapped_result.append(self.mapToDict(r))
        else:
            mapped_result = self.mapToDict(result)
        return jsonify(Chat=mapped_result)


    def getChatByUser(self, uid):
        dao = chatDAO()
        result = dao.getChatByUser(uid)
        mapped_result = []
        if result is None:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)

    def getChatByID(self, cid):
        dao = chatDAO()
        result = dao.getChatByID(cid)
        mapped_result = []
        print('Getting Chat')
        if result is None:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)
