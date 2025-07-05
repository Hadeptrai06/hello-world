from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép truy cập từ frontend

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({'sum': a + b})

if __name__ == '__main__':
    app.run(debug=True)