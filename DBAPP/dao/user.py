from config.dbconfig import pg_config
import psycopg2
from psycopg2 import ProgrammingError
class UserDAO:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )

        self.conn = psycopg2.connect(connection_url)

    
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid,ufirstname,ulastname,uphone,uemail,uusername,upassword,uisactive from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByID(self, uid):
        cursor = self.conn.cursor()
        query = "select uid,ufirstname,ulastname,uphone,uemail,uusername,upassword,uisactive from users " \
                "where uid = %s;"
        cursor.execute(query,(uid,))
        result = cursor.fetchone()         
        return result  

    def getUserByUserName(self,username):
        cursor = self.conn.cursor()
        query = "select * from users where uusername = %s"
        cursor.execute(query,(username,))
        result = cursor.fetchone()       
        return result     

    #Returns a collection of users composing a contact list.
    def getContactsByID(self, uid):
        cursor = self.conn.cursor()
        query  = "select U.ufirstname, U.ulastname " \
                 "from users as U natural inner join contact as C "\
                 "where C.ccontact = %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,firstname,lastname,phone,email,username,password,isactive):
        cursor = self.conn.cursor()
        query = "insert into users(ufirstname,ulastname,uphone,uemail,uusername,upassword,uisactive) "\
                "values (%s,%s,%s,%s,%s,%s,%s) returning uid;"
        cursor.execute(query,(firstname,lastname,phone,email,username,password,isactive,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid
    
    def login(self, username, password):
        cursor = self.conn.cursor()
        result = []
        try:
            query = "select uusername,uid from users where uusername = %s and upassword = %s;"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
        except ProgrammingError as Login_Fail:
            print("No Log", Login_Fail)
            return result
        return result

    def newContact(self, uid, firstname, lastname, emailphone):
        cursor = self.conn.cursor()
        result = []
        query = "select uid " \
                "from users " \
                "where upper(ufirstname) = %s " \
                "and upper(ulastname) = %s " \
                "and (upper(uemail) = %s or uphone = %s)"
        cursor.execute(query, (firstname, lastname, emailphone, emailphone))
        contact = cursor.fetchone()[0]
        if contact:
            query = "insert into contact(ccontact, uid) " \
                    "values (%s, %s);"
            cursor.execute(query, (uid, contact))
            self.conn.commit()


    def getTopPerDay(self):
        cursor = self.conn.cursor()
        query = "with sample as (select uusername, date(mtimestamp)as day , count(*) as count from message natural inner join users group by uusername, day order by  day desc, count desc) select uusername , MAX.DAY, MAX.tot from (select sample.day as DAY, max(sample.count) AS tot from (select uusername, date(mtimestamp)as day , count(*) as count from message natural inner join users group by uusername, day order by  day desc, count desc) as sample group by DAY order by DAY) as MAX, sample where sample.day = MAX.DAY and MAX.tot = sample.count  and MAX.DAY> CURRENT_DATE - 7 order by MAX.DAY"

        print(query)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



