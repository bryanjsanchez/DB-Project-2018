class HashtagDAO:
    def __init__(self):
        H1 = [101, 'Hello', 120]
        H2 = [102, 'NewYear', 120]
        H3 = [103, 'DoingGood', 121]
        H4 = [104, 'NewYear', 121]
        H5 = [105, 'LetsParty', 122]
        H6 = [106, 'YOLO', 122]
        H7 = [107, 'YOLO', 123]
        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)
        self.data.append(H5)
        self.data.append(H6)
        self.data.append(H7)
    
    def getAllHashtags(self):
        return self.data

    def getHashtagsByText(self, text):
        hashtags = []
        for h in self.data:
            if h[1] == text:
                hashtags.append(h)
        return hashtags

    def getHashtagByMessageID(self, messageid):
        hashtags = []
        for h in self.data:
            if h[2] == messageid:
                hashtags.append(h)
        return hashtags


    
    
            
        