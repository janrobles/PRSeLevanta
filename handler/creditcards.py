__author__ = 'janrobles'
from flask import Flask
from flask import jsonify

class CreditCardsHandler:

    def build_creditcards_dict(self,row):
        result = {}
        result['card_#'] = row[0]
        result['exp_date'] = row[1]
        result['balance'] = row[2]
        result['apl_ID'] = row[3]
        return result

    def getAllCards(self):
        #dao = ApplicantsDAO()
        cards = [(123456789,10,100,1),(234567890,5,200,2)]
        result_list = []
        for row in cards:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        return jsonify(Cards = result_list)

    def searchCards(self, args):
        exp_date = args.get("expdate")
        balance = args.get("balance")
        apl_ID = args.get("apl_ID")
        #dao = PartsDAO()
        cards_list = []
        if (len(args) == 2) and apl_ID and balance:
            cards_list = (123456789,10,100,1),(234567890,10,500,2)
        elif (len(args) == 1) and exp_date:
            cards_list = (123456789,10,100,1),(234567890,10,500,2)
        elif (len(args) == 1) and apl_ID:
            cards_list = (123456789,10,100,1),(234567890,10,500,2)
        elif (len(args) == 1) and balance:
            cards_list = (123456789,10,100,1),(234567890,10,500,2)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in cards_list:
            result = self.build_creditcards_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getCardsByNumber(self, card_number):
        row = (1234556789,10,100,1)
        if not row:
            return jsonify(Error = "Card Number Not Found"), 404
        else:
            card_number = self.build_creditcards_dict(row)
            return jsonify(Card = card_number)


