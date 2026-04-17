from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/tareas")
def inicio():
    tareas = []  
    return render_template("tareas.html", tareas=tareas)


@app.route("/login", methods=["POST"])
def iniciar_sesion():
    return redirect("/index")


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        return redirect("/index")
    
    return render_template("registro.html")


@app.route("/recuperar")
def recuperar():
    return render_template("recuperar.html")


@app.route("/agregar", methods=["POST"])
def agregar():
    return redirect("/tareas")


@app.route("/privacidad")
def privacidad():
    return send_file("static/OrbitRay_Privacidad.docx", as_attachment=True)


@app.route("/terminos")
def terminos():
    return send_file("static/OrbitRay_Terminos.docx", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)