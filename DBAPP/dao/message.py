class MessageDAO:
    def __init__(self):
        M1 = [120,541,'How are you?#Hello#NewYear','2018-01-08 04:05:06',0]
        M2 = [121,542,'Good, thanks for asking, hope your doing well.#DoingGood#NewYear','2018-01-08 04:07:06',120]
        M3 = [122,542,'Are you going to the party?#LetsParty#YOLO','2018-01-08 04:10:06',0]
        M4 = [123,543,'Yes, I will see you there.#YOLO','2018-01-08 04:12:06',122]
        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)

    def getAllMessages(self):
        return self.data
    
    def getMessageById(self,mid):
        for m in self.data:
            if m[0] == mid:
                return m
        return None
    
    def getAllMessagesByUId(self,uid):
        result = []
        for m in self.data:
            if m[1] == uid:
                result.append(m)
        return result  
        
    
    



        

