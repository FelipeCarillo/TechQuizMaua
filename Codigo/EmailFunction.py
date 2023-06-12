from smtplib import SMTP
from email.message import EmailMessage

def sendEmail(email,subject=None,text=None,fileName=None,filePath=None):

    file = open(filePath,'rb')

    user = "techquizmaua@gmail.com"
    password = "wgdomarxnnqlimiu"
    smtp_porta = 587
    
    msg = EmailMessage()
    msg['To'] = email
    msg['Subject'] = subject
    if fileName and filePath:
        msg.add_attachment(file.read(),maintype='application', subtype='octet-stream', filename=fileName)
    if text:
        msg.set_content(text)
        
    with SMTP("smtp.gmail.com",smtp_porta) as email:
        email.starttls()
        email.login(user,password)
        email.send_message(msg)
        email.quit()
