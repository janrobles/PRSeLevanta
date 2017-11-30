__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
#from dao.parts import PartsDAO


class ApplicantsHandler:

    def build_applicants_dict(self,row):
        result = {}
        result['applicantsID'] = row[0]
        result['appfname'] = row[1]
        result['applname'] = row[2]
        result['appaddress'] = row[3]
        result['applocation'] = row[4]
        return result

    def getAllApplicants(self):
        #dao = ApplicantsDAO()
        applicants = [(1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')]
        result_list = []
        for row in applicants:
            result = self.build_applicants_dict(row)
            result_list.append(result)
        return jsonify(result_list)
