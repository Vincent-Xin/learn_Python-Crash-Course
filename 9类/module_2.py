# 9-12
import module
class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin_2(module.User):
    """docstring for Admin"""
    def __init__(self,first_name,last_name,sex,age):
        super().__init__(first_name,last_name,sex,age)
        self.privileges=Privileges()