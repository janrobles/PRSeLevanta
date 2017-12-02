__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
#from dao.parts import PartsDAO


class ApplicantsHandler:

    def build_applicants_dict(self,row):
        result = {}
        result['applicantID'] = row[0]
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
        return jsonify(Applicants = result_list)

    def getApplicantsById(self, applincantID):
        #dao = PartsDAO()
        row = (1,'Juan','Del Pueblo','calle bosque','Mayaguez')
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            applicant = self.build_applicants_dict(row)
            return jsonify(Applicant = applicant)

    def searchApplicants(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        location = args.get("location")
        address = args.get("address")
        #dao = PartsDAO()
        applicants_list = []
        if (len(args) == 2) and name and location:
            applicants_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 2) and name and address:
            applicants_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and location:
            applicants_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and address:
            applicants_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and lastname:
            applicants_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in applicants_list:
            result = self.build_applicants_dict(row)
            result_list.append(result)
        return jsonify(Applicants=result_list)


