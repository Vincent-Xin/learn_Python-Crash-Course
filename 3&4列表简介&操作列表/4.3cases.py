#4-3数到20
for value in range(1,21):
	print(value)

#4-4一百万
#for value in range(1,1000001):
#	print(value)

#4-5
numbers1=list(range(1,1000001))
print(min(numbers1))
print(max(numbers1))
print(sum(numbers1))

#4-6
odd_numbers=list(range(1,20,2))
for value in odd_numbers:
	print(value)

#4-7
tri_numbers=list(range(3,31,3))
for value in tri_numbers:
	print(value)

#4-8
Lifang_numbers=[]
for x in range(1,11):
	Lifang_number=x**3
	Lifang_numbers.append(Lifang_number)
for value in Lifang_numbers:
	print(value)

#4-9
Lifang_numbers2=[value**3 for value in range(1,11)]
for value in Lifang_numbers2:
	print(value)
