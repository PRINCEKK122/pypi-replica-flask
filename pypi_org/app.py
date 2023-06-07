import flask

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views.home_views import blueprint as home
    from views.package_views import blueprint as packages
    app.register_blueprint(home)
    app.register_blueprint(packages)


if __name__ == "__main__":
    main()
