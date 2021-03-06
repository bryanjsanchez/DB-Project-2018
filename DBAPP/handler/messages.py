from dao.message import MessageDAO
from handler.hashtags import HashtagHandler
from flask import jsonify

class MessageHandler:

    # Maps a MessageDAO to a dictionary
    def mapToDict(self,row):
        result = {}
        result['mid'] = row[0]
        result['uid'] = row[1]
        result['cgid'] = row[2]
        result['mtext'] = row[3]
        result['mtimestamp'] = row[4]
        result['mrepliedmid'] = row[5]
        return result
    


    def mapUserMsgToDict(self,row):
        result = {}
        result['ufirstname'] = row[0]
        result['ulastname'] = row[1]
        result['mtext'] = row[2]
        result['mtimestamp'] = row[3]
        result['mrepliedmid'] = row[4]
        return result
    
    def mapUserToDict(self,row):
        result = {}
        result['uusername'] = row[0]
        return result

    def mapMsgReactionToDict(self,row):
        result = {}
        result['mrlike'] = row[0]
        result['uusername'] = row[1]
        return result

    def buildMessageAttributes(self,mid,uid,cgid,mtext,mtimestamp,mrepliedmid):
        result = {}
        result['mid'] = mid
        result['uid'] = uid
        result['cgid'] = cgid
        result['mtext'] =mtext
        result['mtimestamp'] = mtimestamp
        result['mrepliedmid'] = mrepliedmid
        return result
    
    def buildLikeDislikeAttributes(self,uid,mid,mrlike,mrtimestamp):
        result = {}
        result['uid'] = uid
        result['mid'] = mid
        result['mrlike'] = mrlike
        result['mrtimestamp'] = mrtimestamp
        return result

    def mapMessageDays(self, row):
        result = {}
        result['Day'] = row[0]
        result['Count'] = row[1]
        return result
    ##### Handlers #####

    def getAllMessages(self):
         dao = MessageDAO()
         result = dao.getAllMessages()
         mapped_result = []
         for r in result:
            mapped_result.append(self.mapToDict(r))
         return jsonify(Message=mapped_result)

    def getMessageByID(self, mid):
        dao = MessageDAO()
        result = dao.getMessageByID(mid)
        if result == None:
            return jsonify(Error="Not Found"), 404
        return jsonify(Message=self.mapToDict(result))

    def getAllMessagesByUser(self, uid):
        dao = MessageDAO()
        result = dao.getAllMessagesByUser(uid)
        mapped_result = []
        if len(result) == 0:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapUserMsgToDict(r))
        return jsonify(Messages=mapped_result)

    def getAllMessageLikesByMID(self, mid):
        dao = MessageDAO()
        result = dao.getAllMessageLikesByMID(mid)
        mapped_result = []
        if len(result) == 0:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapMsgReactionToDict(r))
        return jsonify(MessageLikes=mapped_result)

    def getNumberOfLikesByMID(self, mid):
        dao = MessageDAO()
        result = dao.getNumberOfLikesByMID(mid)
        return jsonify(NumberOfLikes=result)

    def getAllMessageDislikesByMID(self, mid):
        dao = MessageDAO()
        result = dao.getAllMessageDislikesByMID(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for r in result:
            mapped_result.append(self.mapMsgReactionToDict(r))
        return jsonify(MessageDislikes=mapped_result)

    def getNumberOfDislikesByMID(self, mid):
        dao = MessageDAO()
        result = dao.getNumberOfDislikesByMID(mid)
        return jsonify(NumberOfDislikes=result)
    
    def getUsersThatLikedMessageByMID(self,mid):
        dao = MessageDAO()
        result = dao.getUsersThatLikedMessageByMID(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for row in result:
            mapped_result.append(self.mapUserToDict(row))
        return jsonify(Users=mapped_result)

    def getUsersThatDislikedMessageByMID(self,mid):
        dao = MessageDAO()
        result = dao.getUsersThatDislikedMessageByMID(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="Not Found"), 404
        for row in result:
            mapped_result.append(self.mapUserToDict(row))
        return jsonify(Users=mapped_result)


    def insertMessageJson(self,json):
        uid = json["uid"]
        cgid = json["cgid"]
        mtext = json["mtext"]
        mtimestamp = json["mtimestamp"]
        mrepliedmid = json["mrepliedmid"]
        #print(str(uid)+"\n"+str(cgid)+"\n"+mtext+"\n"+mtimestamp+"\n"+str(mrepliedmid)+"\n")
        #print("\n\n" + json["timestamp"] + "\n\n")        
    
        if uid!=None and cgid!=None and mtext!=None and mtimestamp!=None and mrepliedmid!=None:
            dao = MessageDAO()
            hHandler = HashtagHandler()            
            mid = dao.insert(uid,cgid,mtext,mtimestamp,mrepliedmid)
            hashtagJSON = {}
            hashtagJSON["mtext"] = mtext
            hashtagJSON["mid"] = mid
            hHandler.insertHashtagJson(hashtagJSON)
            result = self.buildMessageAttributes(mid,uid,cgid,mtext,mtimestamp,mrepliedmid)
            return jsonify(Message=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMessageLikeJson(self,json):
        uid = json["uid"]
        mid = json["mid"]
        mrtimestamp = json["mrtimestamp"]
        mrlike = "true"

        if uid!=None and mid!=None and mrtimestamp!=None:
            dao = MessageDAO()
            dao.insertLikeDislike(uid,mid,mrlike,mrtimestamp)
            result = self.buildLikeDislikeAttributes(uid,mid,mrlike,mrtimestamp)
            return jsonify(Like = result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMessageDislikeJson(self,json):
        uid = json["uid"]
        mid = json["mid"]
        mrtimestamp = json["mrtimestamp"]
        mrlike = "false"

        if uid!=None and mid!=None and mrtimestamp!=None:
            dao = MessageDAO()
            dao.insertLikeDislike(uid,mid,mrlike,mrtimestamp)
            result = self.buildLikeDislikeAttributes(uid,mid,mrlike,mrtimestamp)
            return jsonify(Dislike = result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400   

    def getMessagePerDay(self):
        dao = MessageDAO()
        result = dao.getMessagePerDay()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapMessageDays(r))
        return jsonify(Messages_Per_Day=mapped_result)

    def getRepliesPerDay(self):
        dao = MessageDAO()
        result = dao.getRepliesPerDay()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapMessageDays(r))
        return jsonify(Replies_Per_Day=mapped_result)

    def getLikesPerDay(self):
        dao = MessageDAO()
        result = dao.getLikesPerDay()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapMessageDays(r))
        return jsonify(Likes_Per_Day=mapped_result)

    def getDislikesPerDay(self):
        dao = MessageDAO()
        result = dao.getDislikesPerDay()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapMessageDays(r))
        return jsonify(Dislikes_Per_Day=mapped_result)
        
