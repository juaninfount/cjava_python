from datetime import datetime

class chat:

    def __init__(self, nombre_cli, mensaje):
        self._codigo = datetime.now().strftime('%Y%m%d%H%M%S')
        self._nombre_cli = nombre_cli
        self._mensaje = mensaje

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre_cli(self):
        return self._nombre_cli

    @nombre_cli.setter
    def nombre_cli(self, nombre_cli):
        self._nombre_cli = nombre_cli

    @property
    def mensaje(self):
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje):
        self._mensaje = mensaje
