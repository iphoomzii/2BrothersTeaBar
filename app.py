from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='template')

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, nameList = ['A', 'B', 'C'])

# @app.route("/<name>")
# def user(name):
#     return f"hello {name}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))

if __name__ == "__mian__":
    app.run(host='localhost', port=5000, debug=True)
