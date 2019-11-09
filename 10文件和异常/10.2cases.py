#10-3
guest_name=input("please enter your name:")
filename='guest.txt'
with open(filename,'w') as file_object:
	file_object.write(guest_name)

#10-4
print("enter 'q' to quit.")
while True:
	user_name=input("Please Enter Your Name:")

	if user_name=='q':
		break
	print("Welcome "+user_name+"!")
	filename='guest_book.txt'
	with open(filename,'a') as file_object:
		file_object.write(user_name.title()+' was here.\n') 

#10-5
print("please tell me why you like coding so much:")
print('enter q to quit.')
while True:
	reason=input()
	if reason=='q':
		break
	filename='reason.txt'
	with open(filename,'a') as file_object:
		file_object.write(reason+'\n')
