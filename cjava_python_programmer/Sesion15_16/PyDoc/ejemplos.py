def promedio(a, b):
    'Calcula el promedio de dos numeros.'
    return (a+b)/2

def formula_cuadratica(a, b, c):
    """Resuelve una ecuación cuadrática.
    
    Devuelve en una tupla en dos raíces que resuelvan la
    ecuación cuadrática:

    ax2 + bx + c = 0.


    Utiliza la fórmula general (tambien conocida 
    coloquialmente como el "chicharronero").

    Parámetros:

    a -- coeficiente cuadrático (debe ser distinto de 0)
    b -- coeficiente lineal
    c -- término independiente

    Excepciones:
    ValueError -- Si (a == 0)

    """

    if a == 0:
        raise ValueError('Coeficiente cuadrático no debe ser 0')

    from cmath import sqrt 
    discriminante = b**2 - 4*a*c
    x1 = (-b + sqrt(discriminante)) / (2*a)
    x2 = (-b - sqrt(discriminante)) / (2*a)
    return (x1,x2)

#print(promedio.__doc__)
#print(formula_cuadratica.__doc__)
help(promedio)