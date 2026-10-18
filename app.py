
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>CI/CD Project</title></head>
      <body style="font-family:Arial;text-align:center;margin-top:100px">
        <h1>CI/CD Pipeline Successful!</h1>
        <h2>GitHub Actions + Docker</h2>
        <p>Application deployed locally.</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

