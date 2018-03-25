from flask import jsonify,request
from dao.hashtag import HashtagDAO

class HashtagHandler:
    #Maps a HashtagDAO to a dictionary

    def mapToDict(self, row):
        result = {}
        result['hid'] = row[0]
        result['htext'] = row[1]
        result['hmessageid'] = row[2]
        return result
        
    def getAllHashtags(self):
        dao = HashtagDAO()
        result = dao.getAllHashtags()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)

    def getHashtagsByText(self, text):
        dao = HashtagDAO()
        result = dao.getHashtagsByText(text)
        mapped_result = []
        if result == None:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        else:
            return jsonify(Hashtag=mapped_result)

    def getHashtagsByMessageID(self, messageid):
        dao = HashtagDAO()
        result = dao.getHashtagByMessageID(messageid)
        mapped_result = []
        if result == None:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapToDict(r))
        else:
            return jsonify(Hashtag=mapped_result)
