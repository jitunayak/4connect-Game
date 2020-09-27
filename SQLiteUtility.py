import sqlite3
from sqlite3 import Error
import random
import string

cursor = None
conn = None


def get_random_string():
    length = 10
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_connection(db_file):
    global  conn
    try:
        conn = sqlite3.connect(db_file)
        global cursor
        cursor = conn.cursor()
        #print("Using ",sqlite3.version)
    except Error as e:
        print(e)

def createTable():
    cursor.execute("""
    CREATE TABLE gamehistory(
    game_no INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    history_player1 TEXT,
    history_player2 TEXT
    )
    """)

def createNewGame(game_id, player1_action, player2_action):
    player1_actions = listToString(player1_action)
    player2_actions =  listToString(player2_action)
    cursor.execute("INSERT INTO gamehistory (game_id, history_player1, history_player2) VALUES ( ?, ?, ?)",
            (game_id,player1_actions, player2_actions))
    conn.commit()
    cursor.execute("SELECT * FROM gamehistory")
    s = cursor.fetchall()

# def VerifGamePlay(game_id, player1_action, player2_action ):
#     player1_actions = listToString(player1_action)
#     player2_actions = listToString(player2_action)
#     cursor.execute(f"UPDATE gamehistory SET history_player1={player1_actions}, history_player2={player2_action} WHERE game_id={game_id}")

def listToString(s):
    str1 = " "
    return (str1.join(str(s)))

def init():
    try:
        create_connection(r"./connectGame.db")
        createTable()
    except:
        #insertData([1,2,3,5],[1,2,2,4])
        create_connection(r"./connectGame.db")
        conn.commit()
        cursor.execute("SELECT * FROM gamehistory")
        s =cursor.fetchall()
        print(s)

if __name__ == '__main__':
    init()