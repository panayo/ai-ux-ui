from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/', methods=['POST'])



if __name__ == '__main__':
    app.run(port=6000, debug=True)