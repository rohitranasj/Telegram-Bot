'''

'''

import requests
import json
from flask import Flask
from flask import request
from flask import Response
import re
from tokenn import *



def writejson(data, filename='response.json'):
	with open(filename,'w') as f:
		json.dump(data,f,indent=4,ensure_ascii=False)


def get_cmc_date(crypto):
	url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
	header = {"X-CMC_PRO_API_KEY":cmc_api}
	param = {'symbol':crypto , 'convert':'USD'}

	r = requests.get(url, headers=header, params=param).json()
	writejson(r)
	
	price = r["data"][crypto]["quote"]["USD"]["price"]
	return price


def parse_message(message):
	chat_id = message["message"]["chat"]["id"]
	text = message["message"]["text"]
	pattern = r'/[a-zA-Z]{2,4}'
	ticker = re.findall(pattern,text)
	if ticker:
		symbol = ticker[0][1:].upper()
	else:
		symbol=''
	return chat_id , symbol

def send_message(chat_id , text='bla-bla'):
	url = 'https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_API>/sendMessage'
	payload = {"chat_id":chat_id, "text":text}
	r = requests.post(url,json=payload)
	return r


app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():

	if request.method == 'POST' :
		msg = request.get_json()
		chat_id , symbol = parse_message(msg)
		if not symbol:
			send_message(chat_id,"wrong_data")
			return Response('OK', status=200)
		price = get_cmc_date(symbol)
		send_message(chat_id,price)
		return Response('ok',status=200)
	else:

		return '<h1>CryptoCurrent Telegran Bot</h1>'


if __name__ == '__main__':
	app.run(debug=True)
