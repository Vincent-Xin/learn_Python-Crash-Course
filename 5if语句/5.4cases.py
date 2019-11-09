#5-8
user_names=['Jack','Tom','Jerry','Fiona','admin']

for user_name in user_names:
	if user_name == 'admin':
		print("Hello admin,would you like to see a status report?")
	else:
		print("Hello "+user_name+",thank you for logging in again.")

#5-9
user_names2=[]

if user_names2:
	for user_name in user_names2:
		if user_name == 'admin':
			print("Hello admin,would you like to see a status report?")
		else:
			print("Hello "+user_name+",thank you for logging in again.")
else:
	print("We need to find some users.\n")

#5-10
current_users=['Jack','Tom','Jerry','Fiona','Billy']
new_users=['TOM','Bin','Jhon','BILLY','Lucy']

current_users2=[]
for current_user in current_users:
	current_users2.append(current_user.lower())

if new_users:
	for new_user in new_users:
		if new_user.lower() in current_users2:
			print("We alrendy have this name.")
		else:
			print("You can use this name.")
else:
	print("Please enter your name.")

#5-11
numbers=list(range(1,10))

for n in numbers:
	if n == 1:
		print(str(n)+"st")
	elif n == 2:
		print(str(n)+"nd")
	elif n == 3:
		print(str(n)+"rd")
	else:
		print(str(n)+"th")



