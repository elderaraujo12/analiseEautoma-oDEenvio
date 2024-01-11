
import smtplib
import mimetypes
import ssl
from email.message import EmailMessage

#dados do email

password = open("senha", "r").read()
from_email = "mayconsuel1155@gmail.com"
to_email = "mayconsuel1155@gmail.com"
sbject = "Automação de Planilha"
body = """"
ola, segue em a nexo  planilha
a disposição para mais informação 
"""

message = EmailMessage()
message [f"from"] = from_email
message["to"] = to_email
message ["subject"] = sbject

message.set_content(body)
safe = ssl.create_default_context()

#adicionar anexo

anexo = "test.xlsx"
mime_typy,mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_subtype,
        subtype=mime_typy,
        filename=anexo
    )
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtp.sendmail(
            from_email,
            to_email,
            message.as_string()
        )