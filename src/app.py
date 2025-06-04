from flask import Flask
from src.controller.home import home_route
from src.controller.user_controller import user_route

#Inicialização da aplicação Flask
App = Flask(__name__)

# Registro de Blueprint 
App.register_blueprint(home_route)
App.register_blueprint(user_route, url_prefix='/user')

#função para renderizar a página inicial  (com debug=True)
App.run(debug=True)