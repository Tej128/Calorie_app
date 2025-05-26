from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Calorie Calculator</title></head>
    <body>
        <h1>Maintenance Calorie Calculator</h1>
        <form action="/api/calculate" method="post">
            Age: <input name="age" /><br/>
            Weight (kg): <input name="weight" /><br/>
            Height (cm): <input name="height" /><br/>
            Gender: <select name="gender"><option>male</option><option>female</option></select><br/>
            <input type="submit" />
        </form>
    </body>
    </html>
    '''

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.form
    age = int(data['age'])
    weight = float(data['weight'])
    height = float(data['height'])
    gender = data['gender'].lower()

    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return jsonify({
        "maintenance_calories": bmr,
        "deficit_calories": bmr - 500,
        "surplus_calories": bmr + 500
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
