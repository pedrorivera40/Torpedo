from flask import Flask, request, jsonify

# Initializing app.
app = Flask(__name__)

# Routes definition.

# Mock route just for testing purposes.
@app.route("/hello/", methods=['GET'])
def hello_world():
	return jsonify(MSG="Hello World!!!"), 200


# Launch app.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
