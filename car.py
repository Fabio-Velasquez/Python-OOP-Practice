class store:
	def __init__(self,city, state, country):
		self.city = city
		self.state = state
		self.country = country


class Car:
	def __init__(self,car_weight, wheels, passengers, model_number):
		self.weight = car_weight
		self.wheels = wheels
		self.passengers = passengers
		self.model_number = model_number

	
	# getter for class
	def get_weight(self):
		return self.weight
		
	def get_wheels(self):
		return self.wheels
		
	def get_passengers(self):
		return self.passengers
		
	def get_model(self):
		return self.model_number
		

		
	# setters for class
	def set_weight(self,weight):
		self.weight = weight
		
	def set_wheels(self,wheels):
		self.wheels = wheels
		
	def set_passengers(self,passengers):
		self.passengers = passengers
		
	def set_model(self, model_number):
		self.model_number = model_number
		

		

class Brand:
	number_of_cars = 0
	def __init__(self, brand, origin, num_of_cars):
		self.brand = brand
		self.origin = origin
		self.num_of_cars = num_of_cars
		self.cars = []
		
		
	def __repr__(self):
		return str(self.cars)
		
	#	getters
	def get_brand(self):
		return self.brand
		
	def get_origin(self):
		return self.origin
		
	def get_num_of_cars(self):
		return self.num_of_cars
	def get_list_of_cars(self):
	
		return self.cars
		
	
	#	setters
	def set_brand(self,brand):
		self.Brand = brand
		
	def set_origin(self, origin):
		self.origin = origin 
	
		
	def set_num_of_cars(self, num_of_cars):
		self.num_of_cars = num_of_cars
	
	# add a type of car to list of cars on the lot
	def add_car(self, car):
		if(len(self.cars) < self.num_of_cars):
			self.cars.append(car)
			Brand.number_of_cars +=1
			return True
		else:
			return False
		


#	class car
supra = Car(3500,4, 4, 103)
Corrolla = Car(3000, 4, 4, 101)
Camery = Car(3500, 4, 4, 102)
F150 = Car(5000, 4, 4, 104) 


#	class brand 
Toyota = Brand("Toyota", "Japan", 30)
Ford = Brand("Ford", "United States", 15)

Orlando = store('orlando','florida','U.S')
Toyota.add_car(Corrolla)
Toyota.add_car(Camery)


print(Toyota.__repr__())
print(Toyota.__str__())

print []
print("weight")
print(Camery.get_weight())

print(Toyota.get_brand())
print(Toyota.get_brand)


print()

print(Toyota.get_origin())

print()

print(str(Toyota.get_list_of_cars()))

print()

print(Toyota.get_num_of_cars())



#print(Toyota.get_list_of_cars())


