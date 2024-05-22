import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, message_body, smtp_server, smtp_port, smtp_username, smtp_password): #changes: reciever emails shall be stored in a list
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body to the email
    msg.attach(MIMEText(message_body, 'plain'))

    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# Replace these variables with your own values
sender_email = 'rishu@intozi.io'
receiver_email = 'aditya@intozi.io'
subject = 'Test Email'
message_body = 'This is a test email sent from Python!'
smtp_server = 'smtp-mail.outlook.com' #outlook smtp server
smtp_port = 587  # SMTP port
smtp_username = 'rishu@intozi.io'
smtp_password = 'xldxcgshaferaxxn' #app specific password

# Call the function to send the email
# send_email(sender_email, receiver_email, subject, message_body, smtp_server, smtp_port, smtp_username, smtp_password)