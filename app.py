from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook : ",data["body"])

    if data["body"]["object"] == "page":
        return "EVENT_RECEIVED", 200
    
    else:
        return "", 404
