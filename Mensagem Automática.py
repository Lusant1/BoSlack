import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
# Interaction com o Outlook
assert isinstance(outlook.CreateItem, object)
email = outlook.CreateItem(0)
'''
email.To = """ana.pont@kovi.com.br; conrado.morais@kovi.com.br; lucas.paula@kovi.com.br; filipe.reis@kovi.com.br; 
           gustavo.sbruzzi@kovi.com.br; sidnei.beserra@kovi.com.br; ricardo.lopes@kovi.com.br; 
           alexandre.pereira@kovi.com.br; paulo.baptista@kovi.com.br; cleiton.andrade@kovi.com.br;
           celso.filho@kovi.com.br; maria.silva@kovi.com.br"""
           '''
email.To = "lucas.paula@kovi.com.br"
email.Subject = "Indicadores das Transferências"
email.HTMLbody = f"""
<p>Bom dia a todos, segue abaixo o Farol de Indicadores das Transferências Emergenciais.</p>




<p>Dúvidas,estou á disposição</p>
<p>Abs</p>
<p>Código Python</p>
"""
email.Send()
print("Email enviado")
