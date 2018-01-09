__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.transactions import transactionsDAO

class TransactionsHandler:

    def build_transactions_dict(self,row):
        result = {}
        result['trans_ID'] = row[0]
        result['card_num'] = row[1]
        result['acct_num'] = row[2]
        result['trans_date'] = row[3]
        result['status'] = row[4]
        result['amount'] = row[5]
        return result

    def getAllTransactions(self):
        dao = transactionsDAO()
        transactions = dao.getAllTransactions()
        result_list = []
        for row in transactions:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions = result_list)

    def getTransactionByID(self,trans_ID):
        dao = transactionsDAO()
        row = dao.getTransactionsByID(trans_ID)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            transaction = self.build_transactions_dict(row)
            return jsonify(Transaction = transaction)

    def searchTransactions(self, args):
        apl_ID = args.get("apl_ID")
        supp_ID = args.get("supp_ID")
        date = args.get("date")
        status = args.get("status")
        dao = transactionsDAO()
        transactions_list = []
        if (len(args) == 2) and apl_ID and date:
            transactions_list = dao.getTransactionsByApplicantsIDandDate(apl_ID,date)
        elif (len(args) == 2) and supp_ID and status:
            transactions_list = dao.getTransactionsBySuppliersIDandStatus(supp_ID,status)
        elif (len(args) == 2) and apl_ID and status:
            transactions_list = dao.getTransactionsByApplicantsIDandStatus(apl_ID,status)
        elif (len(args) == 2) and supp_ID and date:
            transactions_list = dao.getTransactionsBySuppliersIDandDate(supp_ID,date)
        elif (len(args) == 1) and status:
            transactions_list = dao.getTransactionsByStatus(status)
        elif (len(args) == 1) and date:
            transactions_list = dao.getTransactionsByDate(date)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionsByApplicantsID(self,apl_ID):
        dao = transactionsDAO()
        transactions = dao.getTransactionsByApplicantsID(apl_ID)
        result_list = []
        for row in transactions:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionsBySuppliersID(self,supp_ID):
        dao = transactionsDAO()
        transactions = dao.getTransactionsBySuppliersID(supp_ID)
        result_list = []
        for row in transactions:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)
