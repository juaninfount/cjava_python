import web
from web import form
import mailclient

urls = (
        '/','index' 
)

render = web.template.render('templates')
app    = web.application(urls, globals())

myform = form.Form(
        form.Textbox('asunto',id='asunto',description='Asunto:'), 
        form.Textbox('desde',id='desde',description='Correo Desde:'),
        form.Password('password',description="Contrasenha:"),
        form.Textbox('destino',id='destino',description='Correo Destino:'), 
        form.Textarea('mensaje',id='mensaje',description='Mensaje:')
        )

class index:
    def GET(self):
        form = myform()                
        return render.index(form)
        
    def POST(self):        
        i = web.input()
        client = mailclient.mailclient(i.asunto, i.desde, i.password, i.destino, i.mensaje)
        client.send()
        return "Mensaje enviado"
                    
if __name__ == "__main__":
    app.run()