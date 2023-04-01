import smtplib
from email.mime.text import MIMEText

# email address and password of the sender
sender_email = "your_email@example.com"
sender_password = "your_password"

# subject of the email
subject = "Important message"

# read the list of email addresses from the file
with open("emails.list", "r") as email_list:
    email_addresses = email_list.readlines()

#connect to the server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# send the email to each address
for email_address in email_addresses:
    email_address = email_address.strip()
    email_info = email_address.split(',')

    # Collecting the needed informations
    to_email = email_info[0]
    title = email_info[1] # Change company_name to title
    first_name = email_info[2]
    last_name = email_info[3]
    message = (f"Hello {first_name} {last_name},\n\nThis is an important message from {title}.\n\nBest regards,\n {title}")
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    try:
        # send the email
        server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}, Exception:{e}")


server.quit()

