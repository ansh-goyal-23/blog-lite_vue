import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template
from create_pdf import create_pdf_report
# from routes import *

SMTP_SERVER_HOST = "localhost"
SMTP_SERVER_PORT = 1025
SENDER_ADDRESS = "xyz@gmail.com"
SENDER_PASSWORD = " "

def send_email(to_address, subject, message, content="text", attachment_file=None):
    msg = MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = subject

    if content == "html":
        msg.attach(MIMEText(message, "html"))
    else:
        msg.attach(MIMEText(message, "plain"))

    if attachment_file:
        with open(attachment_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_file}",
        )
        msg.attach(part)

    s = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
    s.login(SENDER_ADDRESS, SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()

    return True


def format_message(template_file, data={}):
    with open(template_file) as file_:
        template = Template(file_.read())
        message = template.render(data=data)

        return message


def daily_post(data):
    message = format_message("daily_reminder_email.html", data=data)

    send_email(
        data["email"],
        subject="Been a while",
        message=message,
        content="html",
        # attachment_file="xyz.pdf",
    )

def monthly_post(data):
    message = format_message("monthly_reminder_email.html", data=data)
    file_name = create_pdf_report(data=data)

    send_email(
        data["email"],
        subject="Monthly User Report",
        message=message,
        content="html",
        attachment_file=file_name,
    )

