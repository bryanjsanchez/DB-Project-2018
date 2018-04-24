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

    def getAllMessagesByChat(self, cgid):
        cursor = self.conn.cursor()
        query = "SELECT " \
                "chatgroup.cgname," \
                "message.mid," \
                "message.uid AS User," \
                "message.mtext AS Text," \
                "to_char(message.mtimestamp, 'DD MON YYYY') as Date," \
                "to_char(message.mtimestamp, 'HH:MI AM') as Time," \
                "COUNT(NULLIF(messagereaction.mrlike=true, true)) AS Likes," \
                "COUNT(NULLIF(messagereaction.mrlike=false, true)) AS Dislikes " \
                "FROM message " \
                "LEFT JOIN messagereaction " \
                "USING(mid) " \
                "NATURAL INNER JOIN chatgroup " \
                "WHERE message.cgid = %s " \
                "GROUP BY message.cgid, message.mid, chatgroup.cgname " \
                "ORDER BY message.mtimestamp;"
        cursor.execute(query, (cgid,))
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

    def getChatOwner(self, cgid):
        cursor = self.conn.cursor()
        query = "select U.uid, U.uusername, CG.cgname "\
                "from Users as U, chatgroup as CG, ownschat as o "\
                "where o.uid = U.uid and o.cgid = CG.cgid and CG.cgid = %s"
        cursor.execute(query,(cgid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatUsers(self, cgid):
        cursor = self.conn.cursor()
        query = "SELECT U.uid, U.uusername, CG.cgname from Users as U, chatmember as CH, chatgroup as CG "\
                "where U.uid = CH.uid and CH.cgid = CG.cgid and CG.cgid = %s"
        cursor.execute(query, (cgid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
