def make_car(maker,size,*infos_1,**infos_2):
	car={}
	car['maker']=maker
	car['seze']=size
	if infos_1:
		car['infos']=infos_1
	for key,value in infos_2.items():
		car[key]=value
	return car