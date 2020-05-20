import requests as r
import sqlite3


def cadastrar_time(team_name):
    body = get_team(team_name['nome'])
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    ddl_sql = """
    CREATE TABLE IF NOT EXISTS TIME(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME VARCHAR(100),
        PAIS VARCHAR(50),
        FUNDACAO INT,
        ESTADIO VARCHAR(255),
        CAPACIDADE INT
    )

    """
    cursor.execute(ddl_sql)
    connection.commit()


    dml_insert_sql = """
    INSERT INTO TIME(NOME, PAIS, FUNDACAO, ESTADIO, CAPACIDADE)
    VALUES(?, ?, ?, ?, ?)
    """

    cursor.execute(dml_insert_sql, [body['team']['name'], body['team']['country'], 
                   body['team']['founded'], body['venue']['name'], body['venue']['capacity']])
    connection.commit()
    connection.close()
    return "Time escolhido com sucesso!!"


def get_team(team_name):
    url = f"https://api-football-beta.p.rapidapi.com/teams?name={team_name}"

    headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "370ba1b368msh3d4b495ab10e060p1cd375jsn03d308d545b2"
    }

    response = r.get(url, headers=headers).json()
    return response['response'][0]


def select_time_favorito(time):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    ddl_sql = """
    SELECT NOME, PAIS, FUNDACAO, ESTADIO, CAPACIDADE FROM TIME
    WHERE NOME = ?
    """
    cursor.execute(ddl_sql, [time])
    time = cursor.fetchone()
    dic_time = {
        "nome": time[0],
        "pais": time[1],
        "fundacao": time[2],
        "estadio": time[3],
        "capacidade": time[4]
    }
    connection.commit()
    connection.close()
    return dic_time


def deletar_time_favorito(time):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    ddl_sql = """
    DELETE FROM TIME
    WHERE NOME = ?
    """
    cursor.execute(ddl_sql, [time['nome']])
    connection.commit()
    connection.close()
    return "Time Excluído com Sucesso"