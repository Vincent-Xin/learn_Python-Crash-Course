#10-1
with open('learning_python.txt') as file_object:
	learning_file=file_object.read()
	print(learning_file.rstrip())
	print(file_object)

with open('learning_python.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

with open('learning_python.txt') as file_object:
	learning_list=file_object.readlines()
for line in learning_list:
	print(line.strip())

#10-2
for line in learning_list:
	line=line.replace('Python','C')
	print(line)
print(learning_list)
message="I love you"
message=message.replace('love','hate')
print(message)