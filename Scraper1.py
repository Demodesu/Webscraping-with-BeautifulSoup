# from bs4 import BeautifulSoup
# #https://www.youtube.com/watch?v=XVv6mJpFOb0

# #open specific html file name
# with open('home.html','r') as html_file:
# 	content = html_file.read()

# 	#create instance and print html
# 	soup = BeautifulSoup(content,'lxml')
# 	#find specific tags
# 	tags = soup.find('h5')
# 	#find all tags
# 	all_tags = soup.find_all('h5')
# 	# #print all texts in tags
# 	# for course in all_tags:
# 	# 	print(course.text)
# 	course_cards = soup.find_all('div', class_ = 'card')
# 	for course in course_cards:
# 		course_name = course.h5.text
# 		course_price = course.a.text.split()[-1]

# 		print(f'{course_name} costs {course_price}')

# #we can right click and inspect to see html

from bs4 import BeautifulSoup
import requests #request information form a website
import time

#
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
	#request html information from web
	html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

	soup = BeautifulSoup(html_text,'lxml')
	#inspect html and find what you want
	jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
	for count, job in enumerate(jobs):
		published_date = job.find('span', class_ = 'sim-posted').span.text
		if 'few' in published_date:
			company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') #replace white spaces with empty space
			more_info = job.header.h2.a['href']
			skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
			if unfamiliar_skill not in skills:
				with open(f'Update_Files/{count}.txt', 'w') as f:
					f.write(f'Company: {company_name.strip()} \n')
					f.write(f'Skills: {skills.strip()} \n')
					f.write(f'Info: {more_info} \n')
				print(f'File saved: {count}')

if __name__ == '__main__':
	while True:
		find_jobs()
		time_wait = 0.25
		print(f'Waiting {time_wait} minute(s)...')
		time.sleep(time_wait * 60) # in seconds
