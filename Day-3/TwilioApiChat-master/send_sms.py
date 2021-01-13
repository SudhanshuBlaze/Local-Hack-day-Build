from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = """Hi, This is Kunal 
Sudhanshu Bsdk
Bola na dusra Kaam Kar rha Hoon......"""
message = client.api.account.messages.create(to=my_cell, from_=my_twilio, body=my_msg)