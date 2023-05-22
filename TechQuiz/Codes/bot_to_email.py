from smtplib import SMTP
from email.message import EmailMessage

def sendEmail(fileName,filePath, email):

    file = open(filePath,'rb')

    user = "techquizmaua@gmail.com"
    password = "wgdomarxnnqlimiu"
    smtp_porta = 587
    
    msg = EmailMessage()
    msg['To'] = email
    msg['Subject'] = f"Planilha TechQuiz_{fileName}"
    msg.add_attachment(file.read(),maintype='application', subtype='octet-stream', filename=f"TechQuiz_{fileName}.xlsx")

    with SMTP("smtp.gmail.com",smtp_porta) as email:
        email.starttls()
        email.login(user,password)
        email.send_message(msg)
        email.quit()
