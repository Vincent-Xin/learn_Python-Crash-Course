import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
	random_walk=RandomWalk(10000,3)
	random_walk.fill_walk()

	plt.figure(figsize=(10,8))

	points_list=list(range(random_walk.points_number))
	# plt.scatter(random_walk.x_value,random_walk.y_value,
	# 	edgecolor='none',c=points_list,cmap=plt.cm.Blues,s=10)
	plt.plot(random_walk.x_value,random_walk.y_value,linewidth=1)

	plt.scatter(random_walk.x_value[0],random_walk.y_value[0],edgecolor='none',c='red',s=20)
	plt.scatter(random_walk.x_value[-1],random_walk.y_value[-1],edgecolor='none',c='green',s=20)

	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()

	next_walk=input('Next turn of walk?(y/n)')
	if next_walk.lower() == 'n':
		break
	
