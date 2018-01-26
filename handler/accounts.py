__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.suppliers import suppliersDAO

class AccountsHandler:

    # def build_accounts_dict(self,row):
    #     result = {}
    #     result['account_#'] = row[0]
    #     result['balance'] = row[1]
    #     result['supp_ID'] = row[2]
    #     return result

    def build_accounts_attributes(self, acct_num, supp_ID, balance):
        result = {}
        result['acct_num'] = acct_num
        result['supp_ID'] = supp_ID
        result['balance'] = balance
        return result

    # def getAllAccounts(self):
    #     #dao = ApplicantsDAO()
    #     accounts = [(123456789,100,1),(234567890,500,2)]
    #     result_list = []
    #     for row in accounts:
    #         result = self.build_accounts_dict(row)
    #         result_list.append(result)
    #     return jsonify(Accounts = result_list)
    #
    # def searchAccounts(self, args):
    #     balance = args.get("balance")
    #     suppID = args.get("suppID")
    #     #dao = PartsDAO()
    #     accounts_list = []
    #     if (len(args) == 2) and suppID and balance:
    #         accounts_list = (123456789,100,1),(234567890,500,2)
    #     elif (len(args) == 1) and suppID:
    #         accounts_list = (123456789,100,1),(234567890,500,2)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in accounts_list:
    #         result = self.build_accounts_dict(row)
    #         result_list.append(result)
    #     return jsonify(Accounts=result_list)
    #
    # def getAccountsByNumber(self, accountnumber):
    #     row = (1234556789,100,1)
    #     if not row:
    #         return jsonify(Error = "Account Number Not Found"), 404
    #     else:
    #         accountnumber = self.build_accounts_dict(row)
    #         return jsonify(Account = accountnumber)

    def insertAccount(self,supp_ID,form):
        if len(form) != 2:
            return jsonify(Error = "Malform post request"),400
        else:
            acct_num = form['acct_num']
            balance = form['balance']
            if acct_num and balance:
                dao = suppliersDAO()
                dao.insertAccount(acct_num,supp_ID,balance)
                result = self.build_accounts_attributes(acct_num,supp_ID,balance)
                return jsonify(Account = result),201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateAccount(self,acct_num,form):
        dao = suppliersDAO()
        if not dao.getAccountByAcctNum(acct_num):
            return jsonify(Error = "Account not found"), 404
        else:
            if len(form)!=2:
                return jsonify(Error = "Malform update request"),400
            else:
                balance=form['balance']
                supp_ID=form['supp_ID']
                if balance and supp_ID:
                    dao.updateAccount(acct_num,balance)
                    result = self.build_accounts_attributes(acct_num,supp_ID,balance)
                    return jsonify (Accounts = result),200
                else:
                    return jsonify(Error = "Unexpected attributes in updates request"), 400





