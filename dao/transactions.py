__author__ = 'janrobles'
from config.dbconfig import pg_config
import psycopg2


class transactionsDAO:
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
        query = "select trans_ID,card_num,acct_num, trans_date, status, amount from transactions natural inner join creditcards where apl_ID = %s;"
        cursor.execute(query, (apl_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySuppliersID(self, supp_ID):
        cursor = self.conn.cursor()
        query = "select trans_ID, card_num, acct_num, trans_date, status, amount from transactions natural inner join accounts where supp_ID = %s;"
        cursor.execute(query, (supp_ID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByStatus(self,status):
        cursor = self.conn.cursor()
        query ="select * from transactions where status=%s;"
        cursor.execute(query, (status,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByApplicantsIDandDate(self, apl_ID, date):
        cursor = self.conn.cursor()
        query = "select trans_ID,card_num,acct_num,trans_date, status, amount from transactions natural inner join creditcards where apl_ID = %s and trans_date =%s;"
        cursor.execute(query, (apl_ID, date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySuppliersIDandDate(self, supp_ID, date):
        cursor = self.conn.cursor()
        query = "select trans_ID, card_num, acct_num, trans_date, status, amount from transactions natural inner join accounts where supp_ID = %s and trans_date=%s;"
        cursor.execute(query, (supp_ID,date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByDate(self,date):
        cursor = self.conn.cursor()
        query ="select * from transactions where trans_date=%s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByApplicantsIDandStatus(self, apl_ID, status):
        cursor = self.conn.cursor()
        query = "select trans_ID,card_num,acct_num,trans_date, status, amount from transactions natural inner join creditcards where apl_ID = %s and status=%s;"
        cursor.execute(query, (apl_ID,status))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySuppliersIDandStatus(self, supp_ID, status):
        cursor = self.conn.cursor()
        query = "select trans_ID, card_num, acct_num, trans_date, status, amount from transactions natural inner join accounts where supp_ID = %s and status=%s;"
        cursor.execute(query, (supp_ID, status))
        result = []
        for row in cursor:
            result.append(row)
        return result

