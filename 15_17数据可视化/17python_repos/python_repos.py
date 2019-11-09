import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS
#执行API调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print('Status code',r.status_code)

#将API相应存储在一个变量中
response_dict=r.json()
print(response_dict.keys())

print("Total repositories:",response_dict['total_count'])

repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))

#research on the first repository
repo_dict_0=repo_dicts[0]
print('keys:',len(repo_dict_0.keys()),'\n')

# for key in sorted(repo_dict.keys()):
# 	print(key)

# print('\nSelected information about first repository:')
# print('Name:',repo_dict['name'])
# print('Owner:',repo_dict['owner']['login'])
# print('Stars:',repo_dict['stargazers_count'])
# print('Created:',repo_dict['created_at'])
# print('Updated:',repo_dict['updated_at'])
# print('Repository:',repo_dict['html_url'])
# print('Description:',repo_dict['description'])

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict={
			'value':repo_dict['stargazers_count'],
			'xlink':repo_dict['html_url']
		}
	if repo_dict['description']:
		plot_dict['label']=repo_dict['description']
	else:
		plot_dict['label']='No Description'
	plot_dicts.append(plot_dict)
	
		

my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.title_font_size=24
my_config.x_label_rotation=45
my_config.show_lengend=False
my_config.label_font_size=14
my_config.major_label_font_size=20 #好像没什么效果
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title=('Most-Starred Python Projects on Github')
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repos_2.3.svg')
# i=0
# for repo_dict in repo_dicts:
# 	if repo_dict['name'] == 'system-design-primer':
# 		print(i)
# 		break
# 	i+=1

# print(repo_dicts[1]['name']+'\n'+repo_dicts[1]['created_at']+'\n'+repo_dicts[1]['updated_at'])





