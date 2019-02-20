from twilio.rest import Client

#your account sid and quth token from twilio.com/user/account
account_sid="AC356ba809f7aed2197cdfad949f212a35"
auth_token="834c5155d4d6f277bb44d7903708d9d7"
client=Client(account_sid,auth_token)

message=client.messages.create(
    body="my name is xiao nini",
    to="+6598681209",#replace with your phone number
    from_="+7027660369") #replace with your twilio number
print message.sid
