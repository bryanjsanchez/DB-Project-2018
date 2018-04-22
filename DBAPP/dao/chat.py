from config.dbconfig import pg_config
import psycopg2
class ChatDAO:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )

        self.conn = psycopg2._connect(connection_url)
        

    def getAllChatGroups(self):
        cursor = self.conn.cursor()
        query = "select * from chatgroup"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
       

    def getChatMsgsByUserId(self,cgid,uid):
        cursor = self.conn.cursor()
        query = "select cgname,ufirstname,ulastname,mtext " \
                "from (chatgroup natural inner join chatmember) "\
                "natural inner join (users natural inner join message) "\
                "where cgid = %s"\
                "and uid = %s"
        cursor.execute(query,(cgid,uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatByID(self, cgid):
        cursor = self.conn.cursor()
        query = "select * from chatgroup " \
                "where cgid = %s;"
        cursor.execute(query,(cgid,))
        result = []
        for row in cursor:
           result.append(row)

        return result

    def getChatGroupsByUserId(self,uid):
        cursor = self.conn.cursor()
        query = "select cgid,cgname   " \
                "from (users natural inner join chatmember) "\
                "natural join chatgroup "\
                "where uid = %s"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result