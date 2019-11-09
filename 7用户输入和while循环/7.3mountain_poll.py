responses={}
polling_active=True
while polling_active:
	name=input("what is your name?")
	response=input("which mountain would you like to climb someday?")
	responses[name]=response
	repeat=input("would you let another person respond?(Y/N)")
	if repeat.upper()=="N":
		polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
	print(name+" would like to climb "+response+".")