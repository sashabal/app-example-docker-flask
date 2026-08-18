from flask import Flask, jsonify
import os
import uuid
import getpass

app = Flask(__name__)

@app.route("/")
def hello():
    return "test flask app"

@app.route("/health")
def health():
    return "ok"

@app.route("/info")
def info():
    mac = str(uuid.getnode())
    user = getpass.getuser()
    mid = ""
    for f in ["/etc/machine-id", "/proc/sys/kernel/random/boot_id"]:
        try:
            mid = open(f).read().strip()
            break
        except:
            pass
    eth0 = ""
    try:
        eth0 = open("/sys/class/net/eth0/address").read().strip()
    except:
        pass
    return jsonify(mac=mac, mac_hex=eth0, user=user, machine_id=mid,
                   flask_path=os.path.dirname(__import__('flask').__file__))

@app.route("/test")
def test_route():
    data = {"key": "value"}
    result = data["nonexistent_key"]
    return result

if __name__ == "__main__":
    port = 3478
    app.run(debug=True, host='0.0.0.0', port=port)
