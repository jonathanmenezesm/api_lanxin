from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from database.usuarios import USERS

# Criação do Blueprint para a rota user
user_route = Blueprint('user', __name__)

'''
Criação do Blueprint para a rota de usuários
- /user/ (GET)- Listar usuários OK
- /user/ (POST) - Inserir cliente no servidor 
- /user/new (GET) - Criar novo usuário
- /user/<user_id> (GET )- Obter usuário por ID
- /user/<user_id>/edit (GET)- Editar usuário por ID
- /user/<user_id>/update (PUT)- Atualizar usuário por ID
- /user/<user_id>/delete (DELETE)- Deletar usuário por ID
'''


# listar usuários
@user_route.route('/')
def listar_usuarios():
    return render_template('listar_usuarios.html', users=USERS)

# inserir usuário no servidor 
@user_route.route('/', methods=['POST'])
def inserir_usuario():
    
    data = request.get_json()  
    
    novo_usuario = {
        'id': len(USERS) + 1,
        'nome': data.get('nome'),
        'email': data.get('email')
    }
    USERS.append(novo_usuario)
    return jsonify({'ok': True, 'mensagem': 'Usuário inserido com sucesso!'})

# formulario para criar novo usuário
@user_route.route('/new', methods=['POST'])
def registrar_usuario():
    return render_template('registrar_usuario.html')


# exibir detalhes do usuário
@user_route.route('/<int:user_id>')
def detalhar_usuario(user_id):
    return render_template('detalhar_usuario.html')


# formulario para editar usuário
@user_route.route('/<int:user_id>/edit')
def editar_usuario(user_id):
    return render_template('editar_usuario.html')


# atualizar informações do usuário
@user_route.route('/<int:user_id>/update', methods=['PUT'])
def atualizar_usuario(user_id):
    pass


# deletar usuário por ID
@user_route.route('/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    global USERS
    USERS = [user for user in USERS if user['id'] != user_id]
    return '', 204  # 204 No Content

@user_route.route('/json')
def listar_usuarios_json():
    return jsonify(USERS)