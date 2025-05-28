from flask import Flask
banco_de_dados = "banco_de_dados.db"

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    return app