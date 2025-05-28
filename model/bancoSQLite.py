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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disciplinas (
            id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            alunos TEXT NOT NULL,         -- IDs dos alunos, ex: "1,2,3"
            professores TEXT NOT NULL,    -- IDs dos professores, ex: "1,2"
            publica BOOLEAN NOT NULL
        )
    ''')
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS SALAS (
                    ID_SALA INTEGER PRIMARY KEY AUTOINCREMENT,
                    AGENDADAS BOOLEAN NOT NULL DEFAULT 0,
                    id_turma INTEGER,
                    nome_turma TEXT,
                    id_professor INTEGER,
                    nome_professor TEXT, 
                    id_aluno INTEGER,
                    nome_aluno TEXT,
                    id_atividade INTEGER,
                    nome_atividade TEXT
                   )
                   ''') 
    
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    turma_id INTEGER,
                    sala TEXT,
                    hora_inicio TEXT,
                    hora_fim TEXT,
                    FOREIGN KEY (turma_id) REFERENCES Turmas(id)
                   )
                   ''') 
    print("Tabelas criadas com sucesso!")
    
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
    
        



