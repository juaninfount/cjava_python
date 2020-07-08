import web
from DbClient import DbClient
from Persona import Persona
from web import form

urls = (
        '/','Index' 
)

render = web.template.render('templates')
app    = web.application(urls, globals())

myform = form.Form(
        form.Textbox('dni', id='dni', description='DNI:'), 
        form.Textbox('nombre', id='nombre', description='Nombre:'),
        form.Textbox('apellido', description="Apellido:"),
        form.Textbox('direccion', id='direccion', description='Dirección:'),
        form.Textbox('telefono', id='telefono', description='Teléfono:')
        )

class Index:
    def GET(self):
        form = myform()                        
        return render.Index(form)
  
    def POST(self):        
        i = web.input()
        objpersona = Persona(i.dni, i.nombre, i.apellido, i.direccion, i.telefono)
        print("dni :" + objpersona.dni)
        objdbclient = DbClient()
        objdbclient.insert_new_record(objpersona)       
        return "Registrado"
                    
if __name__ == "__main__":
    app.run()