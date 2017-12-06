__author__ = 'janrobles'
from flask import Flask
from flask import jsonify

class StatsHandler:

    def build_stats_dict(self,row):
        result = {}
        result['timeframe'] = row[0]
        result['resources in need'] = row[1]
        result['resources available'] = row[2]
        result['availability-need'] = row[3]
        return result

    def getWeeklyStats(self):
        #dao = ApplicantsDAO()
        weekly = [('Last Week',100,150,50),('Last Week',233,100,-133)]
        result_list = []
        for row in weekly:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Stats = result_list)

    def getDailyStats(self):
        #dao = ApplicantsDAO()
        daily = [('today',10,10,0),('today',15,10,-5)]
        result_list = []
        for row in daily:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Stats = result_list)


    def getRegionStats(self):
        #dao = ApplicantsDAO()
        region = [('Region: Mayaguez',130,100,30),('Region: San Juan',500,1500,1000)]
        result_list = []
        for row in region:
            result = self.build_stats_dict(row)
            result_list.append(result)
        return jsonify(Stats = result_list)