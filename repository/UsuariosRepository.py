class UsuariosRepository:

    TABLE_NAME = 'Usuarios'
    NOMBRE = 'Nombre'
    APELLIDO = 'Apellido'
    CUIT = 'CUIT'
    ID = 'UsuarioId'

    def __init__(self, db):
        self.db = db

    def insert(self, usuario):
        query = self.get_insert_query(usuario)
        return self.run_query(query=query)

    def update(self, usuario, usuario_id):
        query = self.get_update_query(usuario, usuario_id)
        return self.run_query(query=query)

    def find_by_name(self, usuario_nombre):
        query = f'SELECT * FROM {self.TABLE_NAME} WHERE {self.NOMBRE} = "{usuario_nombre}"'
        return self.run_query(query=query)

    def get_all_usuarios(self):
        query = f'SELECT * FROM {self.TABLE_NAME}'
        return self.run_query(query=query)

    def run_query(self, **kwargs):
        return self.db.run_query(query=kwargs.get('query'))

    def get_insert_query(self, usuario):
        query = f'INSERT INTO {self.TABLE_NAME} ' \
                f'({self.NOMBRE}, {self.APELLIDO}, {self.CUIT})' \
                f' VALUES' \
                f' ("{usuario.nombre}", "{usuario.apellido}", {usuario.cuit})'
        return query

    def get_update_query(self, usuario, usuario_id):
        query = f'UPDATE {self.TABLE_NAME} SET ' \
                f'{self.NOMBRE} = "{usuario.nombre}", {self.APELLIDO} = "{usuario.apellido}", {self.CUIT} = "{usuario.cuit}" ' \
                f'WHERE {self.APELLIDO} = {usuario_id}'
        return query
