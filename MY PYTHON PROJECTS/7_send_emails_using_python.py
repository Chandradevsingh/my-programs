import smtplib as s

obj = s.SMTP('smtp.gmail.com', 587)
obj.ehlo()
obj.starttls()
obj.login('chandradevbijnor@gmail.com', 'Latest$70')
subject = 'Hi...'
body = 'How are you?'
message = f'subject: {subject}\n\n{body}'
listadd = ['chandradevbijnor@gmail.com', 'rvit0950113005@gmail.com']
obj.sendmail('chandradevbijnor@gmail.com', listadd, message)
print('email sent')
obj.quit()