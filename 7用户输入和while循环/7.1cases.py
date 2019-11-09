#7-1
car_type=input("What kind of car type do you want? ")
print("Let me see if I can find you a "+car_type+".")

#7-2
person_count=input("How many people do have meal? ")
if int(person_count)>8:
	print("Sorry,there is no more free table.")
else:
	print("There is just a free table.")

#7-3
a_number=input("Please enter a number as you want:")
a_number=int(a_number)
if a_number and a_number%10 == 0:
	print("The number you enter is just times of ten.")
else:
	print("The number you enter is not times of ten.")

