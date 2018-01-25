__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.suppliers import suppliersDAO


class SuppliersHandler:

    def build_suppliers_dict(self,row):
        result = {}
        result['supp_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        return result

    def build_suppliers_attributes(self, supp_ID,first_name,last_name,street,urb_conde,num,city,state,zip,gps_local):
        result = {}
        result['supp_ID'] = supp_ID
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['street'] = street
        result['urb_conde'] = urb_conde
        result['num']= num
        result['city'] = city
        result['state']=state
        result['zip']=zip
        result['gps_local']=gps_local
        return result

    def build_resources_dict(self,row):
        result = {}
        result['res_ID'] = row[0]
        result['category'] = row[1]
        result['price'] = row[2]
        result['qty'] = row[3]
        return result

    def build_accounts_dict(self,row):
        result = {}
        result['supp_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['account_num'] = row[3]
        result['balance'] = row[4]
        return result

    def build_info_dict(self, row):
        result = {}
        result['supp_ID'] = row[0]
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


    def getAllSuppliersInfo(self):
        dao = suppliersDAO()
        suppliers = dao.getAllSuppliersInfo()
        result_list = []
        for row in suppliers:
            result = self.build_info_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getSuppliersById(self, supp_ID):
        dao = suppliersDAO()
        row = dao.getSuppliersById(supp_ID)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            supplier = self.build_suppliers_dict(row)
            return jsonify(Supplier = supplier)

    def searchSuppliers(self, args):
        name = args.get("first_name")
        lastname = args.get("last_name")
        location = args.get("location")
        region = args.get("address")
        dao = suppliersDAO()
        suppliers_list = []
        if (len(args) == 2) and name and location:
            suppliers_list = dao.getSuppliersByNameAndLocation(name,location)
        elif (len(args) == 2) and name and region:
            suppliers_list = dao.getSuppliersByNameAndRegion(name,region)
        elif (len(args) == 1) and location:
            suppliers_list = dao.getSuppliersByLocation(location)
        elif (len(args) == 1) and region:
            suppliers_list = dao.getSuppliersByRegion(region)
        elif (len(args) == 2) and name and lastname:
            suppliers_list = dao.getSuppliersByNameAndLastname(name,lastname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesBySupplierId(self, supp_ID):
        dao = suppliersDAO()
        resources = dao.getResourcesBySuppliersID(supp_ID)
        if not resources:
            return jsonify(Error="Part Not Found"), 404
        resources_list = resources
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAccountsBySupp_ID(self, supp_ID):
        dao = suppliersDAO()
        accounts = dao.getAccountsBySuppliersID(supp_ID)
        if not accounts:
            return jsonify(Error="Accounts Not Found"), 404
        accounts_list = accounts
        result_list = []
        for row in accounts_list:
            result = self.build_accounts_dict(row)
            result_list.append(result)
        return jsonify(Accounts=result_list)

    def getSuppliersByResourceCategory(self, category):
        dao = suppliersDAO()
        suppliers = dao.getSuppliersByResourceCategory(category)
        if not suppliers:
            return jsonify(Error="Suppliers Not Found"), 404
        suppliers_list = suppliers
        result_list = []
        for row in suppliers_list:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertSuppliers(self, form):
        if len(form) != 9:
            return jsonify(Error = "Malform post request"),400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            street = form['street']
            urb_conde = form['urb_conde']
            num = form['num']
            city = form['city']
            state = form ['state']
            zip = form['zip']
            gps_local = form['gps_local']
            if first_name and last_name and street and urb_conde and num and city and state and zip and gps_local:
                dao = suppliersDAO()
                supp_ID = dao.insert(first_name,last_name)
                dao.insertAddress(supp_ID,street,urb_conde,num,city,state,zip,gps_local)
                result = self.build_suppliers_attributes(supp_ID,first_name,last_name, street,urb_conde,num,city,state,zip,gps_local)
                return jsonify(Supplier = result),201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400