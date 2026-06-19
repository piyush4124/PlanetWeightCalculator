from flask import Flask, request

app = Flask(__name__)

gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.53,
    "Saturn": 1.07,
    "Uranus": 0.89,
    "Neptune": 1.14
}

@app.route("/")
def home():
    return """
    <h2>Planet Weight Calculator</h2>
    <form action="/calculate" method="post">
        Earth Weight: <input name="weight" type="number" step="any"><br><br>
        Planet:
        <select name="planet">
            <option>Mercury</option>
            <option>Venus</option>
            <option>Mars</option>
            <option>Jupiter</option>
            <option>Saturn</option>
            <option>Uranus</option>
            <option>Neptune</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    """

@app.route("/calculate", methods=["POST"])
def calculate():
    weight = float(request.form["weight"])
    planet = request.form["planet"]

    result = weight * gravity[planet]

    return f"""
    <h2>Result</h2>
    <p>Your weight on {planet} is <b>{result:.2f}</b></p>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run()
