import math

def get_prime_numbers(M):
	print('1~'+str(M)+'的质数有：')
	prime_numbers=[2,]
	for m in range(3,M+1,2):
		if m==3:
			prime_numbers.append(m)
		else:
			for n in range(3,int(math.sqrt(m))+1,2):
				if m%n == 0:
					break
			else:
				prime_numbers.append(m)
				
	print(prime_numbers)
	print(len(prime_numbers))

get_prime_numbers(10000)
#10000000 664579 48.8s


#两种算法的对比的完整代码 

# import datetime

# upper_limit = 100000
# delta = [0,0]
# counts = [0,0]

# start = datetime.datetime.now()
# for _ in range(10):
#     counts[0] = 0
#     for x in range(2,upper_limit):
#         for i in range(2,int(x**0.5)+1):
#             if x % i == 0:
#                 break
#         else:
#             #print(x)
#             counts[0] += 1
# delta[0] = (datetime.datetime.now() - start).total_seconds()


# start = datetime.datetime.now()
# for _ in range(10):
#     counts[1] = 1
#     #print(2)
#     for x in range(3,upper_limit,2):
#         for i in range(3,int(x**0.5)+1,2):
#             if x % i == 0:
#                 break
#         else:
#             #print(x)
#             counts[1] += 1
# delta[1] = (datetime.datetime.now() - start).total_seconds()

# print(delta, sep="\t")
# print(counts, sep="\t")