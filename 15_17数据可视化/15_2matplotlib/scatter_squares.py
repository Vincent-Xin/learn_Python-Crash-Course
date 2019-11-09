import matplotlib.pyplot as plt

x_values=list(range(1,101))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
plt.tick_params(axis='both',which='major',labelsize='14')
plt.axis([0,110,0,11000])


plt.savefig('filename.pdf',bbox_inches='tight')
plt.show()
