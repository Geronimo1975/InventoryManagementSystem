from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    data = request.json
    response = {"message": f"Received: {data.get('text', '')}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
