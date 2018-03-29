class ChatDAO:

    def __init__(self):
         #ChatID, UserID, ChatName
        C1 = [556, 541, 'MemesandSlander']
        C2 = [556, 542, 'MemesandSlander']
        C3 = [762, 542, 'NormiesChat']
        C4 = [762, 543, 'NormiesChat']
        self.data = []
        self.data.append(C1)
        self.data.append(C2)
        self.data.append(C3)
        self.data.append(C4)

    def getAllChats(self):
        results = []
        for m in self.data:
            if m[2] not in self.data:
                results.append(m)
        return results

    def getChatByNames(self, text):
        for m in self.data:
            if m[2] == text:
                return m
        return None

    def getChatByUser(self, User):
        results = []
        for m in self.data:
            if m[1] == User:
                results.append(m)
        return results

    def getChatByID(self, ID):
        results = []
        for m in self.data:
            print(m[0])
            if m[0] == ID:
                results.append(m)
        return results