from flask import jsonify
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
    
    def mapContactToDict(self,row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        return result

    def mapContactsToDict(self,id):
        dao = UserDAO()
        contacts = dao.getContactsByID(id)
        if contacts:
            mapped_contacts = []
            for c in contacts:
                mapped_contacts.append(self.mapContactToDict(c))
            return mapped_contacts
        else:
            return None


    ##### Handlers #####

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)
        
    def getUserByID(self,uid):
        dao = UserDAO()
        result = dao.getUserByID(uid)
        if not result:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(User=result)
    
    def getUserByUserName(self,username):
        dao = UserDAO()
        result = dao.getUserByUserName(username)
        if not result:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(User=result)

    def getAllContactsByID(self, id):
        result = self.mapContactsToDict(id)
        if result == None:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(Contacts=result)