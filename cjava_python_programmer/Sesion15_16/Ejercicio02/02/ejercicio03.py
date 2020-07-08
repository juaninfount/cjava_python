import sys

def windows_interaction():
    assert ('win32' in sys.platform)
    print('Hacer algo')

try:
    windows_interaction()
except AssertionError as error:
    print("No se esta ejecutando sistema win32.")
else:
    print('Ejecutando la claúsula else.')
finally:
    print('Última sentencia')