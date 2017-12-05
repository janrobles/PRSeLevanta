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