__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
#from dao.parts import PartsDAO


class SuppliersHandler:

    def build_suppliers_dict(self,row):
        result = {}
        result['supplierID'] = row[0]
        result['suppfname'] = row[1]
        result['supplname'] = row[2]
        result['suppaddress'] = row[3]
        result['supplocation'] = row[4]
        return result

    def build_resources_dict(self,row):
        result = {}
        result['resourceID'] = row[0]
        result['category'] = row[1]
        result ['size'] = row[2]
        result ['gender'] = row [3]
        result ['battery_type']= row[4]
        result ['pack_size'] = row[5]
        result['rname'] = row[6]
        result['qty'] = row[7]
        result['price'] = row[8]
        result['supplierID'] = row[9]
        return result

    def build_accounts_dict(self,row):
        result = {}
        result['account_#'] = row[0]
        result['balance'] = row[1]
        result['supp_ID'] = row[2]
        return result


    def getAllSuppliers(self):
        suppliers = [(1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')]
        result_list = []
        for row in suppliers:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getSuppliersById(self, supp_ID):
        row = (1,'Juan','Del Pueblo','calle bosque','Mayaguez')
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            supplier = self.build_suppliers_dict(row)
            return jsonify(Supplier = supplier)

    def searchSuppliers(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        location = args.get("location")
        address = args.get("address")
        #dao = PartsDAO()
        suppliers_list = []
        if (len(args) == 2) and name and location:
            suppliers_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 2) and name and address:
            suppliers_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and location:
            suppliers_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and address:
            suppliers_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        elif (len(args) == 1) and lastname:
            suppliers_list = (1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesBySupplierId(self, supp_ID):
        #dao = PartsDAO()
        resources = [(1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1)]
        if not resources:
            return jsonify(Error="Part Not Found"), 404
        resources_list = resources
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAccountsBySupp_ID(self, supp_ID):
        #dao = PartsDAO()
        accounts = [(123456789,100,1),(234567890,500,2)]
        if not accounts:
            return jsonify(Error="Part Not Found"), 404
        accounts_list = accounts
        result_list = []
        for row in accounts_list:
            result = self.build_accounts_dict(row)
            result_list.append(result)
        return jsonify(Accounts=result_list)