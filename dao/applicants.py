__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class applicantsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                          pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllApplicants(self):
        cursor = self.conn.cursor()
        query = "select * from applicants;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllApplicantsAddress(self):
        cursor = self.conn.cursor()
        query = "select * from applicantsaddress "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllApplicantsInfo(self):
        cursor =self.conn.cursor()
        query = "select apl_ID,first_name,last_name,street,urb_conde,num,city,state,zip,gps_local,region from applicants natural inner join applicantsaddress natural inner join region"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantById(self, apl_id):
        cursor = self.conn.cursor()
        query = "select * from applicants where apl_id = %s;"
        cursor.execute(query, (apl_id,))
        result = cursor.fetchone()
        return result

    def getApplicantByName(self, first_name):
        cursor = self.conn.cursor()
        query = "select * from applicants where first_name = %s;"
        cursor.execute(query, (first_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantByCity(self, city):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress natural inner join region where region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByNameAndLocation(self, first_name, gps_local):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where first_name = %s and gps_local = %s;"
        cursor.execute(query, (first_name, gps_local))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByNameAndRegion(self, first_name, region):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress natural inner join region where first_name = %s and region = %s;"
        cursor.execute(query, (first_name, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByNameAndAddress(self, first_name, street, urb_conde, num, city, state, zip):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where first_name = %s and street = %s and urb_conde = %s and num = %s and city = %s and state = %s and zip = %s;"
        cursor.execute(query, (first_name, street, urb_conde, num, city, state, zip))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByLocation(self, gps_local):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where gps_local = %s;"
        cursor.execute(query, (gps_local,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByAddress(self, street, urb_conde, num, city, state, zip):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where street = %s and urb_conde = %s and num = %s and city = %s and state = %s and zip = %s;"
        cursor.execute(query, (street, urb_conde, num, city, state, zip))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getApplicantsByNameAndLastname(self, first_name, last_name):
        cursor = self.conn.cursor()
        query = "select apl_ID,first_name,last_name from applicants where first_name= %s and last_name = %s;"
        cursor.execute(query, (first_name, last_name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardsByApplicantsID(self, apl_ID):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name, card_num, exp_date, balance from creditcards natural inner join applicants where apl_ID=%s;"
        cursor.execute(query, (apl_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, first_name, last_name):
        cursor = self.conn.cursor()
        query = "insert into Applicants(first_name,last_name) values (%s,%s) returning apl_ID;"
        cursor.execute(query,(first_name,last_name))
        apl_ID = cursor.fetchone()[0]
        self.conn.commit()
        return apl_ID

    def insertAddress(self, apl_ID, street, urb_conde, num, city, state, zip, gps_local):
        rcity=city
        cursor = self.conn.cursor()
        query = "insert into ApplicantsAddress(apl_ID, rid,street, urb_conde, num,city,state,zip,gps_local) values " \
                "(%s, (select rid from Region where city = %s),%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query, (apl_ID, rcity,street,urb_conde,num,city,state,zip,gps_local))
        self.conn.commit()

    def insertCreditCard(self, card_num, apl_ID, exp_date, balance):
        cursor = self.conn.cursor()
        query = "insert into CreditCards(card_num,apl_ID, exp_date, balance) values (%s,%s,%s,%s);"
        cursor.execute(query, (card_num, apl_ID, exp_date, balance))
        self.conn.commit()

    def updateCreditCard(self,card_num,exp_date,balance):
        cursor = self.conn.cursor()
        query = "update CreditCards set exp_date=%s, balance=%s where card_num=%s;"
        cursor.execute(query,(exp_date,balance,card_num))
        self.conn.commit()

    def getCreditCardByCardNum(self, card_num):
        cursor =self.conn.cursor()
        query = "select * from CreditCards where card_num=%s"
        cursor.execute(query,(card_num))
        result = cursor.fetchone()
        return result






