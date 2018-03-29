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


    ##### Handlers #####

    def getAllHashtags(self):
        dao = HashtagDAO()
        result = dao.getAllHashtags()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)

    def getHashtagByID(self, text):
        dao = HashtagDAO()
        result = dao.getHashtagByID(text)
        if result == None:
            return jsonify(Error="Not Found"), 404
        return jsonify(Hashtag=result)

    def getHashtagByText(self, hid):
        dao = HashtagDAO()
        result = dao.getHashtagByText(hid)
        if result == None:
            return jsonify(Error="Not Found"), 404
        return jsonify(Hashtag=result)

    def getTop10Hashtags(self):
        dao = HashtagDAO()
        result = dao.getTop10Hashtags()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)

