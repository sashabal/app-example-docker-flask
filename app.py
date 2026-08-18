from flask import Flask, jsonify
import os

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "test flask app"

@app.route("/health")
def health():
    return "ok"

@app.route("/test")
def test_route():
    data = {"key": "value"}
    result = data["nonexistent_key"]
    return result

if __name__ == "__main__":
    port = 3478
    from werkzeug.debug import DebuggedApplication
    debugged = DebuggedApplication(app, evalex=True, pin_security=False)
    debugged.trusted_hosts = []
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', port, debugged, use_reloader=True)
