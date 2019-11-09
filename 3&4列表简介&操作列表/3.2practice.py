#3-4嘉宾名单
guest = ['Jack','Fiona','Billy']
print("I want to invite "+guest[0]+","+guest[1]+" and "+guest[2]+" to have dinner!")
#3-5修改嘉宾名单
print("But "+guest[0]+" can't come for some reason!")
guest[0]='Tom'
print("So I will invite "+guest[0]+" instead!")

#3-6添加嘉宾
print("I found a larger table.")
guest.insert(0,'Jerry')
guest.insert(2,"Jhon")
guest.append("Jhonny")
print(guest)
print("Hi "+guest[0]+",would you like to come to my dinner tonight?")

#3-7缩减名单
print("I only can invite two person to my dinner!")
popped_1=guest.pop(0)
popped_2=guest.pop(2)
popped_3=guest.pop(-1)
popped_4=guest.pop(-1)
print(popped_1)
print(popped_2)
print(popped_3)
print(popped_4)
print(guest[0],guest[1])
del guest[-1],guest[-1]
print(guest)