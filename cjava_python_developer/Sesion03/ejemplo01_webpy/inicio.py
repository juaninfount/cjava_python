import web

urls = (
    '/','index',
    '/informacion','informacion'
)

app = web.application(urls, globals())

class index:

    def GET(self):
        return """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        </head>        
        <body><h1>Página Principal</h1>
        <br>
        <br>
        <a href='informacion'>Página auxiliar</a>        
        </body>
        </html>"""

class informacion:

    def GET(self):
        return """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        </head>        
        <body><h1>Página Secundaria</h1>
        <br>
        <br>
        <a href='/'>Página principal</a>        
        </body>
        </html>"""

if __name__ == "__main__":
    app.run()    
