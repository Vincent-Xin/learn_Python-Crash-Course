# -*- coding: utf-8 -*-
import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename_sk='sitka_weather_2014.csv'
filename_dv='death_valley_2014.csv'
def get_data(filename):
	with open(filename) as f:
		reader=csv.reader(f)
		header_row=next(reader)

		# for index,value in enumerate(header_row):
		# 	print(index,value)

		dates,highs,lows=[],[],[]
		for row in reader:
			try:	
				current_time=datetime.strptime(row[0],"%Y-%m-%d")
				high=int(row[1])
				low=int(row[3])
			except ValueError:
				print("missing data",current_time)
			else:
				dates.append(current_time)
				highs.append(high)
				lows.append(low)
	return dates,highs,lows

sk_dates,sk_highs,sk_lows=get_data(filename_sk)
dv_dates,dv_highs,dv_lows=get_data(filename_dv)
	
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(sk_dates,sk_highs,c='green',alpha=0.7,linewidth=1)
plt.plot(sk_dates,sk_lows,c='blue',alpha=0.7,linewidth=1)
plt.plot(dv_dates,dv_highs,c='red',alpha=0.7,linewidth=1)
plt.plot(dv_dates,dv_lows,c='orange',alpha=0.7,linewidth=1)
plt.fill_between(sk_dates,sk_highs,sk_lows,facecolor='blue',alpha=0.2)
plt.fill_between(dv_dates,dv_highs,dv_lows,facecolor='purple',alpha=0.3)
plt.title('Temperature compare between Sitka and death Vally in 2014',
	fontsize=20)
plt.xlabel('Date',fontsize=15)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
