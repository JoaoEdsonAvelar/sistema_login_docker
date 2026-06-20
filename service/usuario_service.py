import bcrypt

from models.usuario import Usuario
from repository.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def cadastrar(self, nome, email, senha):
        senha_criptografada = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt())
        usuario = Usuario(None,nome,email,senha_criptografada.decode("utf-8"))
        self.repository.salvar(usuario)

    def listar_todos(self):
        # Busca todos os usuários através do repositório
        return self.repository.listar_todos()


    def autenticar(self, email, senha):
        usuario = self.repository.buscar_por_email(email)
        if usuario is None:
            return None
        senha_banco = usuario["senha"]
        if bcrypt.checkpw(senha.encode("utf-8"),senha_banco.encode("utf-8")):
            print(usuario)
            print(type(usuario))
            return usuario
        
        return None
