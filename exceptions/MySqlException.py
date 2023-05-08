class MySqlException(Exception):
    MESSAGE = 'No hay una instancia de MySql en localhost, atorrante'

    def __init__(self, errors):
        super().__init__(self.MESSAGE)
        self.errors = errors
