import flask
from services.package_service import get_latest_packages

blueprint = flask.Blueprint("packages", __name__)

@blueprint.route("/project/<package_name>")
def package_details(package_name):
    package_results = "Package details for {}".format(package_name)
    return flask.render_template("packages/details.html", package=package_results)
