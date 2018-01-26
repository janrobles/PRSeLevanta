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

    def insert(self, card_num, res_ID, trans_date, status):
        rid = res_ID
        cursor = self.conn.cursor()
        query = "insert into Transactions(card_num,acct_num,trans_date,status,amount) values (%s,(select acct_num from Accounts where supp_ID=(select supp_ID from Resources natural inner join Supplies where res_ID=%s)),%s,%s,(select price from Resources where res_ID=%s))returning trans_ID;"
        cursor.execute(query, (card_num,res_ID,trans_date,status,rid))
        trans_ID = cursor.fetchone()[0]
        self.conn.commit()
        return trans_ID

    def insertPurchase(self, res_ID, trans_ID):
        rid = res_ID
        cursor = self.conn.cursor()
        query = "insert into Purchase(res_ID,trans_ID,pprice) values (%s,%s,(select price from Resources where res_ID=%s));"
        cursor.execute(query, (res_ID,trans_ID,rid))
        self.conn.commit()

    def insertFulfill(self, trans_ID, res_ID):
        cursor = self.conn.cursor()
        query = "insert into Fulfill(trans_ID, supp_ID) values (%s,(select supp_ID from Resources natural inner join Supplies where res_ID=%s));"
        cursor.execute(query, (trans_ID, res_ID))
        self.conn.commit()

    def insertOwns(self, trans_ID, res_ID):
        cursor = self.conn.cursor()
        query = "insert into Owns (trans_ID,apl_ID) values (%s,(select apl_ID from Resources natural inner join Request where res_ID =%s));"
        cursor.execute(query, (trans_ID,res_ID))
        self.conn.commit()

    def updateTransaction(self, status, trans_ID):
        cursor = self.conn.cursor()
        query = "update Transactions set status=%s where trans_ID=%s;"
        cursor.execute(query, (status, trans_ID))
        self.conn.commit()

