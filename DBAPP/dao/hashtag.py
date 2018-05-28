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
        query = "select hid,htext,hcount from hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagByID(self, hid):
        cursor = self.conn.cursor()
        query = "select * from hashtag " \
                "where hid = {};".format(hid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagByText(self, text):
        cursor = self.conn.cursor()
        query = "select * from hashtag " \
                "where htext = '%s';"
        cursor.execute(query,(text,))
        result = []
        for row in cursor:
            result.append(row)
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
        existingHashtags = self.getAllHashtags()
        
        if existingHashtags:
            for r in existingHashtags:
                if htext == r[1]:
                    query = "update hashtag "\
                            "set hcount = hcount +1 "\
                            "where htext = %s returning hid;"
                    cursor.execute(query,(htext,))
                    hid = cursor.fetchone()[0]
                    self.conn.commit()
                    query = "insert into messagehashtag(mid,hid) "\
                    "values (%s,%s);"
                    cursor.execute(query,(mid,hid,))
                    self.conn.commit()
                    return hid
        else:
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