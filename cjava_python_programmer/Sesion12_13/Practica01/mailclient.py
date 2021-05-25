"""
en  https://myaccount.google.com/lesssecureapps?gar=1, habilitar el envio de correos desde aplicaciones menos seguras (emisor)
"""

import smtplib
from datetime import datetime 

class mailclient:    
    def __init__(self, subject, sendfrom, password, sendto, message):
        headers = {
                        'Content-Type': 'text/html; charset=utf-8',
                        'Content-Disposition': 'inline',
                        'Content-Transfer-Encoding': '8bit',
                        'From': sendfrom,
                        'To': sendto,
                        'Date': datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
                        'X-Mailer': 'python',
                        'Subject': subject,
                        'Password':password,
                        'Message':message
                  }
        self._headers  = headers        

    def send(self):        
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.starttls() # setear conexion smtp actual en modo TLS        
        print(self._headers)        
        self._headers['Message'] = 'Subject: {}\n\n{}'.format(self._headers['Subject'], self._headers['Message'] )        
        server.login(   self._headers['From'], self._headers['Password'] )              
        server.sendmail(self._headers['From'], self._headers['To'], self._headers['Message'].encode("utf8"))
        server.quit()
        print('Correo enviado exitosamente')