from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classic', methods=['POST'])
def classic_bot():
    data = request.json
    response = {"reply": f"Bot reply to: {data.get('text', '')}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
