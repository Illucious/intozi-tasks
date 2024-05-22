import smtplib
from email.mime.text import MIMEText

subject = "Outlook SMTP"
body = "This mail was sent using Outlook's SMTP through a python script."
sender = "visheshgarg@outlook.in"  # Your Outlook email address
recipients = ["visheshgarg570@gmail.com", "	himanshu@intozi.io"]  # Recipient email addresses
password = "lhswpwzwfrpmnmqi"  # Your app-specific password

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp_server:
        smtp_server.ehlo()  # Can be omitted
        smtp_server.starttls()  # Secure the connection
        smtp_server.ehlo()  # Can be omitted
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)
print(send_email)