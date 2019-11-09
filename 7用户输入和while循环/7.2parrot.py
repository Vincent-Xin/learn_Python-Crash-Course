prompt="Tell me something,and I will repeat it back to you."
prompt+="\nEnter 'quit',if you want to stop."

#7.2.2
# message=""
# while message.lower() != 'quit':
# 	message=input(prompt)
# 	if message.lower() != 'quit':
# 		print(message)

# 7.2.3	
active=True
while active:
	message=input(prompt)
	if message.lower() == 'quit':
		active = False
	else:
		print(message)
