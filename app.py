from flask import Flask
app = Flask(name)
@app.route('/')
def hello():
    return "<h1>Hello World- Static website by mukesh bala </h1>"
if name == 'main':
    app.run()
