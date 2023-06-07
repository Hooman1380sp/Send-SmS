import requests
from random import randint
import json

# create random password for send to user 
password=randint(1000,9999)



# these variables are for the message sending api
version = 'v1'
host = 'api.kavenegar.com'
apikey = "your api key in kavenegar"
timeout = None or 10
headers = {
'Accept': 'application/json',
'Content-Type': 'application/x-www-form-urlencoded',
'charset': 'utf-8'
    }
action='sms'
method='send'
params = { 'sender' : '10008663', 'receptor': '123456789(you user phone number)', 'message' :password} 
url = 'https://' + host + '/' + version + '/' + apikey + '/' + action + '/' + method + '.json'
sms=requests.post(url , headers=headers,auth=None,data=params, timeout=timeout).content




# check sms status code and print welcome to user 
response = json.loads(sms.decode("utf-8"))

if (response['return']['status']==200):
	print('your password sended to phone')
	while True:
		human_password=int(input('enter the password: '))

		if human_password==password:
			print('welcome')
			break
		else:
			print('password invlid')
else:
	print(sms)