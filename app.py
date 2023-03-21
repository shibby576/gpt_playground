import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data = request.form["data"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(data),
            temperature=0.79,
            max_tokens = 250
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(data):
    return """What are the trends in this data? 
    
    {}""".format(
        data.capitalize()
    )
