#9-13
from collections import OrderedDict
word_dic=OrderedDict()
word_dic['str()']='make a number be s string'
word_dic['int()']='make an int number'
word_dic['list()']='make a list'
print(word_dic)

for key,value in word_dic.items():
	print(key+":"+word_dic[key])

#9-14
from random import randint
class Die():
	def __init__(self):
		self.sides=6
	def roll_die(self):
		n=randint(1,self.sides)
		print(n)
	def change_sides(self,num):
		self.sides=num
	def zhitouzi(self):
		for i in range(1,11):
			self.roll_die()

a_touzi=Die()
a_touzi.zhitouzi()
a_touzi.change_sides(10)
a_touzi.zhitouzi()
a_touzi.change_sides(20)
a_touzi.zhitouzi()

#9-15
#pymotw.com




