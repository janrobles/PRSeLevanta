__author__ = 'janrobles'
from flask import Flask, jsonify, request
from handler.applicants import ApplicantsHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is PRSeLevanta!'

@app.route('/PRSeLevanta/applicants')
def getAllApplicants():
    #if not request.args:
        return ApplicantsHandler().getAllApplicants()
    #else:
        #return ApplicantsHandler().searchParts(request.args)
if __name__ == '__main__':
    app.run()
