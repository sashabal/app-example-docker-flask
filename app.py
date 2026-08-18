from flask import Flask

app = Flask(__name__)

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
    app.run(debug=True, host='0.0.0.0', port=port)
