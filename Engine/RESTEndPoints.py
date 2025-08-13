from flask import Flask, jsonify, request

app = Flask(__name__)

def listen_for_requests():
    app.run(debug = True)

@app.route("/status", methods = ["GET"])
def get_status():
    return jsonify({"Terveys": "Hyvä!"})

@app.route("/setup", methods = ["POST"])
def setup():
    print("POST:", request.json["initialCells"])
    return jsonify({"Postattiin": "..."})