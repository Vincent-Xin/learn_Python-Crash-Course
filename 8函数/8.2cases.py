#8-3
def make_shirt(size,sentence):
	print("The shirt is "+str(size)+",and "+sentence)

make_shirt(5,'I love you!')
make_shirt(sentence='I lave you!',size=5)

#8-4
def make_shirt2(size='large',sentence='I love Python!'):
	print("The shirt is "+str(size)+",and "+sentence)

make_shirt2()
make_shirt2('medium')
make_shirt2(sentence='I love you!')

#8-5
def describe_city(city,county='China'):
	print(city.title(),"is in",county.title())

describe_city("Beijing")
describe_city("shanghai",county='China')
describe_city("london","british")
