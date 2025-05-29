import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from config import banco_de_dados as bd

def inicializar_banco():
    conexao = sqlite3.connect(bd)
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor() 
    print("Conexão com o banco de dados estabelecida.")
   
    # Criação das tabelas
   
    # cursor.execute('''
    #                 CREATE TABLE IF NOT EXISTS SALAS (
    #                 ID_SALA INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 AGENDADAS BOOLEAN NOT NULL DEFAULT 0,
    #                 id_turma INTEGER,
    #                 nome_turma TEXT,
    #                 id_professor INTEGER,
    #                 nome_professor TEXT, 
    #                 id_aluno INTEGER,
    #                 nome_aluno TEXT,
    #                 id_atividade INTEGER,
    #                 nome_atividade TEXT
    #                )
    #                ''') 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            disciplina TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            turno TEXT NOT NULL,
            professor_id INTEGER NOT NULL,
            ativo BOOLEAN NOT NULL,
            FOREIGN KEY (professor_id) REFERENCES professores (id)
        )
    ''')
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    turma_id INTEGER,
                    sala TEXT,
                    data TEXT,
                    hora_inicio TEXT,
                    hora_fim TEXT,
                    FOREIGN KEY (turma_id) REFERENCES Turmas(id)
                   )
                   ''') 
    print("Tabelas criadas com sucesso!")

    
    # Verificar se a tabela professores já possui registros
    cursor.execute("SELECT COUNT(*) FROM professores")
    if cursor.fetchone()[0] == 0:
        professores = [
            ("João Silva", "Matemática"),
            ("Maria Oliveira", "História"),
            ("Carlos Souza", "Física"),
            ("Ana Lima", "Química"),
            ("Fernanda Costa", "Biologia")
        ]
        cursor.executemany("INSERT INTO professores (nome, disciplina) VALUES (?, ?)", professores)

    # Buscar IDs reais dos professores
    cursor.execute("SELECT id FROM professores ORDER BY id")
    professores_ids = [row[0] for row in cursor.fetchall()]

    # Inserir turmas (se não existirem)
    cursor.execute("SELECT COUNT(*) FROM turmas")
    if cursor.fetchone()[0] == 0:
        turmas = [
            ("Turma A", "Manhã", professores_ids[0], True),
            ("Turma B", "Tarde", professores_ids[1], True),
            ("Turma C", "Noite", professores_ids[2], True),
            ("Turma D", "Manhã", professores_ids[3], True),
            ("Turma E", "Tarde", professores_ids[4], True)
        ]
        cursor.executemany("INSERT INTO turmas (nome, turno, professor_id, ativo) VALUES (?, ?, ?, ?)", turmas)



    conexao.commit()
    conexao.close()
    print("Banco de dados inicializado com sucesso!")


class BancoSQLite:
    def __init__(self):
        self.conexao = sqlite3.connect(bd)
        self.conexao.execute("PRAGMA foreign_keys = ON")
        self.conexao.row_factory = sqlite3.Row
        self.cursor = self.conexao.cursor()
        print("Conexão com o banco de dados estabelecida.")

    def close(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")

    def conectar_banco(self):
        return sqlite3.connect(bd)
    
        



