from flask import Flask, render_template

#criando a aplicação Flask
app = Flask(__name__)

#Definindo uma rote basica que responde a requisições HTTP GET
@app.route("/")
def root():
    return "<h1>Olá, Mundo!</h1>"

if __name__ == "__main__":
    app.run(debug=True)