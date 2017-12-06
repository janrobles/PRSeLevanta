__author__ = 'janrobles'
from flask import Flask
from flask import jsonify

class TransactionsHandler:

    def build_transactions_dict(self,row):
        result = {}
        result['purchase_ID'] = row[0]
        result['supp_ID'] = row[1]
        result['apl_ID'] = row[2]
        result['date'] = row[3]
        result['total'] = row[4]
        result['dispatched'] = row[5]
        return result

    def getAllTransactions(self):
        #dao = ApplicantsDAO()
        transactions = [(123,1,2,30,220,'True'), (123,1,2,30,220,'False')]
        result_list = []
        for row in transactions:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions = result_list)

    def getTransactionByID(self,purchase_ID):
        row = (123,1,2,30,220,0)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            transaction = self.build_transactions_dict(row)
            return jsonify(Transaction = transaction)

    def searchTransactions(self, args):
        apl_ID = args.get("apl_ID")
        supp_ID = args.get("supp_ID")
        date = args.get("date")
        dispatched = args.get("dispatched")
        #dao = PartsDAO()
        transactions_list = []
        if (len(args) == 2) and apl_ID and supp_ID:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 2) and supp_ID and dispatched:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 1) and supp_ID:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 2) and supp_ID and date:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 1) and apl_ID:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 1) and dispatched:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        elif (len(args) == 1) and date:
            transactions_list = (123,1,2,30,220,'True'),(123,1,2,30,220,'False')
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in transactions_list:
            result = self.build_transactions_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)
