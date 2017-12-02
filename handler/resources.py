__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
#from dao.parts import PartsDAO


class ResourcesHandler:

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

    def build_suppliers_dict(self,row):
        result = {}
        result['supplierID'] = row[0]
        result['suppfname'] = row[1]
        result['supplname'] = row[2]
        result['suppaddress'] = row[3]
        result['supplocation'] = row[4]
        return result

    def getAllResources(self):
        #dao = ApplicantsDAO()
        resources = [(1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)]
        result_list = []
        for row in resources:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesById(self, resourceID):
        row = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            supplier = self.build_resources_dict(row)
            return jsonify(Resource = supplier)

    def searchResources(self, args):
        category = args.get("category")
        name = args.get("name")
        qty = args.get("qty")
        price = args.get("price")
        #dao = PartsDAO()
        resources_list = []
        if (len(args) == 2) and name and qty:
            resources_list = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)
        elif (len(args) == 2) and category and qty:
            resources_list = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)
        elif (len(args) == 1) and name:
            resources_list = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)
        elif (len(args) == 1) and category:
            resources_list = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)
        elif (len(args) == 2) and name and price:
            resources_list = (1,'Medication','Zyrtec','N/A','N/A','N/A','24','100','$3.99',1),(2,'Clothing','Pants','M','F','N/A','N/A','50','$0.00',2)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getSuppliersByResourceId(self, resourceID):
        #dao = PartsDAO()
        suppliers = [(1,'Juan','Del Pueblo','calle bosque','Mayaguez')]
        if not suppliers:
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = suppliers
        result_list = []
        for row in suppliers_list:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)