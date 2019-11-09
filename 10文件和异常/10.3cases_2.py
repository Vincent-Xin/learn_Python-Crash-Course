#10-8
# with open('cats.txt','w') as f_obj:
# 	f_obj.write('cat_1\ncat_2\ncat_3')
# with open('dogs.txt','w') as f_obj:
# 	f_obj.write('dog_1\ndog_2\ndog_3')
# with open('cats.txt','r') as f_obj:
# 	for line in f_obj:
# 		print(line.strip())
# with open('dogs.txt','r') as f_obj:
# 	for line in f_obj:
# 		print(line.strip())
# try:
# 	with open('cats.txt','r') as f_obj:
# 		for line in f_obj:
# 			print(line.strip())
# except FileNotFoundError:
# 	print('not cats')
# try:
# 	with open('dogs.txt','r') as f_obj:
# 		for line in f_obj:
# 			print(line.strip())
# except FileNotFoundError:
# 	print('not dogs')

#10-9
#10-10
with open('a_book.txt') as f_obj:
	contents=f_obj.read()
	words=contents.split()
	word_number=len(words)
	row_number=words.count('the')
	all_row_number=words.count('The')
	print(str(word_number)+'\n'+str(row_number)+'\n'+str(all_row_number))