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
    
    def insertHashtagJson(self,json):
        mtext = json["mtext"] 
        mid = json["mid"] 
        hashtags = self.hashes(mtext)
        dao = HashtagDAO()
        for h in hashtags:
            hid = dao.insert(h,mid)
        #result = self.buildAttributes(hid,htext)
            print(hid)
            print("\n\n\nPRINT\n\n\n")


         
    def hashes(self,inputString):
        hashTable = []
        c = 0
        if '#' in inputString:
            hashString = ""
            for j in range(0, len(inputString)):
                if inputString[j] == '\"' and c!=2:
                    c = c + 1
                    continue
                if inputString[j] == '#' and c!=1:
                    hashString = self.hash(inputString[j:len(inputString)])
                    #print("Found a hash" + hashString)
                    hashTable.append(hashString)
                    continue
        return hashTable  
    
    def hash(self,inputString):
        invalid = [' ','#','!','?','.']
        print("Input given: " + inputString)
        hashString = "#"
        for i in range(1,len(inputString)):
            if inputString[i] not in invalid:
                hashString = hashString + inputString[i]
            else:
                break
        return hashString



        

