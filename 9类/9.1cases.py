# -*- coding: utf-8 -*-
#9-1 
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)
	def open_restaurant(self):
		print("The restaurant is opening.")
restaurant=Restaurant('中华大酒店','中国菜')
print(restaurant.restaurant_name,restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
restaurant_2=Restaurant('钓鱼台国宾馆','鲁菜')
restaurant_3=Restaurant('长城饭店','Chinese food')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#9-3
class User():
	"""a person's information"""
	def __init__(self, first_name,last_name,sex,age):
		# super(User, self).__init__()
		self.first_name = first_name
		self.last_name=last_name
		self.sex=sex
		self.age=age
	def describe_user(self):
		print(self.first_name.title(),self.last_name.title(),self.sex,self.age)
	def greet_user(self):
		full_name=self.first_name.title()+" "+self.last_name.title()
		print("Hello,"+full_name+".")

user_1=User('Xin','yuanchang','male',28)
user_2=User('辛','元昌','男',29)

user_1.describe_user()
user_1.greet_user()
user_2.greet_user()
user_2.describe_user()