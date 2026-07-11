from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    student = {
        "Name": request.form["name"],
        "Age": request.form["age"],
        "Department": request.form["dept"]
    }
    students.append(student)
    return redirect("/view")

@app.route("/view")
def view():
    return render_template("view.html", students=students)

@app.route("/delete/<name>")
def delete(name):
    global students
    students = [s for s in students if s["Name"] != name]
    return redirect("/view")

@app.route("/search", methods=["POST"])
def search():
    name = request.form["name"]
    result = [s for s in students if s["Name"].lower() == name.lower()]
    return render_template("view.html", students=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)