import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
from itertools import cycle
import time

# Configuration des expéditeurs SMTP
smtp_senders = [
    your email and password here]

# Demander les informations de l'utilisateur
receiver_email = input("Veuillez entrer l'email du destinataire : ")
email_count = int(input("Combien d'emails souhaitez-vous envoyer ? "))

# Corps de l'e-mail
subject = "你已被黑客攻击"
body = "您正面临黑客攻击，请发送邮件至 « ouber.it@gmail.com » 停止邮件发送。"
filename = "video.mp4"  # Chemin de la pièce jointe

# Cycler les expéditeurs SMTP
smtp_sender_cycle = cycle(smtp_senders)


# Fonction pour créer un message
def create_message(sender, receiver, subject, body, filename):
    message = MIMEMultipart()
    anonymous_sender_name = "匿名"
    anonymous_sender_email = "no-reply@example.com"
    message["From"] = formataddr((anonymous_sender_name, anonymous_sender_email))
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Ajouter la pièce jointe
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}",
            )
            message.attach(part)
    except FileNotFoundError:
        print(f"Fichier {filename} introuvable. L'e-mail sera envoyé sans pièce jointe.")

    return message


# Fonction pour envoyer un e-mail via SMTP
def send_via_smtp(sender, password, smtp_server, port, receiver, message):
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    print(f"E-mail envoyé avec succès à {receiver} via {sender}")


# Envoyer les emails
def send_emails(count):
    current_smtp_sender = next(smtp_sender_cycle)
    for i in range(count):
        message = create_message(
            sender=current_smtp_sender["email"],
            receiver=receiver_email,
            subject=subject,
            body=body,
            filename=filename,
        )

        try:
            # Envoyer l'e-mail via SMTP
            send_via_smtp(
                current_smtp_sender["email"],
                current_smtp_sender["password"],
                current_smtp_sender["smtp_server"],
                current_smtp_sender["port"],
                receiver_email,
                message,
            )

            # Alterner entre les expéditeurs SMTP après chaque e-mail
            if (i + 1) % len(smtp_senders) == 0:
                current_smtp_sender = next(smtp_sender_cycle)

        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email {i + 1}: {e}")
            continue

        print(f"Email {i + 1}/{count} envoyé.")


# Étape principale
try:
    print("\nEnvoi des emails...")
    send_emails(email_count)
    print("\nTous les emails ont été envoyés avec succès !")
except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
