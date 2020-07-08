class Alumno:

    def __init__(self, codigo, nombre, apellido_pat, apellido_mat, celular):
        self._codigo = codigo
        self._nombre = nombre
        self._apellido_pat = apellido_pat
        self._apellido_mat = apellido_mat
        self._celular = celular

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido_pat(self):
        return self._apellido_pat

    @apellido_pat.setter
    def apellido_pat(self, apellido_pat):
        self._apellido_pat = apellido_pat

    @property
    def apellido_mat(self):
        return self._apellido_mat

    @apellido_mat.setter
    def apellido_mat(self, apellido_mat):
        self._apellido_mat = apellido_mat

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, celular):
        self._celular = celular