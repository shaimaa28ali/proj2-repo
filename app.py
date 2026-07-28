from flask import Flask, render_template, request
from planner_graph import planner

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        tasks = request.form["tasks"]

        result = planner.invoke({
            "tasks": tasks,
            "summary": "",
            "category": "",
            "priority": "",
            "smart_plan": ""
        })

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)