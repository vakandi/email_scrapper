import smtplib
from email.mime.text import MIMEText

# email address and password of the sender
sender_email = "your_email@example.com"
sender_password = "your_password"

# subject of the email
subject = "Solutions digital pour votre entreprise"
sender_name = "Wael Bousfira, Insight-Development"

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
    message = (f"Bonjour {first_name} {last_name},\n\nJe me permets de vous contacter pour vous présenter notre agence web et les solutions numériques que nous proposons. Nous sommes spécialisés dans le conception et le développement web standard et développment d'applications et logiciel pour entreprise, ainsi que des plateformes sur mesure pour entreprise.\nNous savons que chaque entreprise est unique et a des besoins spécifiques. Notre équipe d'experts travaillera en étroité collaboration avec vous pour comprendre vos besoins et fournir des solutions personnalisés et rentables qui répondent aux objectifs commerciaux de {title}.\n\nSi vous êtes intéressé par nos services, nous serions heureux de discuter de la manière dont nous pourrions collaborer. N'hésitez pas à nous contacter pour parler plus précisemment de vos besoins.\n\nCordialement,\n\n{sender_name}\n")
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

