__author__ = 'janrobles,ericbarbosa,jantoro'
from flask import Flask, request, jsonify,render_template
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
    return render_template('home.html')

#### Routes of applicants ####
@app.route('/PRSeLevanta/applicants', methods=['GET','POST'])
def getAllApplicants():
    if request.method == 'POST':
        ApplicantsHandler().insertApplicants(request.form)
        return render_template('')
    else:
        if not request.args:
            return ApplicantsHandler().getAllApplicantsInfo()
        else:
            return ApplicantsHandler().searchApplicants(request.args)

# @app.route('/PRSeLevanta/applicants/<first_name>', methods=['GET','POST'])
# def getAllApplicants():
#     if request.method == 'POST':
#          ApplicantsHandler().insertApplicants(request.form)
#
#     else:
#         if not request.args:
#             return ApplicantsHandler().getAllApplicantsInfo()
#         else:
#             return ApplicantsHandler().searchApplicants(request.args)

@app.route('/PRSeLevanta/applicants/<int:apl_ID>')
def getApplicantById(apl_ID):
    return ApplicantsHandler().getApplicantsById(apl_ID)

@app.route('/PRSeLevanta/applicants/<int:apl_ID>/creditcards', methods =['GET','POST'])
def getCreditCardByApl_ID(apl_ID):
    return ApplicantsHandler().getCreditCardsByApl_ID(apl_ID)

@app.route('/PRSeLevanta/ApplicantSignUp')
def ApplicantForm():
    return render_template('ApplicantSignUp.html')


##### Routes of Suppliers  #####
@app.route('/PRSeLevanta/suppliers', methods=['GET','POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SuppliersHandler().insertSuppliers(request.form)
    else:
        if not request.args:
            return SuppliersHandler().getAllSuppliersInfo()
        else:
            return SuppliersHandler().searchSuppliers(request.args)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>')
def getSupplierById(supp_ID):
    return SuppliersHandler().getSuppliersById(supp_ID)

@app.route('/PRSeLevanta/resources/<int:resourceID>/suppliers')
def getSuppliersByResourceId(resourceID):
    return ResourcesHandler().getSuppliersByResourceId(resourceID)

@app.route('/PRSeLevanta/resources/<category>/suppliers')
def getSuppliersByResourceCategory(category):
    return SuppliersHandler().getSuppliersByResourceCategory(category)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>/accounts', methods=['GET','POST'])
def getAccountsBySupp_ID(supp_ID):
    if request.method == 'POST':
        return AccountsHandler.insertAccount(supp_ID,request.form)
    else:
        return SuppliersHandler().getAccountsBySupp_ID(supp_ID)

@app.route('/PRSeLevanta/SupplierSignUp')
def SupplierForm():
    return render_template('SupplierSignUp.html')


#### Routes of Resources ####
@app.route('/PRSeLevanta/resources' , methods=['GET','POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourcesHandler().insertResources(request.form)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)

@app.route('/PRSeLevanta/resources/<int:res_ID>', methods = ['GET','PUT'])
def getResourcesById(res_ID):
    if request.method == 'PUT':
        return ResourcesHandler().updateResource(res_ID,request.form)
    else:
        return ResourcesHandler().getResourcesById(res_ID)

@app.route('/PRSeLevanta/resourcesavailable')
def getResourcesAvailable():
    if not request.args:
        return ResourcesHandler().getResourcesAvailable()
    else:
        return ResourcesHandler().searchResourcesAvailable(request.args)

@app.route('/PRSeLevanta/resourcesinneed')
def getResourcesInNeed():
    if not request.args:
        return ResourcesHandler().getResourcesInNeed()
    else:
        return ResourcesHandler().searchResourcesInNeed(request.args)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>/resources')
def getResourcesBySupplierId(supp_ID):
    return SuppliersHandler().getResourcesBySupplierId(supp_ID)

@app.route('/PRSeLevanta/request' , methods=['GET','POST'])
def getRequestedResources():
    if request.method=='POST':
        return ResourcesHandler().insertRequest(request.form)
    else:
        return ResourcesHandler().getRequestedResources()

@app.route('/PRSeLevanta/applicants/<int:apl_ID>/requested')
def getResourcesRequestedByApplicantsId(apl_ID):
    return ResourcesHandler().getResourcesRequestedByApplicantID(apl_ID)


#### Routes of Transactions ####
@app.route('/PRSeLevanta/transactions', methods=['GET','POST'])
def getAllTransactions():
    if request.method == 'POST':
        return TransactionsHandler().insertTransaction(request.form)
    else:
        if not request.args:
            return TransactionsHandler().getAllTransactions()
        else:
            return TransactionsHandler().searchTransactions(request.args)

@app.route('/PRSeLevanta/transactions/<int:trans_ID>',methods=['GET','PUT'])
def getTransactionById(trans_ID):
    if request.method == 'PUT':
        return TransactionsHandler().updateTransaction(trans_ID, request.form)
    else:
        return TransactionsHandler().getTransactionByID(trans_ID)

@app.route('/PRSeLevanta/applicants/<int:apl_ID>/transactions')
def getTransactionByApplicantsId(apl_ID):
    return TransactionsHandler().getTransactionsByApplicantsID(apl_ID)

@app.route('/PRSeLevanta/suppliers/<int:supp_ID>/transactions')
def getTransactionBySuppliersId(supp_ID):
    return TransactionsHandler().getTransactionsBySuppliersID(supp_ID)


#### Routes of Stats ####
@app.route('/PRSeLevanta/dailystats')
def getDailyStats():
    return StatsHandler().getDailyStats()

@app.route('/PRSeLevanta/weeklystats')
def getWeeklyStats():
    return StatsHandler().getWeeklyStats()

@app.route('/PRSeLevanta/regionstats')
def getRegionStats():
    return StatsHandler().getRegionStats()


if __name__ == '__main__':
    app.run()
