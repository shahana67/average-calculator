from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-average', methods=['POST'])
def calculate_average():
    data = request.json
    if not data or 'numbers' not in data:
        return jsonify({'error': 'No data provided or missing "numbers" field'}), 400
    
    numbers = data['numbers']
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'All elements in "numbers" must be int or float'}), 400
    
    if not numbers:
        return jsonify({'error': '"numbers" array is empty'}), 400

    average = sum(numbers) / len(numbers)
    return jsonify({'average': average})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
