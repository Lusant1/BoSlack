import email
import os
import smtplib
from email.mime import image
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import time

email1 = 'luiz.santos@kovi.com.br'
cam_assinatura = 'C:\\Users\\aluga.com\\Downloads\\Transf Diária.png'


def enviar_email(cam_assinatura, email):
    # Iniciar servidor SMTP
    host = "smtp-mail.outlook.com"
    porta = 587
    login = "luiz.santos@kovi.com.br"
    senha = "291322Ls!"
    server = smtplib.SMTP(host, porta)
    server.starttls()
    server.login(login, senha)

    # Construir o corpo
    corpo = "<b> Olá, tudo bem?</b> <br/> <br/> Esse e-mail foi gerado automaticamente." \
            "<br/>Segue o Farol De Transferências.<br/>"

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email1
    email_msg['Subject'] = "Envio do Arquivo"
    email_msg.attach(MIMEText(corpo, 'html'))

    # Abrir o arquivo em modo leitura e binário
    attachmente = open(cam_assinatura, 'rb')
    # Ler o arquivo em modo binário e jogamos codificado em base 64
    att = MIMEBase('application', 'octer-stream')
    att.set_payload(attachmente.read())
    encoders.encode_base64(att)

    # Adicionamoeso cabeçalho no tipo anexo de e-mail
    att.add_header('Content-Disposition',
                   f'attachment; filename=Transf Diária.png')

    # Fechamos o arquivo
    attachmente.close()

    # Colocamos no corpo do e-mail
    email_msg.attach(att)

    # Enviar e-mail
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    # Encerrando
    server.quit()

    time.sleep(1)


enviar_email(cam_assinatura, email)
