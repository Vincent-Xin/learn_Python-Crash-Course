#9-10
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

#9-11
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