
archivo = 'file.log'

try:
    with open(archivo) as file:
        read_data = file.read()
except FileNotFoundError as ArchivoNoEncontradoError:
    print("Archivo "+archivo+" no encontrado.")