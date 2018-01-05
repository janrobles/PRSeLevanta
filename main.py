__author__ = 'janrobles,ericbarbosa,jantoro'
from flask import Flask, request, jsonify
from handler.applicants import ApplicantsHandler
from handler.resources import ResourcesHandler
from handler.suppliers import SuppliersHandler
from handler.accounts import AccountsHandler
from handler.creditcards import CreditCardsHandler
from handler.stats import StatsHandler
from handler.transactions import TransactionsHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is PRSeLevanta!'

@app.route('/PRSeLevanta/applicants')
def getAllApplicants():
    if not request.args:
        return ApplicantsHandler().getAllApplicantsInfo()
    else:
        return ApplicantsHandler().searchApplicants(request.args)

@app.route('/PRSeLevanta/resources')
def getAllResources():
     if not request.args:
        return ResourcesHandler().getAllResources()
     else:
        return ResourcesHandler().searchResources(request.args)

@app.route('/PRSeLevanta/suppliers')
def getAllSuppliers():
     if not request.args:
        return SuppliersHandler().getAllSuppliers()
     else:
        return SuppliersHandler().searchSuppliers(request.args)

@app.route('/PRSeLevanta/accounts')
def getAllAccounts():
    if not request.args:
        return AccountsHandler().getAllAccounts()
    else:
        return AccountsHandler().searchAccounts(request.args)

@app.route('/PRSeLevanta/creditcards')
def getAllCards():
    if not request.args:
        return CreditCardsHandler().getAllCards()
    else:
        return CreditCardsHandler().searchCards(request.args)
@app.route('/PRSeLevanta/applicants/<int:apl_ID>/creditcards')
def getCreditCardByApl_ID(apl_ID):
    return ApplicantsHandler().getCreditCardByApl_ID(apl_ID)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>/accounts')
def getAccountsBySupp_ID(supp_ID):
    return SuppliersHandler().getAccountsBySupp_ID(supp_ID)

@app.route('/PRSeLevanta/transactions')
def getAllTransactions():
    if not request.args:
        return TransactionsHandler().getAllTransactions()
    else:
        return TransactionsHandler().searchTransactions(request.args)

@app.route('/PRSeLevanta/transactions/<int:purchase_ID>')
def getTransactionById(purchase_ID):
    return TransactionsHandler().getTransactionByID(purchase_ID)

@app.route('/PRSeLevanta/dailystats')
def getDailyStats():
    return StatsHandler().getDailyStats()

@app.route('/PRSeLevanta/weeklystats')
def getWeeklyStats():
    return StatsHandler().getWeeklyStats()

@app.route('/PRSeLevanta/regionstats')
def getRegionStats():
    return StatsHandler().getRegionStats()

@app.route('/PRSeLevanta/applicants/<int:apl_ID>')
def getApplicantById(apl_ID):
    return ApplicantsHandler().getApplicantsById(apl_ID)

@app.route('/PRSeLevanta/accounts/<int:accountnumber>')
def getAccountsByNumber(accountnumber):
    return AccountsHandler().getAccountsByNumber(accountnumber)

@app.route('/PRSeLevanta/creditcards/<int:cardnumber>')
def getCardsByNumber(cardnumber):
    return CreditCardsHandler().getCardsByNumber(cardnumber)

@app.route('/PRSeLevanta/resources/<int:resourceID>')
def getResourcesById(resourceID):
    return ResourcesHandler().getResourcesById(resourceID)

@app.route('/PRSeLevanta/resources/<int:resourceID>/suppliers')
def getSuppliersByResourceId(resourceID):
    return ResourcesHandler().getSuppliersByResourceId(resourceID)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>')
def getSupplierById(supp_ID):
    return SuppliersHandler().getSuppliersById(supp_ID)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>/resources')
def getResourcesBySupplierId(supp_ID):
    return SuppliersHandler().getResourcesBySupplierId(supp_ID)

if __name__ == '__main__':
    app.run()
