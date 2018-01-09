__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class resourcesDAO:
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

    def getResourceById(self, res_id):
        cursor = self.conn.cursor()
        query = "select * from resources where res_id = %s;"
        cursor.execute(query, (res_id,))
        result = cursor.fetchone()
        return result


    def getSuppliersByResourcesId(self, res_ID):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from supplies natural inner join suppliers where res_ID=%s;"
        cursor.execute(query, (res_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesInNeed(self):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty  from resources natural inner join request where resources.qty = 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesInNeedByCategoryKeyword(self,category):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty  from resources natural inner join request where resources.qty = 0 and category like %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #### puede ser igual a cero??
    def getResourcesByQty(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from resources where qty > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailableByCategoryKeyword(self, category):
        cursor = self.conn.cursor()
        query = "select * from resources where qty > 0 and category like %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategory(self, category):
        cursor = self.conn.cursor()
        query = "select * from resources where category = %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress natural inner join region where region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryandRegion(self, category, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join  suppliersaddress natural inner join region where category = %s and region = %s;"
        cursor.execute(query, (category, region))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCity(self, city):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByRegion(self,  region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress natural inner join region where region = %s;"
        cursor.execute(query, (res_ID, region))
        result = cursor.fetchone()
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesRequestedByApplicantID(self, apl_ID):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join request where apl_ID = %s;"
        cursor.execute(query,(apl_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryandQty(self, category, qty):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources where category=%s and qty=%s;"
        cursor.execute(query,(category,qty))
        result = []
        for row in cursor:
            result.append(row)
        return result




