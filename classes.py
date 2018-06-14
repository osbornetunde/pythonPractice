# class Dog():
# 	"""A simple attempt to model a dog"""

# 	def __init__(self, name, age):
# 		"""Initialize name and age attributes."""
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		"""Simulate a dog sitting in response to a command."""
# 		print(self.name.title() + " is now sitting.")

# 	def roll_over(self):
# 		"""simulate rolling over in response to a command."""
# 		print(self.name.title() + " rolled over!")

# dog = Dog('willie', 6)

# # print("My dog's name is " + dog.name.title() + ".")
# # print("My dog is " + str(dog.age) + " years old.")

# dog.sit()
# dog.roll_over()



"""Exercise 1/2"""

class Restaurant():
	def __init__(self,name,types):
		self.restaurant_name = name
		self.cuisine_type = types

	def describe_restaurant(self):
		print("The name of the restaurant is :", self.restaurant_name.title())
		print("We offer the " + self.cuisine_type + " type of cuisine")

	def open_restaurant(self):
		print(self.restaurant_name, " is opened")


restaurant = Restaurant('dovers', 'spanish')
mamaput = Restaurant('buka', 'Naija')

restaurant.describe_restaurant()
#restaurant.open_restaurant()
mamaput.describe_restaurant()


"""Exercise 3"""
# class User():
# 	def __init__(self, f_name, l_name, age):
# 		self.first_name = f_name
# 		self.last_name = l_name
# 		self.age = age

# 	def describe_user(self):
# 		print("My name is  {}  {}  , i am  {} years old.".format(self.first_name, self.last_name, self.age))


# 	def greet_user(self):
# 		print("You are welcome ",self.first_name)


# user = User('Tunde', 'Osborne', '20')
# user.describe_user()
# user.greet_user()


class Car():
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()

	def read_odometer(self):
		"""print a statement showing the car's milaege."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")


	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		self.odometer_reading = mileage

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class"""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())




# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

