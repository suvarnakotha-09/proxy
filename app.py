from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.headers.get("X-Real-IP", request.remote_addr)
    return f"Hello from the Python backend!\nI saw client IP: {ip}\n"

app.run(host="127.0.0.1", port=5000)
