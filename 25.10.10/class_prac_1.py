#문제 1
class Car:
	def __init__(self, brand, mileage, fuel):
		self.brand = brand
		self.mileage = mileage
		self.fuel = fuel
	def drive(self, distance):
		self.mileage += distance
		return self.mileage
		
	def refuel(self, amount):
		self.fuel += amount
		return self.fuel
		
	def status(self):
		print(f"브랜드명:{self.brand},주행거리:{self.mileage},연료량:{self.fuel}")