from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return """
    <html>
    <head><title>Medicine Management</title></head>
    <body>
        <h1>Welcome to the Medicine Management Website!</h1>
        <p>This platform will help you manage your medicines efficiently.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
