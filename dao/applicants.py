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
        result = cursor.fetchone()
        return result

    def getApplicantByCity(self, city):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where city = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        return result

    def getApplicantByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join region where region = %s;"
        cursor.execute(query, (region,))
        result = cursor.fetchone()
        return result

    def getApplicantsByNameAndLocation(self, first_name, gps_local):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name from applicants natural inner join applicantsaddress where first_name = %s and gps_local = %s;"
        cursor.execute(query, (first_name, gps_local))
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

    def getApplicantsByLastname(self, last_name):
        cursor = self.conn.cursor()
        query = "select * from applicants where last_name = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardsByApplicantsID(self, apl_ID):
        cursor = self.conn.cursor()
        query = "select apl_ID, first_name, last_name, card_num, exp_date, balance from creditcards natural inner join applicants where apl_ID=%s;"
        cursor.execute(query, (apl_ID,))
        result = cursor.fetchone()
        return result



