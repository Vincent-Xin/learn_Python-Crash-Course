#8-12
def make_sandwich(*sub_materials):
	print("The sandwich is made with: ")
	for sub_material in sub_materials:
		print(sub_material)
make_sandwich('a')
make_sandwich('a','b','s')
make_sandwich(1,'a')
make_sandwich()
#8-13
def build_profile(first,last,**user_info):
	'''创建用户字典'''
	profile={}
	profile['姓氏']=first.title()
	profile['名字']=last.title()
	for key,value in user_info.items():
		profile[key]=value
	return profile

my_info=build_profile('辛','元昌',性别='男',籍贯='山东',现居='北京')
print(my_info)

#8-14
def make_car(maker,size,*infos_1,**infos_2):
	car={}
	car['maker']=maker
	car['seze']=size
	if infos_1:
		car['infos']=infos_1
	for key,value in infos_2.items():
		car[key]=value
	return car
new_car=make_car('who','large',color='blue',tow_package=True)
print(new_car)

def make(a,b='dog'):
	print(a,b)
make('A','cat')