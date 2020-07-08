import sys

def windows_interaction():
    assert ('windows ' in sys.platform)
    print('Hacer algo')

try:
    windows_interaction()
except AssertionError as error:
    print(error)
    print('La funcion windows_interaction() no fue ejecutada.')



