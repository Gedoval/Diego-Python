import pymysql

from exceptions.MySqlException import MySqlException
from exceptions.query_exception import QueryException


class MySqlDriver:
    DB = {
        'prd': {
            'host': 'URL en CLoud',
            'user': 'usuario de cloud',
            'password': 'password de cloud',
            'db': 'sarasa'
        },
        'local': {
            'host': 'localhost',
            'user': 'root',
            'password': 'diegoPelado',
            'db': 'test'
        }
    }

    def __init__(self, env='local'):
        self.env = env
        self.driver = self.connect_driver()

    def connect_driver(self):
        mysql_datos = self.DB[self.env]
        host = mysql_datos['host']
        try:
            driver = pymysql.connect(host=host,
                                     user=mysql_datos['user'],
                                     password=mysql_datos['password'],
                                     database=mysql_datos['db'],
                                     cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            raise MySqlException(errors=e.__cause__)
        return driver

    def run_query(self, **kwargs):
        query = kwargs.get('query')
        parameters = kwargs.get('params')
        if query is None:
            raise QueryException
        try:
            with self.driver.cursor() as cursor:
                cursor.execute(kwargs.get('query'), parameters)
                result = cursor.fetchall()
        finally:
            cursor.close()
        return result
