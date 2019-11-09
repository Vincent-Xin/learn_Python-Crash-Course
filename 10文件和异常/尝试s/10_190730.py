#10-6逻辑
'''循环输入整数并求和，以及退出和提醒修正输入'''
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

