import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = "sender mail address"
to_address = "receivers mail address"

# instance of MIMEMultipart
mail = MIMEMultipart()

# set sender email address
mail['From'] = from_address

# set receivers email address
mail['To'] = to_address

# subject
mail['Subject'] = "Subject of the email"

# body
body = "Body of the email."

# attach the body with the mail instance
mail.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "sample.pdf"  # file name with extension
attachment = open(filename, 'rb') 

# instance of MIMEBase
file_base = MIMEBase('application', 'octet-stream')

# enoded form
file_base.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(file_base)

file_base.add_header('Content-Disposition', 'attachment; filename = %s' % filename)

# attach the instance base to instance mail
mail.attach(file_base)

# create SMTP session
sess = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
sess.starttls()

# Authentication
sess.login(from_address, "password of the sender email")

# Converts the Multipart mail into string
text = mail.as_string()

# sending the mail
sess.sendmail(from_address, to_address, text)

# terminate the session
sess.quit()
