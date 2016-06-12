"""A class that reads json formatted test file containing data about customers
 and prints all the customers within 100KM of Intercom Office.

Written by: Harpreet Singh
"""
import json
import math


class IntercomLunch():

	intercomLat = math.radians(53.3381985)
	intercomLon = math.radians(-6.2592576)
	earthRadius = 6371

	def calculateDistance(self, data):
		"""This function calculates the Great Circle distance between a given point and 
			the co-ordinates of the Intercom Office"""
		lat = math.radians(float(data['latitude']))
		lon = math.radians(float(data['longitude']))
		
		deltaLong = math.fabs(lon - self.intercomLon)
		
		part1 = (math.sin(lat) * math.sin(self.intercomLat))
		part2 = math.cos(lat) * math.cos(self.intercomLat) * math.cos(deltaLong)
		
		deltaRo = math.acos(part1 + part2)
		distance = self.earthRadius * deltaRo
		return distance

	def findCustomersToInvite(self, data):
		"""This function filters the list to contain the customers within 100 km 
		    sorted in ascending order of their user IDs"""
		distance = lambda d: self.calculateDistance(d) < 100
		invited = [a for a in data if distance(a)]
		inviteInOrder = sorted(invited, key=lambda x: x['user_id'])
		return inviteInOrder

	def printCustomersToInvite(self, fileName):
		"""This function reads a text file, and converts the contents into a python list 
		of dictionaries and prints the customers to be invited within 100 km radius"""
		customers = ""
		with open(fileName) as f:
		    for line in f:
		    	customers += line.replace('\n', ',') 
 		    	if 'str' in line: break
		
		c = '[' + customers[:len(customers)] + ']'

		info = self.findCustomersToInvite(json.loads(c))
		
		for i in info:
			print i['user_id'], i['name'] 

if __name__ == '__main__': 
	ob = IntercomLunch()
	fileName = 'customers.json'  # Change the filename here to use a different file
	ob.printCustomersToInvite(fileName)









