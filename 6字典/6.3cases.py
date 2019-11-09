#6-4
word_dics={
	'str()':'make a number be a string',
	'int':'an int number',
	'list()':'make a list',
}

for word in word_dics.keys():
	print(word+":\n\t"+word_dics[word])
# print("str()"+":\n\t"+word_dics['str()'])
# print("int"+":\n\t"+word_dics['int'])
# print("list()"+":\n\t"+word_dics['list()'])
word_dics['range(m,n,x)']="生成步长为x的从m到n的数字序列"
for word in word_dics.keys():
	print(word+":\n\t"+word_dics[word])
print(word_dics)
print(word_dics)
#6-5
rivers={
	'changjiang':'China',
	'amazon':'brazil',
	'nile':'egypt',
}
for rive,county in rivers.items():
	print("The "+rive.title()+" River runs through "+county.title()+".")
for rive in rivers.keys():
	print(rive.title())
for county in rivers.values():
	print(county.title())

#6-6
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}
all_names=['jen','sarah','edward','phil','tom','jerry']
done_names=favorite_languages.keys()
for name in all_names:
	if name in done_names:
		print("Thank you,"+name.title()+"!")
	elif name not in done_names:
		print(name.title()+",Would you help us?")









