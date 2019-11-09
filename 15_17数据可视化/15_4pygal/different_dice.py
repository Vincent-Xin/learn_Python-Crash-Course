import pygal

from die import Die

die_1=Die()
die_2=Die(10)

results=[]
#15-6
# results=[die_1.roll()+die_2.roll() for x in range(10000)]
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

roll_die(10000)
count_side_num(results)

hist=pygal.Bar()

hist.title='10000times rollings of a D6 and  D10'
hist.x_labels=list(range(2,max_sides_num+1))
#15-6
# hist.x_labels=[x for x in range(2,max_sides_num+1)]
hist.x_title='Results'
hist.y_title='Frequencies of Results'

hist.add('D6&D10',frequencies)
hist.render_to_file('different_dice.svg')

# print(results)
print(frequencies)