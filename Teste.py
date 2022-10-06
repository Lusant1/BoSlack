import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)
anexo = "https://drive.google.com/file/d/1yR0lCwSxKbKg7-ULznwDQgtV1-Xz_pw0/view?usp=sharing"
# configurar as informações do seu e-mail
email.To = "luiz.santos@kovi.com.br"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
<p>Olá, aqui é o código Python</p>

<p>Abs,</p>
<p>Código Python</p>
"""

anexo.Attachment()
email.Send()
print("Email Enviado")