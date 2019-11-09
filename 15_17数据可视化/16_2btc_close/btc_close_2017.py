import json
import pygal
import math
from itertools import groupby

filename='btc_close_2017.json'
with open(filename,'r') as f:
	btc_data=json.load(f)

# for btc_dict in btc_data:
# 	date=btc_dict['date']
# 	month=int(btc_dict['month'])
# 	week=int(btc_dict['week'])
# 	weekday=btc_dict['weekday']
# 	close=int(float(btc_dict['close']))
# 	print("{}is month {} week {},{},the close price is {} RMB.".format(
# 		date,month,week,weekday,close))
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))

line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价（￥）'
line_chart.x_labels=dates
N=20
line_chart.x_labels_major=dates[::N]
line_chart.add('log收盘价',close)
line_chart.render_to_file('收盘价折线图.svg')

line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价对数变换（￥）'
line_chart.x_labels=dates
N=20
line_chart.x_labels_major=dates[::N]
close_log=[math.log(_) for _ in close]
line_chart.add('log收盘价',close_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')

def draw_line(x_data,y_data,title,y_legend):
	xy_map=[]
	for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda a:a[0]):
		y_list=[v for a,v in y]
		xy_map.append([x,sum(y_list)/len(y_list)])
	x_unique,y_mean=[*zip(*xy_map)]
	line_chart=pygal.Line()
	line_chart.title=title
	line_chart.x_labels=x_unique
	line_chart.add(y_legend,y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

index_month=dates.index('2017-12-01')
line_chart_month=draw_line(months[:index_month],close[:index_month],
	'收盘价月日均值','月日均值')
# line_chart_month

index_week=dates.index('2017-12-11')
line_chart_week=draw_line(weeks[1:index_week],close[:index_week],
	'收盘价周日均值','周日均值')
# line_chart_week

wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekday_int=[wd.index(x)+1 for x in weekdays[1:index_week]]
line_chart_weekday=draw_line(weekday_int,close[1:index_week],
	'收盘价周均值','周均值')
# line_chart_weekday
charts=['收盘价折线图.svg','收盘价对数变换折线图.svg',
	'收盘价月日均值.svg','收盘价周日均值.svg','收盘价周均值.svg']
with open ('收盘价dashboard.html','w',encoding='utf-8') as html_file:
	html_file.write("<html><head><title>收盘价</title><meta charset='utf-8'>")
	html_file.write("</head><body>\n")
	for svg in charts:
		html_file.write('	<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
	html_file.write('</body></html>')
