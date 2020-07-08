import web
from web import form
 
urls = (
   '/', 'index'
 )
 
plantilla = web.template.render('./templates/') 
app = web.application(urls, globals())
 
myform = form.Form(
        form.Textbox("nombre"),
        form.Textbox("id", form.notnull, form.regexp(r'\d+', 'Debe ser un dígito'),
        form.Validator('Debe ser más de 5', lambda x:int(x)>5)),
        form.Textarea('observacion'),
        form.Checkbox('reenviar'),
        form.Dropdown('prioridad', ['baja', 'media', 'alta']))
 
class index:
# Método de Llegada
 def GET(self):
    form = myform()
    return plantilla.formulario_2(form)
 
 # Método POST
 def POST(self):
    form = myform()
    if not form.validates():
        return plantilla.formulario_2(form)
    else:
    # form.d.nombre y form['nombre'].value son formas equivalente
    # de extraer los argumentos validos del formulario.
        return "Gran exito! Nombre: %s, ID: %s" % (form.d.nombre, form['id'].value)

if __name__ == "__main__":
    app.run()