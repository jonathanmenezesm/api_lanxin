from flask import Blueprint, render_template
from database.usuarios import USERS

# Criação do Blueprint para a rota home
home_route = Blueprint('home', __name__)

# Rota para renderizar a página inicial
@home_route.route('/')
def home():
    return render_template('index.html', users=USERS)