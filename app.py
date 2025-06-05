from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='10.0.0.53', port=8000)
