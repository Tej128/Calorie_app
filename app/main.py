from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        gender = request.form["gender"]

        if gender == "male":
            s = 5
        else:
            s = -161

        bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
        maintenance = bmr * 1.2
        deficit = maintenance * 0.8
        surplus = maintenance * 1.2

        result = {
            "bmr": round(bmr, 2),
            "maintenance": round(maintenance, 2),
            "deficit": round(deficit, 2),
            "surplus": round(surplus, 2)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
