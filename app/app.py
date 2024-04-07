from flask import Flask, render_template, request, jsonify

try:
    from app.bmi_calculator import calculate_bmi, categorize_bmi
except ImportError:
    from bmi_calculator import calculate_bmi, categorize_bmi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    height = float(data.get('height'))
    weight = float(data.get('weight'))

    bmi = round(calculate_bmi(height, weight), 2)
    category = categorize_bmi(bmi)
    return jsonify({'bmi': bmi, 'category': category})


if __name__ == '__main__':
    app.run(host='localhost', debug=True)