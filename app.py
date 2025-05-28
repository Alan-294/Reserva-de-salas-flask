from config import create_app
from flask import Flask
from controller.reserva_controller import reserva_bp

app = create_app()
app.register_blueprint(reserva_bp, url_prefix='/reservas')

from model.bancoSQLite import inicializar_banco

inicializar_banco()

app = create_app()
app.register_blueprint(reserva_bp, url_prefix='/reservas')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    

