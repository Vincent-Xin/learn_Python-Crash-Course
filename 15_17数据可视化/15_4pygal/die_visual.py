import pygal

from die import Die

die=Die()

results=[]
frequencies=[]

def roll_die(roll_num):
	for x in range(roll_num):
		result=die.roll()
		results.append(result)

def count_side_num(results):
	for result in range(1,die.sides_num+1):
		frequency=results.count(result)
		frequencies.append(frequency)
	return frequencies

roll_die(1000)
count_side_num(results)

hist=pygal.Bar()

hist.title='1000times rollings of a D6'
hist.x_labels=list(range(1,die.sides_num+1))
hist.x_title='Results'
hist.y_title='Frequencies of Results'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

# print(results)
print(frequencies)