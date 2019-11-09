#10-6

print("tell me two numbers and I will add them.\nenter q to quit.")
# # number_1=input("first: ")
# # number_2=input("second:")
# def add(num_1,num_2):
# 	sum_num=num_1+num_2
# 	return sum_num

# try:
# 	result=add(number_1,number_2)
# except ValueError:
# 	print('亲，这里建议你输入正确数字呢！')
# else:
# 	print(result)

# def accept_number(num):
# 	num=input('number:')
# 	try:
# 		num=int(num)
# 	except ValueError:
# 		print('亲，这里建议你输入正确数字呢！')
# 	else:
# 		return num
# flag=True
# while flag:
# 	num_1=input('number1:')
# 	if num_1=='q':
# 		break
# 	try:
# 		num_1=int(num_1)
# 	except ValueError:
# 		print('亲，这里建议你输入正确数字呢！')
# 		continue
# 	else:
# 		flag=False

# while flag==False:
# 	num_2=input('number2:')
# 	if num_2=='q':
# 		break
# 	try:
# 		num_2=int(num_2)
# 	except ValueError:
# 		print('亲，这里建议你输入正确数字呢！')
# 		continue
# 	else:
# 		flag=True
# if num_1 and num_2:
# 	result=add(num_1,num_2)
# 	print(result)

def get_nums(n):
	i=0
	nums=[]
	while i<n:
		num=input('number'+str(i+1)+':')
		if num=='q':
			break
		try:
			num=int(num)
		except ValueError:
			print('亲，这里建议你输入正确数字呢！')
			continue
		else:
			nums.append(num)
			i+=1
	return nums
def add_nums(nums):
	if(len(nums)>=2):
		num_sum=sum(nums)
		print(num_sum)

while True:
	some_nums=get_nums(4)
	if(len(some_nums)<4):
		break
	add_nums(some_nums)








