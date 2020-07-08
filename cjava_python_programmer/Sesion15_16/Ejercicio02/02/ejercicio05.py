try:
    d = {}
    #a = d[1]
    b = d._atributo_ficticio_
except KeyError as e:
    print("Ha ocurrido un KeyError. Mensaje de Excepcion:", e)
except AttributeError as e:
    print("Ha ocurrido un AttributeError. Mensaje de Excepcion:", e)