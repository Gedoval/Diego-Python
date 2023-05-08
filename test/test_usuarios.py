import pytest
from database.mysql import MySqlDriver
from repository.UsuariosRepository import UsuariosRepository
from model.usuarios import Usuarios


class TestUsuarios:

    @pytest.fixture
    def mysql_local(self):
        return MySqlDriver(env='local')

    @pytest.fixture
    def usuarios_repo(self, mysql_local):
        return UsuariosRepository(db=mysql_local)

    def test_get_all_usuarios(self, usuarios_repo):
        usuarios = usuarios_repo.get_all_usuarios()
        assert len(usuarios) > 0

    def test_insert_new_usuario(self, usuarios_repo):
        usuario = Usuarios(nombre='Agarramela', apellido='ConLaMano', cuit=666)
        usuarios_repo.insert(usuario)

        usuario = usuarios_repo.find_by_name('Agarramela')[0]

        assert usuario is not None
        assert usuario.get('Apellido') == 'ConLaMano'
        assert usuario.get('CUIT') == 666

