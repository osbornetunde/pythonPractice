import time, schedule
from datetime import datetime as dt
hosts_path = r"/etc/hosts"

redirect = "127.0.0.1"
website_list=["","www.apple.com","web.whatsapp.com","www.facebook.com","facebook.com","www.gmail.com","mail.google.com","www.google.com","google.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,0) <dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,2):
		print("working hours.....")
		with open(hosts_path,'r+') as file:
			content = file.read()
			print(content)
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("Fun hours")
		time.sleep(5)