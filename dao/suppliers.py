__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class suppliersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                          pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from suppliers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSuppliersAddress(self):
        cursor = self.conn.cursor()
        query = "select * from suppliersaddress "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSuppliersInfo(self):
        cursor =self.conn.cursor()
        query = "select supp_ID,first_name,last_name,street,urb_conde,num,city,state,zip,region,gps_local from suppliers natural inner join suppliersaddress natural inner join region"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersById(self, supp_id):
        cursor = self.conn.cursor()
        query = "select * from suppliers where supp_id = %s;"
        cursor.execute(query, (supp_id,))
        result = cursor.fetchone()
        return result

    def getSuppliersByName(self, first_name):
        cursor = self.conn.cursor()
        query = "select * from suppliers where first_name = %s;"
        cursor.execute(query, (first_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress natural inner join region where region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByNameAndLocation(self, first_name, gps_local):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress where first_name = %s and gps_local = %s;"
        cursor.execute(query, (first_name, gps_local))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByNameAndAddress(self, first_name, street, urb_conde, num, city, state, zip):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress where first_name = %s and street = %s and urb_conde = %s and num = %s and city = %s and state = %s and zip = %s;"
        cursor.execute(query, (first_name, street, urb_conde, num, city, state, zip))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLocation(self, gps_local):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress where gps_local = %s;"
        cursor.execute(query, (gps_local,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAddress(self, street, urb_conde, num, city, state, zip):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress where street = %s and urb_conde = %s and num = %s and city = %s and state = %s and zip = %s;"
        cursor.execute(query, (street, urb_conde, num, city, state, zip))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLastname(self, last_name):
        cursor = self.conn.cursor()
        query = "select * from suppliers where last_name = %s;"
        cursor.execute(query, (last_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsBySuppliersID(self, supp_ID):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name, acct_num, balance from accounts natural inner join suppliers where supp_ID=%s;"
        cursor.execute(query, (supp_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySuppliersID(self, supp_ID):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies where supp_ID=%s;"
        cursor.execute(query, (supp_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByResourceCategory(self, category):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from supplies natural inner join resources natural inner join suppliers where category=%s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByNameAndRegion(self, first_name, region):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from suppliers natural inner join suppliersaddress natural inner join where first_name = %s and region = %s;"
        cursor.execute(query, (first_name,region))
        result = []
        for row in cursor:
            result.append(row)
        return result