# # -*- coding: utf-8 -*-
# #8-6
# def city_county(city,county):
# 	city_county_0='"'+city.title()+','+county.title()+'"'
# 	return city_county_0

# city_county_1=city_county('beijing','china')
# city_county_2=city_county('new york','America')
# city_county_3=city_county('taibei','china')
# print(city_county_1+"\n"+city_county_2+'\n'+city_county_3)

#8-7
# def make_album(singer,album_name):
# 	album={}
# 	album['歌手']=singer
# 	album['专辑名']=album_name
# 	return album

# print(make_album('李志','梵高先生'))

# def make_album2(singer,album_name,song_number=""):
# 	album={}
# 	album['歌手']=singer
# 	album['专辑名']=album_name
# 	if song_number:
# 		album['歌曲数量']=song_number
# 	return album
# print(make_album2('李志','梵高先生',5))

#8-8
def make_album3(singer,album_name,song_number=""):
	album={}
	album['歌手']=singer
	album['专辑名']=album_name
	if song_number:
		album['歌曲数量']=song_number
	return album
while True:
	singer=input("enter a singer:").title()
	album_name=input("enter an album_name:").title()
	if singer=="" and album_name=="":
		break

	a_album=make_album3(singer,album_name)
	print(a_album)

