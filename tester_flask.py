from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, World!, {escape(name)}</p>"
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)