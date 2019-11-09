#6-1
a_person={
	'first_name':'Vincent',
	'last_name':'Xin',
	'age':29,
	'city':'Beijing',
}

print(a_person['last_name'],a_person['first_name'],a_person['age'],a_person['city'])

#6-2
favorite_numbers={
	'Jack':2,
	"Tom":3,
	'Bin':5,
}
print("Jack's favorite number is "+str(favorite_numbers['Jack']))
print("Tom likes number "+str(favorite_numbers['Tom'])+" most.")

#6-3
word_dics={
	'str()':'make a number be a string',
	'int':'a int number',
	'list()':'make a list',
}
print("str()"+":\n\t"+word_dics['str()'])
print("int"+":\n\t"+word_dics['int'])
print("list()"+":\n\t"+word_dics['list()'])