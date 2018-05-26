from config.dbconfig import pg_config
import psycopg2
class MessageDAO:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )

        self.conn = psycopg2.connect(connection_url)
        

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select mid,uid,cgid,mtext,mtimestamp,mrepliedmid from message"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    
    def getMessageByID(self, mid):
        cursor = self.conn.cursor()
        query = "select mid,uid as mauthor,mtext,mtimestamp,mrepliedmid "\
                " from message " \
                "where mid = %s"
        cursor.execute(query,(mid,))
        result = []
        
        for row in cursor:
            print(row)
            result.append(row)
        return result
    
    def getAllMessagesByUser(self, uid):
        cursor = self.conn.cursor()
        query = "select ufirstname,ulastname,mtext,mtimestamp,mrepliedmid " \
                "from users natural inner join message "\
                "where uid = %s;"
        cursor.execute(query,(uid,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageLikesByMID(self, mid):
        cursor = self.conn.cursor()
        query = "select mrlike,uusername from messagereaction natural inner join users " \
                "where mid = %s" \
                "and mrlike = true"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfLikesByMID(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from messagereaction " \
                "where mid = %s" \
                "and mrlike = true"
        cursor.execute(query,(mid,))
        result = cursor.fetchone()
        return result[0]

    def getAllMessageDislikesByMID(self, mid):
        cursor = self.conn.cursor()
        query = "select mrlike,uusername from messagereaction natural inner join users " \
                "where mid = %s" \
                "and mrlike = false"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfDislikesByMID(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from messagereaction " \
                "where mid = %s " \
                "and mrlike = false"
        cursor.execute(query,(mid,))
        result = cursor.fetchone()
        return result[0]

    def getUsersThatLikedMessageByMID(self,mid):
        cursor = self.conn.cursor()
        query = "select uusername " \
                "from users natural inner join messagereaction "\
                "where mid = %s "\
                "and mrlike = true"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUsersThatDislikedMessageByMID(self,mid):
        cursor = self.conn.cursor()
        query = "select uusername " \
                "from users natural inner join messagereaction "\
                "where mid = %s "\
                "and mrlike = false"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        
        
    def insert(self,uid,cgid,mtext,mtimestamp,mrepliedmid):
        cursor = self.conn.cursor()
        query = "insert into message(uid,cgid,mtext,mtimestamp,mrepliedmid) "\
                "values (%s,%s,%s,%s,%s) returning mid;"
        cursor.execute(query,(uid,cgid,mtext,mtimestamp,mrepliedmid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid
    
    def insertLikeDislike(self,uid,mid,mrlike):
        cursor = self.conn.cursor()
        query = "insert into messagereaction(uid,mid,mrlike) "\
                "values (%s,%s,%s);"
        cursor.execute(query,(uid,mid,mrlike,))
        self.conn.commit()

    

