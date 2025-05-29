from config import create_app
from flask import Flask
from controller.reserva_controller import reserva_bp
from model.bancoSQLite import inicializar_banco
from model.bancoSQLite import importar_professores_da_api
from model.bancoSQLite import importar_turmas_da_api

app = create_app()
app.register_blueprint(reserva_bp)

inicializar_banco()
importar_professores_da_api()
importar_turmas_da_api()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    

