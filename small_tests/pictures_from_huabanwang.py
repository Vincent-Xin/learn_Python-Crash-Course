import requests
import re

URL='https://huaban.com/explore/renxiangsheying/'
# URL='https://www.toutiao.com/i6491207417328566798/'

response=requests.get(URL)
print(response.status_code)
# print(response.text)
# list_url_images=re.findall(r'src="http://"',response.text)
# print(len(list_url_images))
# for image_url in list_url_images:
# 	resp=requests.get(image_url)
# 	with open('/pictures_from_huabanwang/') as 
