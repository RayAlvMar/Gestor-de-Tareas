from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)

usuarios = ["ray@gmail.com", "yo@gmail.com"]
contrasenas = ["123456", "rayy123"]

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
    email = request.form["email"]
    password = request.form["password"]

    if email in usuarios:
        i = usuarios.index(email)

        if contrasenas[i] == password:
            return redirect("/index")
        else:
            return render_template("login.html", error="Contraseña incorrecta")
    else:
        return render_template("login.html", error="El usuario no existe")


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