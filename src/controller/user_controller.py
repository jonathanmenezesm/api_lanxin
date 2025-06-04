from flask import Blueprint, render_template
from database.usuarios import USERS

# Criação do Blueprint para a rota user
user_route = Blueprint('user', __name__)

'''
Criação do Blueprint para a rota de usuários
- /user/ (GET)- Listar usuários
- /user/ (POST) - Inserir cliente no servidor (Login)
- /user/new (GET) - Criar novo usuário
- /user/<user_id> (GET )- Obter usuário por ID
- /user/<user_id>/edit (GET)- Editar usuário por ID
- /user/<user_id>/update (PUT)- Atualizar usuário por ID
- /user/<user_id>/delete (DELETE)- Deletar usuário por ID
'''

@user_route.route('/')
def listar_usuarios():
    # listar usuários
    return render_template('listar_usuarios.html', users=USERS)

@user_route.route('/', methods=['POST'])
def inserir_usuario():
    # inserir usuário no servidor (Login)
    pass

@user_route.route('/new')
def registrar_usuario():
    # formulario para criar novo usuário
    return render_template('registrar_usuario.html')

@user_route.route('/<int:user_id>')
def detalhar_usuario(user_id):
    # exibir detalhes do usuário
    return render_template('detalhar_usuario.html')

@user_route.route('/<int:user_id>/edit')
def editar_usuario(user_id):
    # formulario para editar usuário
    return render_template('editar_usuario.html')

@user_route.route('/<int:user_id>/update', methods=['PUT'])
def atualizar_usuario(user_id):
    # atualizar informações do usuário
    pass

@user_route.route('/<int:user_id>/delete', methods=['DELETE'])
def deletar_usuario(user_id):
    # deletar usuário por ID
    pass
