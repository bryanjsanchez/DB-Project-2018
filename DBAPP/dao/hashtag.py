from config.dbconfig import pg_config
import psycopg2
class HashtagDAO:

    def __init__(self):

        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )

        self.conn = psycopg2.connect(connection_url)
    
    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagByID(self, hid):
        cursor = self.conn.cursor()
        query = "select hid,htext,hcount from hashtag " \
                "where hid = %s;"
        cursor.execute(query,(hid,))
        result = cursor.fetchone()        
        return result

    def getHashtagByText(self, text):
        cursor = self.conn.cursor()
<<<<<<< Updated upstream
        query = "select * from hashtag " \
                "where htext = '#{}';".format(text)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
=======
        print("\n\n\n" + text + "\n\n\n")
        hashtag = '#'+text
        query = "select hid,htext,hcount from hashtag " \
                "where htext = %s;"
        cursor.execute(query,(hashtag,))
        result = cursor.fetchone()        
>>>>>>> Stashed changes
        return result

    def getTop10Hashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag " \
                "order by hcount desc " \
                "limit 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    #Inserts a new hashtag
    def insert(self,htext,mid):
        cursor = self.conn.cursor()
        query = "insert into hashtag (htext,hcount) "\
                "values (%s,%s) returning hid;"
        cursor.execute(query,(htext,1,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into messagehashtag(mid,hid) "\
                "values (%s,%s);"
        cursor.execute(query,(mid,hid,))

        self.conn.commit()
        return hid

    def getTrending(self):
        cursor = self.conn.cursor()
        query = "select h.htext, count(*) as Hits from hashtag as h, messagehashtag as mh, message as m "\
                "where h.hid = mh.hid and mh.mid = m.mid and m.mtimestamp > current_date - 360"\
                "group by h.htext order by Hits desc, h.htext asc limit 10"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
