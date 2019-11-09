import pygal

from die import Die

die_1=Die()
die_2=Die()

results=[]
frequencies=[]
max_sides_num=die_1.sides_num+die_2.sides_num

def roll_die(roll_num):
	for x in range(roll_num):
		result=die_1.roll()+die_2.roll()
		results.append(result)

def count_side_num(results):
	for result in range(2,max_sides_num+1):
		frequency=results.count(result)
		frequencies.append(frequency)
	return frequencies

hist=pygal.Bar()

roll_die(1000)
count_side_num(results)

hist=pygal.Bar()

hist.title='1000times rollings of a two D6s'
hist.x_labels=list(range(2,max_sides_num+1))
hist.x_title='Results'
hist.y_title='Frequencies of Results'

hist.add('D6',frequencies)
hist.render_to_file('dice_visual.svg')

# print(results)
print(frequencies)