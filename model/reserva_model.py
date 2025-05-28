from model.bancoSQLite import bd

class Reserva(bd):
    _tablename_ = 'Reservas'
    id = bd.Column(bd.Integer, primary_key=True)
    turma_id = bd.Column(bd.Integer, nullable=False)
    sala = bd.Column(bd.String(50), nullable=False)
    data = bd.Column(bd.String(20), nullable=False)
    hora_inicio = bd.Column(bd.String(10), nullable=False)
    hora_fim = bd.Column(bd.String(10), nullable=False)