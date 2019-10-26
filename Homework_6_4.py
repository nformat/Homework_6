import smtplib
import base64

f = "py.test.mail.ek@gmail.com"
t = "el.piankova@gmail.com"
pas = base64.b64decode(b'TXlQeXRob25UZXN0UGEkJHcwcmQ=').decode('utf-8')
msg = "It's works!"

with  smtplib.SMTP("smtp.gmail.com", 587) as mail:
    mail.starttls()
    mail.login(f, pas)
    mail.sendmail(from_addr=f, to_addrs=t, msg=msg)
