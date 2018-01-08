__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class applicantsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                          pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select * from transactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByApplicantsID(self, apl_ID):
        cursor = self.conn.cursor()
        query = "select trans_ID, trans_date, status, amount from transactions natural inner join applicants where apl_ID = %s;"
        cursor.execute(query, (apl_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySuppliersID(self, supp_ID):
        cursor = self.conn.cursor()
        query = "select trans_ID, trans_date, status, amount from transactions natural inner join applicants where supp_ID = %s;"
        cursor.execute(query, (supp_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        query = "select res_ID, category from resources natural inner join transactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
