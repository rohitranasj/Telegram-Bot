# Telegram-Bot
-----
Telegram Bot for getting the price of cryptocurrency like BTC , ETH in USD.
just send the abbreviation of cryptocurrency after /. e.g
/BTC , /ETH

## Description

- api used for cryptocurrency data - coinmarketcap.com
- request form - /v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD
- sent mgs by bot Manual Method - https://api.telegram.org/bot15586***51:AAHOi04uyrxfZ***VepWyhFolPgNq_OQNO0/sendmessage?chat_id=7998**695&text=%22bye%22
flask is used for connecting with telegram using webhook as it req ssl / https
- For Tunnerling - staqlab-tunnel.com
- we will set webhook at this public url, so that telegram can send us all mgs here in post-json object
- [https://api.telegram.org/bot1598*17*1:AAHOi04uyrxfZ1xoVepjohFolPgNq_OQNO0/setwebhook?url=https://gxaqrw*jeun.staqlab-tunnel.com]


## ToDo list:
- Input Validation
- Deploy pythonanywhere
