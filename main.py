from flask import Flask, render_template, request, redirect, url_for
from hangiman import HangimanGame
import os

app = Flask(__name__)

game = HangimanGame()  # Global game instance

def get_game():
    return game

def save_game(new_game):
    game = new_game

@app.route('/', methods=['GET'])
def index():
    state = game.get_state()
    return render_template('index.html', **state)

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.form.get('letter', '').strip()
    game.guess(letter)
    return redirect(url_for('index'))

@app.route('/new')
def new():
    global game
    game = HangimanGame()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)