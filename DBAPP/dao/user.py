from config.dbconfig import pg_config
import psycopg2
class UserDAO:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )

        self.conn = psycopg2._connect(connection_url)

    
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByID(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users " \
                "where uid = {};".format(uid)
        cursor.execute(query)
        result = []
        for  row in cursor:
            result.append(row)
        return result       

    #Returns a collection of users composing a contact list.
    def getContactsByID(self, id):
        cursor = self.conn.cursor()
        query  = ""
        result = []
        #Still need to get the query for this operation
        return result
