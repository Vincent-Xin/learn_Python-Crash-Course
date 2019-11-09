#9-6
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

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,cuisine_type):
            super().__init__(restaurant_name,cuisine_type)
            self.flavors=['sugar','salt','ice']

    def show_kinds(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream_store=IceCreamStand('icelove','kinds of icecream')
ice_cream_store.show_kinds()

#9-7
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
class Admin(User):
    """docstring for Admin"""
    def __init__(self,first_name,last_name,sex,age):
        super().__init__(first_name,last_name,sex,age)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin=Admin('Li','dashen','female','50')
admin.show_privileges()

#9-8
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

class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """docstring for Admin"""
    def __init__(self,first_name,last_name,sex,age):
        super().__init__(first_name,last_name,sex,age)
        self.privileges=Privileges()
    
admin=Admin('Li','dashen','female','50')
admin.privileges.show_privileges()

#9-9
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(battery_size)+'-kwh battery.')

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size=85

    def get_range(self):
        if self.battery_size == 70:
            range=240
        elif self.battery_size ==85:
            range=270
        message="This car can go approximately "+str(range)
        message+="miles on full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

my_ele_car=ElectricCar('tesla','model s','2019')
my_ele_car.battery.get_range()
my_ele_car.battery.upgrade_battery()
my_ele_car.battery.get_range()




