#10-11
#10-12
import json
# def get_favorite_number():
# 	filename='favorite_number.json'
# 	favorite_number=input("What is your favorite number?")
# 	with open(filename,'w') as file_object:
# 		json.dump(favorite_number,file_object)
# 	return favorite_number
# def read_number():
# 	filename='favorite_number.json'
# 	try:
# 		with open(filename,'r') as file_object:
# 			favorite_number=json.load(file_object)
# 	except FileNotFoundError:
# 		favorite_number=get_favorite_number()
	
# 	print('I know your favorite number is '+favorite_number+'.')

# read_number()

# 10-13ø∫øø∫˙∆˚˚¬¬πø∆∆µµ≤˚¬¬≥≥
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
		answer=input("Are you "+username+"?(y/n)")
		if answer.lower() == 'y':
			print("welcome back")
		else:
			username=get_new_username()
			print('Welcome!')
	else:
		username=get_new_username()
		print('welcome!')
greet_user()
