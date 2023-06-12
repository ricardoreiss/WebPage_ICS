from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/home.html")
def index():
	return render_template("home.html")

@app.route("/profissoes.html")
def profissoes():
	return render_template("profissoes.html")

@app.route("/objetivos.html")
def objetivos():
	return render_template("objetivos.html")

@app.route("/mercado.html")
def mercado():
	return render_template("mercado.html")

@app.route("/universidades.html")
def universidades():
	return render_template("universidades.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)