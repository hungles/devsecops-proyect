from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "DevSecOps app running"})

@app.route("/api/message", methods=["POST"])
def message():
    payload = request.get_json(silent=True) or {}
    text = payload.get("text", "")
    return jsonify({"received": text, "length": len(text)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
