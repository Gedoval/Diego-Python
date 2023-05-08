
class Usuarios:

    def __init__(self, nombre, apellido, cuit):
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit

    def __str__(self):
        return f'* Nombre: {self.nombre}\n' \
               f'* Apellido: {self.apellido}\n' \
               f'* CUIT: {self.cuit}\n'
