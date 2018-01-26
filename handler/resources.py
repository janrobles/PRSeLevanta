__author__ = 'janrobles'
from flask import Flask
from flask import jsonify
from dao.resources import resourcesDAO


class ResourcesHandler:

    def build_resources_dict(self,row):
        result = {}
        result['res_ID'] = row[0]
        result['category'] = row[1]
        result['price'] = row[2]
        result['qty'] = row[3]
        return result

    def build_resourcesrequested_dict(self, row):
        result = {}
        result['res_ID'] = row[0]
        result['apl_ID'] = row[1]
        result['category'] = row[2]
        result['price'] = row[3]
        result['qty'] = row[4]
        return result

    def build_request_attributes(self, req_ID,apl_ID, res_ID):
        result = {}
        result['req_ID'] = req_ID
        result['apl_ID'] = apl_ID
        result['res_ID'] = res_ID
        return result

    def build_resources_attributes(self, res_ID, category, price, qty):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        return result

    def build_clothing_attributes(self, res_ID, category, price, qty, size, gender):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['size'] = size
        result['gender'] = gender
        return result

    def build_food_attributes(self, res_ID, category, price, qty, kind):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['kind'] = kind
        return result

    def build_pgenerator_attributes(self, res_ID, category, price, qty, watts):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['watts'] = watts
        return result

    def build_batteries_attributes(self, res_ID, category, price, qty, kind):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['kind'] = kind
        return result

    def build_ice_attributes(self, res_ID, category, price, qty, size):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['size'] = size
        return result

    def build_fuel_attributes(self, res_ID, category, price, qty, kind,size):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['kind'] = kind
        result['size'] = size
        return result

    def build_medication_attributes(self, res_ID, category, price, qty, dosis):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['dosis'] = dosis
        return result

    def build_water_attributes(self, res_ID, category, price, qty, size):
        result = {}
        result['res_ID'] = res_ID
        result['category'] = category
        result['price'] = price
        result['qty'] = qty
        result['size'] = size
        return result

    def build_suppliers_dict(self,row):
        result = {}
        result['supp_ID'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        return result

    def getAllResources(self):
        dao = resourcesDAO()
        resources = dao.getAllResources()
        result_list = []
        for row in resources:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesById(self, res_ID):
        dao = resourcesDAO()
        row = dao.getResourceById(res_ID)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource = resource)

    def getResourcesAvailable(self):
        dao = resourcesDAO()
        resources = dao.getResourcesAvailable()
        result_list = []
        for row in resources:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourcesInNeed(self):
        dao = resourcesDAO()
        resources = dao.getResourcesInNeed()
        result_list = []
        for row in resources:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def searchResourcesInNeed(self, args):
        category = args.get("category")
        dao = resourcesDAO()
        resources_list = []
        if (len(args) == 1) and category:
            resources_list = dao.getResourcesInNeedByCategoryKeyword(category)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResourcesAvailable(self, args):
        category = args.get("category")
        dao = resourcesDAO()
        resources_list = []
        if (len(args) == 1) and category:
            resources_list = dao.getResourcesAvailableByCategoryKeyword(category)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResources(self, args):
        category = args.get("category")
        qty = args.get("qty")
        price = args.get("price")
        region = args.get("region")
        city =args.get("city")
        dao = resourcesDAO()
        resources_list = []
        if (len(args) == 1) and city:
            resources_list = dao.getResourcesBySupplierCity(city)
        elif (len(args) == 2) and category and qty:
            resources_list = dao.getResourcesByCategoryandQty(category,qty)
        elif (len(args) == 2) and category and region:
            resources_list = dao.getResourcesByCategoryandRegion(category,region)
        elif (len(args) == 1) and category:
            resources_list = dao.getResourcesByCategory(category)
        elif (len(args) == 1) and qty:
            resources_list = dao.getResourcesByQty(qty)
        elif (len(args) == 1)  and price:
            resources_list = dao.getResourcesByPrice(price)
        elif (len(args) == 1) and region:
            resources_list = dao.getResourcesByRegion(region)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getSuppliersByResourceId(self, res_ID):
        dao = resourcesDAO()
        suppliers = dao.getSuppliersByResourcesId(res_ID)
        if not suppliers:
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = suppliers
        result_list = []
        for row in suppliers_list:
            result = self.build_suppliers_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesRequestedByApplicantID(self, apl_ID):
        dao = resourcesDAO()
        requests = dao.getResourcesRequestedByApplicantID(apl_ID)
        if not requests:
            return jsonify(Error="Part Not Found"), 404
        requests_list = requests
        result_list = []
        for row in requests_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestedResources(self):
        dao = resourcesDAO()
        requests = dao.getRequestedResources()
        if not requests:
            return jsonify(Error="No request at the moment"), 404
        requests_list = requests
        result_list = []
        for row in requests:
            result = self.build_resourcesrequested_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

    def insertResources(self, form):
        if len(form) == 4 and form['category']=="food":
            supp_ID=form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            kind = form['kind']
            if supp_ID and category and price and qty and kind:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID,supp_ID)
                dao.insertFood(res_ID, kind)
                result = self.build_food_attributes(res_ID, category, price, qty, kind)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form) == 6 and form['category'] == 'clothing':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            size = form['size']
            gender = form['gender']
            if supp_ID and category and price and qty and size and gender:
                dao = resourcesDAO()
                res_ID = dao.insert(category,price,qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertClothing(res_ID,size,gender)
                result = self.build_clothing_attributes(res_ID,category,price,qty,size,gender)
                return jsonify(Cloth = result),201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form) ==5 and form['category']=='pgenerator':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            watts = form['watts']
            if supp_ID and category and price and qty and watts:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertPgenerator(res_ID, watts)
                result = self.build_pgenerator_attributes(res_ID, category, price, qty, watts)
                return jsonify(Power_Generators=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form)== 5 and form['category']=='batteries':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            kind = form['kind']
            if supp_ID and category and price and qty and kind:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertBatteries(res_ID, kind)
                result = self.build_batteries_attributes(res_ID, category, price, qty, kind)
                return jsonify(Batteries=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form)==5 and form['category']=='medication':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            dosis = form['dosis']
            if supp_ID and category and price and qty and dosis:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertMedication(res_ID, dosis)
                result = self.build_medication_attributes(res_ID, category, price, qty, dosis)
                return jsonify(Medication=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form)==5 and form['category']=='ice':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            size = form['size']
            if supp_ID and category and price and qty and size:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertIce(res_ID, size)
                result = self.build_ice_attributes(res_ID, category, price, qty, size)
                return jsonify(Ice=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form)==6 and form['category']=='fuel':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            kind = form['kind']
            size = form['size']
            if supp_ID and category and price and qty and kind and size:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertFuel(res_ID, kind, size)
                result = self.build_fuel_attributes(res_ID, category, price, qty, kind,size)
                return jsonify(Fuel=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        elif len(form)==5 and form['category']=='water':
            supp_ID = form['supp_ID']
            category = form['category']
            price = form['price']
            qty = form['qty']
            size = form['size']
            if supp_ID and category and price and qty and size:
                dao = resourcesDAO()
                res_ID = dao.insert(category, price, qty)
                dao.insertSupplies(res_ID, supp_ID)
                dao.insertWater(res_ID, size)
                result = self.build_water_attributes(res_ID, category, price, qty, size)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

        else:
            return jsonify(Error="Malform post request"), 400

    def updateResource(self,res_ID,form):
        dao = resourcesDAO()
        if not dao.getResourceById(res_ID):
            return jsonify(Error="Resource not found"), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malform update request"), 400
            else:
                res_ID = form['res_ID']
                category = form['category']
                price = form['price']
                qty = form['qty']
                if price and qty:
                    dao.updateResource(price, qty, res_ID)
                    result = self.build_resources_attributes(res_ID,category,price,qty)
                    return jsonify(Resource=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in updates request"), 400

    def insertRequest(self, form):
        if len(form) != 2:
            return jsonify(Error="Malform post request"), 400
        else:
            apl_ID = form['apl_ID']
            res_ID = form['res_ID']
            if apl_ID and res_ID:
                dao = resourcesDAO()
                req_ID =dao.insertRequest(apl_ID, res_ID)
                result = self.build_request_attributes(req_ID,apl_ID, res_ID)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400






