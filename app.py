from boggle import Boggle
boggle_game = Boggle()

from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

# Need to manually create HTML templates folder and tell Flask to render from it
app = Flask(__name__,template_folder='templates')

app.debug = True
# Debug Toolbar Requirement
app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def show_board():
    board = boggle_game.make_board()
    session['board'] = board

    return render_template('boggle.html', board=board)

@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})