from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_bmi():
    name = request.form["name"]
    age = request.form["age"]
    height = float(request.form["height"])
    weight = float(request.form["weight"])

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"""
    <h1>Hello, {name}!</h1>
    <p>Age: {age}</p>
    <p>Your BMI is: {bmi:.2f}</p>
    <p>You are classified as: {category}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
