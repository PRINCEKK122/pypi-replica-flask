import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    test_packages =[
        "package1",
        "package2",
        "package3"
    ]
    return flask.render_template("index.html", packages=test_packages)


if __name__ == "__main__":
    app.run(debug=True)
