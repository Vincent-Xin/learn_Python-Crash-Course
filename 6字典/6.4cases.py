# -*- coding: utf-8 -*-
#6-7
a_person={'first_name':'Vincent','last_name':'Xin','age':29,'city':'Beijing',}
b_person={'first_name':'Jack','last_name':'Ma','age':45,'city':'Hangzhou',}
c_person={'first_name':'Tony','last_name':'Ma','age':44,'city':'Shenzhen',}
people=[a_person,b_person,c_person]
for person in people:
	for value in person.values():
		print(value)

#6-8
horse={'name':'horse','type':'dog','master':'王磊'}
dog={'name':'dog','type':'cat','master':'冰儿'}
pets=[horse,dog]
for pet in pets:
	print(pet['name'].title()+"'s type is a "+pet['type']+",its master is "+
		pet['master']+".")

#6-9
favorite_places={
	'Vincent':['Beijing','Shanghai','Germany'],
	"Huang":['Germany','Shanghai','Chenzhou'],
	'Tom':["Jerry's house"]
}
for person,places in favorite_places.items():
	print("\n"+person+" like ")
	for place in places:
		print(place)

#6-10
favorite_numbers={
	'Jack':[2,3,4],
	"Tom":[7],
	'Bin':[5,10],
}
for name,numbers in favorite_numbers.items():
	if len(numbers)>1:
		print("\n"+name+"'s favorite numbers are ")
	elif len(numbers)==1:
		print("\n"+name+"'s favorite number is ")
	for number in numbers:
		print(number)
#6-11
cities={
	'Beijing':{
		'county':'China',
		'people':'2000',
		'location':'north'
	},
	"New York":{
		'county':"America",
		'people':"3000",
		'location':'west'
	},
	"Singapore":{
		'county':"Singapore",
		'people':'1500',
		'location':'south'
	}
}

for cities,city_infos in cities.items():
	print("\n"+cities+":")
	for city_info,value in city_infos.items():
		print("\t"+city_info+":"+value)

# 6-12
