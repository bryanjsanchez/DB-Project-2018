class HashtagDAO:

    def __init__(self):
        H1 = [101, 'Hello', 1]
        H2 = [102, 'NewYear', 2]
        H3 = [103, 'DoingGood', 1]
        H4 = [104, 'LetsParty', 1]
        H5 = [105, 'YOLO', 2]
        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)
        self.data.append(H5)
    
    def getAllHashtags(self):
        return self.data

    def getHashtagByID(self, hid):
        for h in self.data:
            if h[0] == hid:
                return h
        return None

    def getHashtagByText(self, text):
        for h in self.data:
            if h[1] == text:
                return h
        return None

    def getTop10Hashtags(self):
        self.data.sort(key=lambda x:x[2], reverse=True)
        return self.data[:10]


