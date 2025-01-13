from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classic', methods=['POST'])
def classic_bot():
    data = request.json
    response = {"reply": f"Bot reply to: {data.get('text', '')}"}
    return jsonify(response) # jsonify() function in Flask is used to convert a dictionary into a JSON response.

if __name__ == '__main__': # if __name__ == '__main__' is used to execute some code only if the file was run directly, and not imported.
    app.run(debug=True)
