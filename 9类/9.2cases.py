#9-4
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print(self.restaurant_name,self.cuisine_type)
	def open_restaurant(self):
		print("The restaurant is opening.")
	def set_number_served(self,num):
		self.number_served=num
	def increment_number_served(self,incre_num):
		self.number_served+=incre_num

restaurant=Restaurant('中华大酒店','中国菜')
print(restaurant.number_served)

restaurant.increment_number_served(56)
print(restaurant.number_served)

restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(56)
print(restaurant.number_served)

restaurant.number_served=12
print(restaurant.number_served)

#9-5
class User():
	"""a person's information"""
	def __init__(self, first_name,last_name,sex,age):
		# super(User, self).__init__()
		self.first_name = first_name
		self.last_name=last_name
		self.sex=sex
		self.age=age
		self.login_attempts=0

	def describe_user(self):
		print(self.first_name.title(),self.last_name.title(),self.sex,self.age)
	def greet_user(self):
		full_name=self.first_name.title()+" "+self.last_name.title()
		print("Hello,"+full_name+".")
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0

user_1=User('Xin','yuanchang','male',28)
user_2=User('辛','元昌','男',29)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)

