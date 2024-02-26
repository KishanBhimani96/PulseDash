from flask import Flask, render_template, jsonify, request
import psutil
from threading import Thread
import time

app = Flask(__name__)

def get_system_metrics():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
    }

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page with JavaScript

@app.route('/metrics')
def metrics():
    return jsonify(get_system_metrics())

if __name__ == '__main__':
    app.run(debug=True, port=8000)
 