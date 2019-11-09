import json
# def greet_user():
# 	'''问候用户，并指出其名字'''
# 	filename='username.json'
# 	try:
# 		with open(filename) as f_obj:
# 			username=json.load(f_obj)
# 	except FileNotFoundError:
# 		username=input('What is your name?')
# 		with open(filename,'w') as f_obj:
# 			json.dump(username,f_obj)
# 			print("welcome "+username+"!")
# 	else:
# 		print("welcome back "+username+"!")


def get_stored_username():
	'''get the name if user stored it '''
	filename='username.json'
	try:
		with open(filename) as f_obj:
			username=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username=input("What is your name?")
	filename='username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user():
	username=get_stored_username()
	if username:
		print("welcome back")
	else:
		username=get_new_username()
		print('welcome!')
greet_user()