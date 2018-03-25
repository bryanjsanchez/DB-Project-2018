from flask import jsonify,request
from dao.user import UserDAO
class UserHandler:
    #Maps a UserDAO to a dictionary
    def mapToDict(self,row):
        result = {}
        result['uid'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        result['phone'] = row[3]
        result['email'] = row[4]
        result['username'] = row[5]
        result['password'] = row[6]#Not sure if password should be displayed.
        result['isActive'] = row[7]
        return result
    def mapContactsToDict(self,id):
        dao = UserDAO()
        contacts = dao.getContactsById(id)
        if contacts:
            mapped_contacts = {}
            for c in contacts:
                mapped_contacts[c[0]] = self.mapToDict(c)
            return mapped_contacts
        else:
            return None
        
        
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)
        
    def getUserById(self,id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result == None:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(User=self.mapToDict(result))
    def getContactsById(self,id):
        result = self.mapContactsToDict(id)
        if result == None:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(Contacts=result)
    
        