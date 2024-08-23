import smtplib

my_email = "aleemhassaan70@gmail.com"
password = "adsi wfpp kqej bclm "
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="um7339605@gmail.com", msg="Subject:Hello\n\n\n")
connection.close()