from flask import Flask, flash, render_template, request, redirect, send_file, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "rayos_de_orbita"

client = MongoClient("mongodb://localhost:27017/")
db = client["gestor_tareas"]
usuarios_collection = db["usuarios"]

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    usuario = usuarios_collection.find_one({
        "email": email,
        "password": password
    })

    if usuario:
        session["usuario"] = email
        flash("Inicio de sesión exitoso")
        return redirect("/index")
    else:
        flash("Correo o contraseña incorrectos")
        return redirect("/login")


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("password")
        edad = request.form.get("edad")
        genero = request.form.get("genero")

        usuario_existente = usuarios_collection.find_one({"email": email})

        if usuario_existente:
            flash("El usuario ya existe")
            return redirect("/registrar")

        usuarios_collection.insert_one({
            "nombre": nombre,
            "email": email,
            "password": password,
            "edad": edad,
            "genero": genero
        })

        session["usuario"] = email
        return redirect("/index")
    
    return render_template("registro.html")


@app.route("/index")
def index():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("index.html")


@app.route("/tareas")
def inicio():
    if "usuario" not in session:
        return redirect("/login")

    tareas = []
    return render_template("tareas.html", tareas=tareas)


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