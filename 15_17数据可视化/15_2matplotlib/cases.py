#15-1 15-2
import matplotlib.pyplot as plt


# plt.plot([1,2,3,4,5],[x**3 for x in range(1,6)],linewidth=2)
# plt.axis([0,10,0,150])
# plt.show()
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,
	edgecolor='none',c=x_values,cmap=plt.cm.Reds,s=20)
plt.savefig('cases.svg',bbox_inches='tight')
plt.show()