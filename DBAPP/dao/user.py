class UserDAO:

    def __init__(self):
        U1 = [541,'Juan','Ocasio Rivera','787-854-9124','juan.ocasio@email.com','jocasio','password1','true']
        U2 = [542,'Juaquin','Velazquez Olivier','939-123-9863','juanquin.velazquez@email.com','jvelazquez','password2','false']
        U3 = [543,'Silva','Costa Miranda','787-191-9999','silva.costa@email.com','scosta','password3','false']
        U4 = [544,'Omar','Cruz Fuentes','787-555-4444','omar.cruz@email.com','ocruz','password4','true']
        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
    
    def getAllUsers(self):
        return self.data
    
    def getUserByID(self, id):
        for u in self.data:
            if u[0] == id:
                return u
        return None

    #Returns a collection of users composing a contact list.
    def getContactsByID(self, id):
        Contacts = [] #If no condition is met the function will return an empty list.
        if id == 541:
            Contacts.append(self.data[1])
            Contacts.append(self.data[3])
        elif id == 542:
            Contacts.append(self.data[0])
            Contacts.append(self.data[2])
            Contacts.append(self.data[3])
        elif id == 543:
            Contacts.append(self.data[1])
            Contacts.append(self.data[3])
        elif id ==544:
            Contacts.append(self.data[0])
            Contacts.append(self.data[1])
            Contacts.append(self.data[2])
        return Contacts