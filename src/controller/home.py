from flask import Blueprint, render_template

# Criação do Blueprint para a rota home
home_route = Blueprint('home', __name__)

# Rota para renderizar a página inicial
@home_route.route('/')
def home():
    return render_template('home.html')