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

    def getAllSuppliers(self):
        suppliers = [(1,'Juan','Del Pueblo','calle bosque','Mayaguez'),(2,'Jan','Robles','calle bosque','Bayamon')]
        result_list = []
        for row in suppliers:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getSuppliersById(self, supplierID):
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