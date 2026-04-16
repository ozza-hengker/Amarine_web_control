# Install dulu library-nya: 
# pip install flask flask-socketio paramiko eventlet

import eventlet
eventlet.monkey_patch() # Wajib untuk background task web socket

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import paramiko
import threading
import time

app = Flask(__name__, template_folder='.') # Baca index.html di folder yang sama
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# === KONFIGURASI JETSON ===
JETSON_IP = '192.168.2.2' # Ganti dengan IP Jetson / ubuntu.local
JETSON_USER = 'amarine'
JETSON_PASS = '123890' # Ganti dengan password aslinya

# Simpan state SSH channels
active_sessions = {}

def ssh_reader_thread(process_id, stdout, channel):
    """Membaca output dari Jetson secara terus-menerus dan mengirim ke web"""
    while not channel.exit_status_ready():
        if channel.recv_ready():
            # Baca per baris (atau per byte) dari terminal
            line = channel.recv(1024).decode('utf-8')
            if line:
                socketio.emit('terminal_output', {'id': process_id, 'text': line.strip()})
        eventlet.sleep(0.1) # Cegah CPU 100%

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_process')
def handle_start(data):
    process_id = data.get('id')
    target_val = data.get('target') # Hasil dari dropdown (misal: 'qual', 'build')
    
    # 1. Tentukan Command berdasarkan ID dan Target Dropdown
    command = "echo 'Command belum disetting'"
    if process_id == 'gazebo':
        command = f"echo 'Starting Gazebo {target_val}...' && sleep 2 && ping 8.8.8.8" # CONTOH! Ganti command ROS2 aslinya
    elif process_id == 'sitl':
        command = "echo 'Starting SITL...' && top -b -n 5" # CONTOH command
    # Tambahkan elif untuk ros1, ros2, dsb...

    socketio.emit('terminal_output', {'id': process_id, 'text': f"[BACKEND] Menyambungkan SSH ke {JETSON_IP}..."})
    
    try:
        # Buka koneksi SSH baru untuk setiap proses
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(JETSON_IP, username=JETSON_USER, password=JETSON_PASS, timeout=5)
        
        # Eksekusi command dengan get_pty=True agar bisa dikirim Ctrl+C nanti
        stdin, stdout, stderr = client.exec_command(command, get_pty=True)
        channel = stdout.channel
        
        active_sessions[process_id] = {'client': client, 'channel': channel}
        
        # Mulai thread untuk membaca output secara real-time
        socketio.start_background_task(ssh_reader_thread, process_id, stdout, channel)
        socketio.emit('terminal_output', {'id': process_id, 'text': f"[BACKEND] Eksekusi: {command}"})

    except Exception as e:
        socketio.emit('terminal_output', {'id': process_id, 'text': f"[ERROR] SSH Gagal: {str(e)}", 'is_error': True})

@socketio.on('kill_process')
def handle_kill(data):
    process_id = data.get('id')
    if process_id in active_sessions:
        session = active_sessions[process_id]
        channel = session['channel']
        client = session['client']
        
        try:
            # Kirim sinyal Ctrl+C (SIGINT) ke terminal Jetson
            channel.send('\x03')
            time.sleep(1)
            client.close()
            socketio.emit('terminal_output', {'id': process_id, 'text': f"[BACKEND] Proses {process_id} dimatikan paksa (SIGINT).", 'is_error': True})
        except Exception as e:
            print("Error saat kill:", e)
        
        del active_sessions[process_id]

if __name__ == '__main__':
    print("🚀 GCS Backend Menyala! Buka http://127.0.0.1:5000 di browser.")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
