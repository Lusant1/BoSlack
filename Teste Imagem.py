import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

msg = MIMEMultipart('alternative')
msg['Subject'] = "Teste"
msg['From'] = "luiz.santos@kovi.com.br"
msg['To'] = "lucas.paula@Kovi.com.br; luiz.santos@kovi.com.br"

text = MIMEText('<img src="cid:image1">', 'html')
msg.attach(text)

image = MIMEImage(open('/path/to/image', 'rb').read())

# Define the image's ID as referenced in the HTML body above
image.add_header('Content-ID', '<image1>')
msg.attach(image)

s = smtplib.SMTP('localhost')
s.sendmail(from_addr, to_addr, msg.as_string())
s.quit()