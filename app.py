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

def page(title, content):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: white;
                color: black;
                padding: 30px;
                border-radius: 15px;
                width: 320px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                text-align: center;
            }}
            h2 {{
                margin-bottom: 20px;
            }}
            input, select {{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
            }}
            button {{
                width: 100%;
                padding: 10px;
                background: #2a5298;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }}
            button:hover {{
                background: #1e3c72;
            }}
            a {{
                display: inline-block;
                margin-top: 15px;
                color: #2a5298;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """

@app.route("/")
def home():
    content = """
    <h2>🌍 Planet Weight Calculator</h2>
    <form action="/calculate" method="post">
        <input name="weight" type="number" step="any" placeholder="Enter Earth weight" required>

        <select name="planet">
            <option>Mercury</option>
            <option>Venus</option>
            <option>Mars</option>
            <option>Jupiter</option>
            <option>Saturn</option>
            <option>Uranus</option>
            <option>Neptune</option>
        </select>

        <button type="submit">Calculate</button>
    </form>
    """
    return page("Home", content)

@app.route("/calculate", methods=["POST"])
def calculate():
    weight = float(request.form["weight"])
    planet = request.form["planet"]

    result = weight * gravity[planet]

    content = f"""
    <h2>✨ Result</h2>
    <p>Your weight on <b>{planet}</b> is:</p>
    <h1>{result:.2f}</h1>
    <a href="/">← Try Again</a>
    """
    return page("Result", content)

if __name__ == "__main__":
    app.run()
