import web

urls = (
    '/', 'index',
     '/informacion','informacion'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return """<html>
                <body>
                <h1>Pagina principal</h1>
                <br>
                <a href='/Informacion' > Pagina Auxiliar
                </a>        
                </body>
                </html>"""
                
    class informacion:
        def GET(self):
            return """
                    <html>
                    <body>
                    <h1>Pagina secundaria</h1>
                    <br>
                    <a href='/' > Principal
                    </a>
                    </body>
                    </html>
                    """

if __name__ == "__main__":
    app.run()
