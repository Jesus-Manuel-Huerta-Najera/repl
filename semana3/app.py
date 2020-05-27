import web
#pip install web.py
urls = (
    '/(.*)', 'mvc.controllers.visitas.Visitas'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()