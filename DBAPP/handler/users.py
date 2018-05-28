from flask import jsonify
from dao.user import UserDAO

class UserHandler:

    #Maps a UserDAO to a dictionary
    def mapToDict(self,row):
        result = {}
        #print("\n\n\n\n" + row + "\n\n\n\n")
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

    def mapTop(self, row):
        result = {}
        result['uusername'] = row[0]
        result['day'] = row[1]
        result['count'] = row[2]
        return result
    
    def buildUserAttributes(self,uid,firstname,lastname,phone,email,username,password,isactive):
        result = {}
        result['uid'] = uid
        result['firstname'] = firstname
        result['lastname'] = lastname
        result['phone'] = phone
        result['email'] = email
        result['username'] = username
        result['password'] = password
        result['isactive'] = isactive
        return result


    ##### Handlers #####

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)
        
    def getUserByID(self,uid):
        dao = UserDAO()
        result = dao.getUserByID(uid)
        if not result:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(User=self.mapToDict(result))
    
    def getUserByUserName(self,username):
        dao = UserDAO()
        result = dao.getUserByUserName(username)
        if not result:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(User=self.mapToDict(result))

    def getAllContactsByID(self, id):
        result = self.mapContactsToDict(id)
        if result == None:
            return jsonify(Error="Not Found"), 404
        else:
            return jsonify(Contacts=result)


    def insertUserJson(self,json):
        firstname = json["firstname"]
        lastname = json["lastname"]
        phone = json["phone"]
        email = json["email"]
        username = json["username"]
        password = json["password"]
        isactive = "true"
        if firstname!=None and lastname!=None and phone!=None and email!=None and username!=None and password!=None and isactive!=None:
            dao = UserDAO()
            uid = dao.insert(firstname,lastname,phone,email,username,password,isactive)
            result = self.buildUserAttributes(uid,firstname,lastname,phone,email,username,password,isactive)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
        return None
    
    def login(self, username, password):
        dao = UserDAO()
        result = dao.login(username, password)
        return result

    def newContact(self, form, uid):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            print(form)
            firstname = form['firstname'].upper()
            lastname = form['lastname'].upper()
            emailphone = form['emailphone'].upper()
            if uid and firstname and lastname and emailphone:
                dao = UserDAO()
                dao.newContact(uid, firstname, lastname, emailphone)
                return jsonify(Success="Successfully added contact"), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def getTopPerDay(self):
        dao = UserDAO()
        result = dao.getTopPerDay()
        print(result)
        if result is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapTop(r))
            return jsonify(Top_Users=mapped_result)


