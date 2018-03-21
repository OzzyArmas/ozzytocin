from flask import Flask
app = Flask(__name__)

@app.route("/")
def landing():
  return """
      <h> Hellow World! </h>
      """
if __name__ == "__main__":
    app.run()
