import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "otky623@gmail.com"
password = "xrjvwhjjhaaklzop"

receiver = "otky623@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi! 
How are you?
bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)