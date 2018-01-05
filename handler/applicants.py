__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.applicants import applicantsDAO


class ApplicantsHandler:

    def build_applicants_dict(self,row):
        result = {}
        result['apl_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        return result

    def build_creditcards_dict(self,row):
        result = {}

        result['apl_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['card_num'] = row[3]
        result['exp_date'] = row[4]
        result['balance'] = row[5]
        return result

    def build_applicantsaddress_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['apl_ID'] = row[1]
        result['rid'] = row[2]
        result['street'] = row[3]
        result['urb_conde']= row[4]
        result['num'] = row[5]
        result['city'] = row[6]
        result['state'] = row[7]
        result['zip'] = row[8]
        result['gps_local'] = row[9]
        return result

    def build_info_dict(self, row):
        result = {}
        result['apl_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['street'] = row[3]
        result['urb_conde'] = row[4]
        result['num'] = row[5]
        result['city'] = row[6]
        result['state'] = row[7]
        result['zip'] = row[8]
        result['region'] = row[9]
        result['gps_local'] = row[10]
        return result

    def getAllApplicants(self):
        dao = applicantsDAO()
        applicants = dao.getAllApplicants()
        result_list = []
        for row in applicants:
            result = self.build_applicants_dict(row)
            result_list.append(result)
        return jsonify(Applicants = result_list)

    def getApplicantsAddress(self):
        dao = applicantsDAO()
        addresses = dao.getAllApplicantsAddress()
        if not addresses:
            return jsonify(Error="Part Not Found"), 404
        addresses_list = addresses
        result_list = []
        for row in addresses_list:
            result = self.build_applicantsaddress_dict(row)
            result_list.append(result)
        return jsonify(Addresses=result_list)

    def getAllApplicantsInfo(self):
        dao = applicantsDAO()
        info = dao.getAllApplicantsInfo()
        if not info:
            return jsonify(Error="Part Not Found"), 404
        info_list = info
        result_list = []
        for row in info_list:
            result = self.build_info_dict(row)
            result_list.append(result)
        return jsonify(ApplicantsInfo=result_list)

    def getApplicantsById(self, apl_ID):
        dao = applicantsDAO()
        row = dao.getApplicantById(apl_ID)
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
        dao = applicantsDAO()
        applicants_list = []
        if (len(args) == 2) and name and location:
            applicants_list = dao.getApplicantsByNameAndLocation(name, location)
        elif (len(args) == 2) and name and address:
            applicants_list = dao.getApplicantsByNameAndAddress(name, address)
        elif (len(args) == 1) and location:
            applicants_list = dao.getApplicantsByLocation(location)
        elif (len(args) == 1) and address:
            applicants_list = dao.getApplicantsByAddress(address)
        elif (len(args) == 1) and lastname:
            applicants_list = dao.getApplicantsByLastname(lastname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in applicants_list:
            result = self.build_applicants_dict(row)
            result_list.append(result)
        return jsonify(Applicants=result_list)


    def getCreditCardByApl_ID(self, apl_ID):
        dao = applicantsDAO()
        row = dao.getCreditCardsByApplicantsID(apl_ID)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            applicant = self.build_creditcards_dict(row)
            return jsonify(CreditCards = applicant)

