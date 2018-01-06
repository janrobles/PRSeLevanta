__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class applicantsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                          pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesInfo(self):
        cursor =self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, res_id):
        cursor = self.conn.cursor()
        query = "select * from resources where res_id = %s;"
        cursor.execute(query, (res_id,))
        result = cursor.fetchone()
        return result

    def getResourceByCategory(self, category):
        cursor = self.conn.cursor()
        query = "select * from resources where category = %s;"
        cursor.execute(query, (category,))
        result = cursor.fetchone()
        return result

    def getResourcesInNeed(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty = 0;"
        cursor.execute(query, (qty,))
        result = cursor.fetchone()
        return result

    def getResourcesAvailable(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty >= 0;"
        cursor.execute(query, (qty,))
        result = cursor.fetchone()
        return result

    def getResourcesByCategory(self, category):
        cursor = self.conn.cursor()
        query = "select * from resources where category = %s;"
        cursor.execute(query, (category,))
        result = cursor.fetchone()
        return result

    def getResourcesByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join suppliers natural inner join suppliersaddress natural inner join region where region = %s;"
        cursor.execute(query, (region))
        result = cursor.fetchone()
        return result

    def getResourcesByCategoryandRegion(self, category, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join suppliers natural inner join suppliersaddress natural inner join region where category = %s and region = %s;"
        cursor.execute(query, (category, region))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierCity(self, city):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join suppliers natural inner join supplieraddress where city = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        return result










