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
        resources = dao.getResourcesAvailable()
        result_list = []
        for row in resources:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

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
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Requests = result_list)

