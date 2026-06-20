from flask import render_template,request,redirect,session,flash
from service.usuario_service import UsuarioService

service = UsuarioService()

def tela_login():
    return render_template("login.html")


def login():
    email = request.form["email"]
    senha = request.form["senha"]
    usuario = service.autenticar(email,senha)

    if usuario:
        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        return redirect("/home")
    flash("Usuário ou senha inválidos")
    return redirect("/")


def tela_cadastro():
    return render_template("cadastro.html")

def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    service.cadastrar(nome,email,senha)
    flash("Usuário cadastrado com sucesso!")
    return redirect("/")


def home():
    if "usuario_id" not in session:
        return redirect("/")
    return render_template("home.html",nome=session["usuario_nome"])

def listar_usuarios():
    # Segurança: impede que visitantes não logados acessem a lista
    if "usuario_id" not in session:
        return redirect("/")
        
    usuarios_cadastrados = service.listar_todos()
    return render_template("usuarios.html", usuarios=usuarios_cadastrados)

def logout():
    session.clear()
    return redirect("/")