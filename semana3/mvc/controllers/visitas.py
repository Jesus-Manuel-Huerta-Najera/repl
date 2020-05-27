import web
from datetime import date
from datetime import datetime

class Visitas:
    def GET(self, name):
        try:
          cookie = web.cookies()
          visitas = 0
          today = date.today()
          now1 = datetime.now()
          now = now1.hour
          web.setcookie("Hora",str(now),expires="", domain= None)
          web.setcookie("Fecha",str(today),expires="", domain= None)
          if name:
            web.setcookie("name",name,expires="", domain= None)
          else:
            name = "Anónimo"
            web.setcookie("name",name,expires="", domain= None)
          if cookie.get("visitas"):
            visitas = int(cookie.get("visitas"))
            visitas += 1
            web.setcookie("visitas",str(visitas),expires="", domain= None)
          else:
            web.setcookie("visitas",str(visitas),expires="", domain= None)
            visitas = "1"
          return "Visitas: " + str(visitas) + ", Nombre: " + name + ", Fecha: " + str(today) + ",Hora: " + str(now)

        except Exception as e:
          return "Error"+str(e.args)