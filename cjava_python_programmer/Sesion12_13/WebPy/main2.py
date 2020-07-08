import smtplib


headers = {
    'Content-Type':''
}



subject = 'Prueba correo jorge'
message =  'Soy Juan, y este es mi segundo mensaje'
message =  'Subject: {}\n\n{} '.format(subject,message)  
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls() # setear conexion smtp actual en modo TLS
server.login('juan.infount@gmail.com','@4n45t4c14r0m4n0v@')
server.sendmail('juan.infount@gmail.com','jorge.l.cordova.lopez@gmail.com', message)
server.quit()
print('Correo enviado exitosamente')
