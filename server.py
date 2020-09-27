from flask import Flask, request
import random
import string
import SQLiteUtility as db
import ConnectUtility as ut

app = Flask(__name__)

@app.route('/')
def hello_world():
   json = """
\n{
'id : 1',
'position : 3'
}   
   """
   return f"\nlocalhost:5000/start - to start the game\nlocalhost:5000/play - to play \n\n Expected JSON:\n {json}"

@app.route('/start')
def create_game_id():
   game_id = random.randrange(1,1000)
   return f"READY - Game Id:{game_id}"

@app.route('/play', methods= ['POST'])
def play_game():
   data = request.get_json()
   try:
      game_id = int(data['id'])
      column_number = int(data['position'])
      if column_number >= 0 and column_number <= 7:
         return ut.takeInput(game_id,column_number)
      else: return "Invalid"
   except:
      return "Invalid"

if __name__ == '__main__':
   app.run()