__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class applicantsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s passwd=%s" % (pg_config['prselevantadb'],
                                                            pg_config['boricuaadmin'],
                                                            pg_config['icom5016'])
        self.conn = psycopg2._connect(connection_url)

    def getAllApplicants(self):
        cursor = self.conn.cursor()
        query = "select * from applicants;"
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
        query = "select * from applicants where city = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        return result

    def getApplicantByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from applicants where region = %s;"
        cursor.execute(query, (region,))
        result = cursor.fetchone()
        return result




######-----------------------------------------------------------------------##################
    def getPartsByColor(self, color):
        cursor = self.conn.cursor()
        query = "select * from parts where pcolor = %s;"
        cursor.execute(query, (color,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByMaterial(self, material):
        cursor = self.conn.cursor()
        query = "select * from parts where pmaterial = %s;"
        cursor.execute(query, (material,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByColorAndMaterial(self, color, material):
        cursor = self.conn.cursor()
        query = "select * from parts where pmaterial = %s and pcolor = %s;"
        cursor.execute(query, (material, color))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByPartId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from parts natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
