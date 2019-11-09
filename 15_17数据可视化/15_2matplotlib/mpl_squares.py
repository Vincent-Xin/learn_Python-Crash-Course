import matplotlib.pyplot as plt

x_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(x_value,squares,linewidth=1.5)
plt.title('Data Analysis Practice',fontsize=15)
plt.xlabel('Xvalues',fontsize=12)
plt.ylabel('Squares',fontsize=12)
plt.tick_params(axis='both',labelsize=10)
plt.show()

