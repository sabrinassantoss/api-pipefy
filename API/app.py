from flask import Flask, jsonify, request

import services

app = Flask(__name__)

PIPE_ID = "303843596"
PIPEFY_URL = "https://api.pipefy.com/graphql"
PIPEFY_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MDQyMDIzOTMsImp0aSI6IjAyZmI0MGFmLWYwNGQtNGNjMi05Yjc4LWJkZmQ5YzhhZWM4NCIsInN1YiI6MzA0MTY1MTY2LCJ1c2VyIjp7ImlkIjozMDQxNjUxNjYsImVtYWlsIjoiZGVzYWZpb2ludGVncmFjYW9AcHJvZmVjdHVtLmNvbS5iciIsImFwcGxpY2F0aW9uIjozMDAzMDU3MDEsInNjb3BlcyI6W119LCJpbnRlcmZhY2VfdXVpZCI6bnVsbH0.NDCy-EvEyaQpct5lEeaXRdCCWCuU4K-DRggf2wdZIsVMo8tIwk0kY7bPVPnngajjULE_hF-O0rqqydkyzJiNBA"
PIPEFY_HEADER = {
    "authorization": "Bearer " + PIPEFY_TOKEN,
    "Content-Type": "application/json"
}
 
@app.route("/", methods=["GET"])
def index():
    output = {"status": "Active"}

    return jsonify(output)

@app.route("/cards", methods=["GET"])
def list_cards():

    response = services.list_cards(PIPE_ID, PIPEFY_URL, PIPEFY_HEADER)

    return jsonify(response)

@app.route("/create/card", methods=["POST"])
def create_card():

    client_data = request.get_json()
    response = services.create_card(PIPE_ID, PIPEFY_URL, PIPEFY_HEADER, client_data)

    return jsonify(response)

@app.route("/delete/card/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):

    response = services.delete_card(PIPEFY_URL, PIPEFY_HEADER, card_id)

    return jsonify(response)

@app.route("/update/phase/card/<int:card_id>", methods=["PUT"])
def update_phase_card(card_id):

    client_data = request.get_json()
    response = services.update_phase_card(PIPEFY_URL, PIPEFY_HEADER, card_id, client_data["phase"].lower())

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
