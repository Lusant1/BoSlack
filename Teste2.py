import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')
# criar um email
email = outlook.CreateItem(0)

# configurar as informações do seu e-mail
email.To = "luiz.santos@kovi.com.br"

email.Subject = "E-mail automático do Python (Transferências De Ruptura e D-1)"
email.HTMLBody = '<h1>Boa tarde, segue em anexo o Farol De Resultdos Das Transferências De Ruptura e D-1</h1>'

anexo = "C:\\Users\\aluga.com\\Downloads\\Transf Diária.png"
email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")
