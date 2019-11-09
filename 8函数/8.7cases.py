#8-15
from printing_functions_8_15 import print_models,show_completed_models

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#8-16
import make_car_8_16

new_car=make_car_8_16.make_car('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')


from make_car_8_16 import make_car

new_car=make_car('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')


from make_car_8_16 import make_car as mc

new_car=mc('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')


import make_car_8_16 as m_8

new_car=m_8.make_car('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')


from make_car_8_16 import *

new_car=make_car('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')


#8-17函数编写指南


