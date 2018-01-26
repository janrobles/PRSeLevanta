__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.applicants import applicantsDAO

class CreditCardsHandler:

    # def build_creditcards_dict(self,row):
    #     result = {}
    #     result['card_#'] = row[0]
    #     result['exp_date'] = row[1]
    #     result['balance'] = row[2]
    #     result['apl_ID'] = row[3]
    #     return result

    def build_creditcards_attributes(self, card_num, apl_ID, exp_date, balance):
        result={}
        result['card_num']=card_num
        result['apl_ID']=apl_ID
        result['exp_date']=exp_date
        result['balance']=balance
        return balance

    # def getAllCards(self):
    #     #dao = ApplicantsDAO()
    #     cards = [(123456789,10,100,1),(234567890,5,200,2)]
    #     result_list = []
    #     for row in cards:
    #         result = self.build_creditcards_dict(row)
    #         result_list.append(result)
    #     return jsonify(Cards = result_list)
    #
    # def searchCards(self, args):
    #     exp_date = args.get("expdate")
    #     balance = args.get("balance")
    #     apl_ID = args.get("apl_ID")
    #     #dao = PartsDAO()
    #     cards_list = []
    #     if (len(args) == 2) and apl_ID and balance:
    #         cards_list = (123456789,10,100,1),(234567890,10,500,2)
    #     elif (len(args) == 1) and exp_date:
    #         cards_list = (123456789,10,100,1),(234567890,10,500,2)
    #     elif (len(args) == 1) and apl_ID:
    #         cards_list = (123456789,10,100,1),(234567890,10,500,2)
    #     elif (len(args) == 1) and balance:
    #         cards_list = (123456789,10,100,1),(234567890,10,500,2)
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in cards_list:
    #         result = self.build_creditcards_dict(row)
    #         result_list.append(result)
    #     return jsonify(Cards=result_list)
    #
    # def getCardsByNumber(self, card_number):
    #     row = (1234556789,10,100,1)
    #     if not row:
    #         return jsonify(Error = "Card Number Not Found"), 404
    #     else:
    #         card_number = self.build_creditcards_dict(row)
    #         return jsonify(Card = card_number)

    def insertCreditCard(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malform post request"),400
        else:
            card_num = form['card_num']
            apl_ID = form['apl_ID']
            exp_date = form['exp_date']
            balance = form['balance']
            if card_num and apl_ID and exp_date and balance:
                dao = applicantsDAO()
                dao.insertCreditCard(card_num,apl_ID,exp_date,balance)
                result = self.build_creditcards_attributes(card_num,apl_ID,exp_date, balance)
                return jsonify(Credit_Cards = result),201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCreditCards(self,card_num,form):
        dao = applicantsDAO()
        if not dao.getAccountByCardNum(card_num):
            return jsonify(Error = "Account not found"), 404
        else:
            if len(form)!=4:
                return jsonify(Error = "Malform update request"),400
            else:
                card_num=form['card_num']
                apl_ID=form['apl_ID']
                exp_date = form['exp_date']
                balance = form['balance']
                if balance and exp_date and apl_ID and card_num:
                    dao.updateCreditCard(exp_date,balance,card_num)
                    result = self.build_creditcards_attributes(card_num,apl_ID,exp_date,balance)
                    return jsonify (Credit_Card = result),200
                else:
                    return jsonify(Error = "Unexpected attributes in updates request"), 400






