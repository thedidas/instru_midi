# ✅ Monkey patch FIRST!
import eventlet
eventlet.monkey_patch()

from flask import Flask, request
from flask_socketio import SocketIO
from flask import render_template

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received from STM32:", data)
    socketio.emit('sensor_data', data)  # Broadcast to connected clients
    return {"status": "success"}

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)
