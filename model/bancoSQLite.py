import sqlite3
import sys
import os
import requests 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from config import banco_de_dados as bd


def importar_professores_da_api():
    url = "http://localhost:5000/api/professores"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        professores = resposta.json()

        conexao = sqlite3.connect(bd)
        cursor = conexao.cursor()

        for prof in professores:
            cursor.execute(
                "INSERT OR IGNORE INTO professores (id, nome, disciplina) VALUES (?, ?, ?)",
                (prof["id"], prof["nome"], prof["disciplina"])
            )
        
        conexao.commit()
        conexao.close()
        print("Professores importados com sucesso!")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")

import requests
import sqlite3
from config import banco_de_dados as bd

def importar_turmas_da_api():
    url = "http://localhost:5000/api/turma"  # endpoint exato da API

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na resposta
        turmas = resposta.json()

        conexao = sqlite3.connect(bd)
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        for turma in turmas:
            cursor.execute("""
                INSERT OR IGNORE INTO turmas (id, nome, turno, professor_id, ativo)
                VALUES (?, ?, ?, ?, ?)
            """, (
                turma["id"],
                turma["nome"],
                turma["turno"],
                turma["professor_id"],
                turma["ativo"]
            ))

        conexao.commit()
        conexao.close()
        print("Turmas importadas com sucesso!")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar API de turmas: {e}")


def inicializar_banco():
    conexao = sqlite3.connect(bd)
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor() 
    print("Conexão com o banco de dados estabelecida.")
   
    # Criação das tabelas
   

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
    
        



