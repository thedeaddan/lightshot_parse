import random
import string
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

def generate_random_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
i = 0
generated = []
while True:
	i+= 1
	gen_string = generate_random_string(6)
	if gen_string not in generated:
		generated.append(gen_string)
		url = 'https://prnt.sc/'+gen_string
		response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
		soup = BeautifulSoup(response.text, 'lxml')
		try:
			quotes = str(soup.find_all('img', class_='no-click screenshot-image')[0])
		except:
			quotes = str(soup.find_all('img', class_='no-click screenshot-image'))
		try:
			div = quotes.split(" ")[8]
		except:
			print(quotes)
		try:
			url_pic= div.split('"')[1]
		except:
			print(div)
		if "eQqbGWo.jpg" not in quotes:
			if "//st.pr" in url_pic:
				url_pic = "http:"+url_pic
			img_data = requests.get(url_pic,headers={'User-Agent': UserAgent().chrome}).content
			with open('/home/thedeaddan/pics/'+gen_string+'.jpg', 'wb') as handler:
				handler.write(img_data)
			print(url_pic)
			print("saved")
