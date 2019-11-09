# def get_formatted_name(first_name,last_name):
# 	full_name=first_name+" "+last_name
# 	return full_name.title()

# while True:
# 	f_name=input("First name:")
# 	if f_name=='q':
# 		break
	
# 	l_name=input("Last name:")
# 	if l_name=='q':
# 		break
	
# 	formatted_name=get_formatted_name(f_name,l_name)
# 	print("\nHello,"+formatted_name+".")


def get_formatted_name():
	while True:
		first_name=input("First name:")
		if first_name=='q':
			break
		
		last_name=input("Last name:")
		if last_name=='q':
			break
		
		full_name=first_name+" "+last_name
		
		formatted_name=full_name.title()
		print("\nHello,"+formatted_name+".")

get_formatted_name()

