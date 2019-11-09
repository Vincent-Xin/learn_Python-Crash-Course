# -*- coding: utf-8 -*-
'''观察随着扔硬币的数量越来越多，大数定理的表现'''
import pygal
from matplotlib import pyplot as plt
from random import choice

# N=1000 #coins counts

def random_coins(N):
	probs=[]
	for n in range(1,N+1):
		times=0
		for i in range(1,n+1):
			once=choice([1,2])
			if once==1:
				times+=1
		probs.append(times/n)
	return probs

# def draw_chart(probs):
# 	line_chart=pygal.Line(show_minor_x_labels=False)
# 	line_chart.title='模拟硬币正面朝上的概率随硬币数量增加的变化'
# 	line_chart.x_labels=list(range(1,N+1,int(N/10)))
# 	line_chart.x_labels_major=list(range(1,N+1,int(N/10)))
# 	line_chart.add('正面朝上概率',probs)
# 	line_chart.render_to_file('硬币概率_1000.svg')
# 	return line_chart

def draw_chart(probs):
	fig=plt.figure(dpi=128,figsize=(10,6))
	plt.plot(list(range(1,len(probs)+1)),probs,linewidth=1,c='red',alpha=0.8)
	plt.xlabel('Times',fontsize=15)
	plt.title('Changes with times of coins',fontsize=20)
	plt.ylabel('Probabilities',fontsize=15)
	plt.tick_params(axis='both',which='major',labelsize=15)
	# plt.savefig('正面朝上概率变化.svg',bbox_inches='tight')
	plt.show()

coin_probs=random_coins(1000)
draw_chart(coin_probs)









