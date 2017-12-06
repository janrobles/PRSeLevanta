__author__ = 'janrobles'
from flask import Flask
from flask import jsonify

class AccountsHandler:

    def build_accounts_dict(self,row):
        result = {}
        result['account_#'] = row[0]
        result['balance'] = row[1]
        result['supp_ID'] = row[2]
        return result

    def getAllAccounts(self):
        #dao = ApplicantsDAO()
        accounts = [(123456789,100,1),(234567890,500,2)]
        result_list = []
        for row in accounts:
            result = self.build_accounts_dict(row)
            result_list.append(result)
        return jsonify(Accounts = result_list)

    def searchAccounts(self, args):
        balance = args.get("balance")
        suppID = args.get("suppID")
        #dao = PartsDAO()
        accounts_list = []
        if (len(args) == 2) and suppID and balance:
            accounts_list = (123456789,100,1),(234567890,500,2)
        elif (len(args) == 1) and suppID:
            accounts_list = (123456789,100,1),(234567890,500,2)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in accounts_list:
            result = self.build_accounts_dict(row)
            result_list.append(result)
        return jsonify(Accounts=result_list)

    def getAccountsByNumber(self, accountnumber):
        row = (1234556789,100,1)
        if not row:
            return jsonify(Error = "Account Number Not Found"), 404
        else:
            accountnumber = self.build_accounts_dict(row)
            return jsonify(Account = accountnumber)


