#Ejercicio 2:  Escribir una función reciba un diccionario con las asignaturas 
#  las notas de un alumno y devuelva otro diccionario con 
#  asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
#print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
#{'MATEMÁTICAS': 'A', 'FÍSICA': 'A', 'QUÍMICA': 'C', 'ECONOMÍA': 'D', 'HISTORIA': 'B', 'PROGRAMACIÓN': 'D'}

def calificacion(resultados):
    nuevos_resultados = {}
    for x in resultados:
        nota_numerica = resultados[x] 
        nota_literal = ''
        if nota_numerica <= 20 and nota_numerica >= 18:
           nota_literal = 'A'
        elif nota_numerica <= 17 and nota_numerica >= 15:
           nota_literal = 'B'
        elif nota_numerica <= 14 and nota_numerica >= 11:
           nota_literal = 'C'
        elif nota_numerica <= 10 and nota_numerica >= 0:
           nota_literal = 'D'
        nuevos_resultados[ x.upper() ] = nota_literal

    return nuevos_resultados


print(calificacion({'Matemáticas':20, 'Física':16, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))