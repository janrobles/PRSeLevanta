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


    def getSuppliersByResourcesId(self, res_ID):
        cursor = self.conn.cursor()
        query = "select supp_ID, first_name, last_name from supplies natural inner join suppliers where res_ID=%s;"
        cursor.execute(query, (supp_ID,))
        for row in cursor:
            result.append(row)
        return result

    def getResourcesInNeed(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty = 0;"
        cursor.execute(query, (qty,))
        result = cursor.fetchone()
        return result

    #### puede ser igual a cero??
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
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress natural inner join region where region = %s;"
        cursor.execute(query, (region))
        result = cursor.fetchone()
        return result

    def getResourcesByCategoryandRegion(self, category, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress natural inner join region where category = %s and region = %s;"
        cursor.execute(query, (category, region))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplierCity(self, city):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join supplieraddress where city = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        return result

    def getResourceAtRegion(self, res_ID, region):
        cursor = self.conn.cursor()
        query = "select res_ID, category, price, qty from resources natural inner join supplies natural inner join suppliersaddress natural inner join region where res_ID = %s and region = %s;"
        cursor.execute(query, (res_ID, region))
        result = cursor.fetchone()
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        query = "select res_ID, category from resources natural inner join request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

 ## def getKeywordRequested(self, resName):
#         cursor = self.conn.cursor()
#         query = "select res_ID, category resources natural inner join transactions where resName like = %s% order by resName"
#         cursor.execute(query, (resName))
#         result = cursor.fetchone()
#         return result


 ## def getKeywordAvailable(self, resName):
#         cursor = self.conn.cursor()
#         query = "select res_ID, category resources natural inner join transactions where qty > 0 and resName like = %s% order by resName"
#         cursor.execute(query, (resName))
#         result = cursor.fetchone()
#         return result



