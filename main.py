__author__ = 'janrobles'
from flask import Flask, jsonify, request
from handler.applicants import ApplicantsHandler
from handler.resources import ResourcesHandler
from handler.suppliers import SuppliersHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is PRSeLevanta!'

@app.route('/PRSeLevanta/applicants')
def getAllApplicants():
    if not request.args:
        return ApplicantsHandler().getAllApplicants()
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

@app.route('/PRSeLevanta/applicants/<int:applicantID>')
def getApplicantById(applicantID):
    return ApplicantsHandler().getApplicantsById(applicantID)

@app.route('/PRSeLevanta/resources/<int:resourceID>')
def getApplicantById(resourceID):
    return ResourcesHandler().getResourcesById(resourceID)

# @app.route('/PartApp/parts/<int:pid>/suppliers')
# def getSuppliersByPartId(pid):
#     return PartHandler().getSuppliersByPartId(pid)
#
@app.route('/PRSeLevanta/suppliers/<int:supplierID>')
def getSupplierById(supplierID):
    return SuppliersHandler().getSuppliersById(supplierID)

# @app.route('/PartApp/suppliers/<int:sid>/parts')
# def getPartsBySuplierId(sid):
#     return SupplierHandler().getPartsBySupplierId(sid)

if __name__ == '__main__':
    app.run()
