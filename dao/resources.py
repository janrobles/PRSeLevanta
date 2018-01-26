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

    def insert(self, category, price, qty):
        cursor = self.conn.cursor()
        query = "insert into Resources(category, price, qty) values (%s, %s, %s) returning res_ID"
        cursor.execute(query,(category, price, qty))
        res_ID = cursor.fetchone()[0]
        self.conn.commit
        return res_ID

    def insertFood(self, res_ID, kind):
        cursor = self.conn.cursor()
        query = "insert into Food(res_ID, kind) values (%s, %s);"
        cursor.execute(query,(res_ID, kind))
        self.conn.commit

    def insertClothing(self, res_ID, size, gender):
        cursor = self.conn.cursor()
        query = "insert into Clothing(res_ID, size, gender) values (%s,%s,%s);"
        cursor.execute(query,(res_ID, size, gender))
        self.conn.commit

    def insertSupplies(self, res_ID, supp_ID):
        cursor = self.conn.cursor()
        query = "insert into Supplies(res_ID,supp_ID) values (%s,%s);"
        cursor.execute(query,(res_ID,supp_ID))
        self.conn.commit

    def insertPgenerator(self, res_ID, watts):
        cursor = self.conn.cursor()
        query = "insert into PowerGenerator(ress_ID,watts) values (%s,%s);"
        cursor.execute(query,(res_ID,watts))
        self.conn.commit

    def insertBatteries(self, res_ID, kind):
        cursor = self.conn.cursor()
        query = "insert into Batteries(ress_ID,kind) values (%s,%s);"
        cursor.execute(query, (res_ID, kind))
        self.conn.commit

    def insertMedication(self, res_ID, dosis):
        cursor = self.conn.cursor()
        query = "insert into Medication(ress_ID,dosis) values (%s,%s);"
        cursor.execute(query, (res_ID, dosis))
        self.conn.commit

    def insertIce(self, res_ID, size):
        cursor = self.conn.cursor()
        query = "insert into Ice(res_ID,size) values (%s,%s);"
        cursor.execute(query, (res_ID, size))
        self.conn.commit

    def insertFuel(self, res_ID, kind, size):
        cursor = self.conn.cursor()
        query = "insert into Fuel(res_ID,kind,size) values (%s,%s,%s);"
        cursor.execute(query, (res_ID, kind,size))
        self.conn.commit

    def insertWater(self, res_ID, size):
        cursor = self.conn.cursor()
        query = "insert into Watwe(res_ID,size) values (%s,%s);"
        cursor.execute(query, (res_ID, size))
        self.conn.commit

    def updateResource(self, price, qty, res_ID):
        cursor = self.conn.cursor()
        query = "update Resources set price=%s, qty=%s where res_ID=%s;"
        cursor.execute(query, (price, qty, res_ID))
        self.conn.commit()

    def insertRequest(self, apl_ID, res_ID):
        cursor = self.conn.cursor()
        query = "insert into Request(apl_ID, res_ID) values (%s, %s);"
        cursor.execute(query, (apl_ID, res_ID))
        self.conn.commit







