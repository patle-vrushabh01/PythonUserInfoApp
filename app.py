from flask import Flask, redirect
from flasgger import Swagger
from api.routes import api as api_routes
from api.errors import errors as api_errors
from config.swagger import SWAGGER_CONFIG





def create_app():
    app = Flask(__name__)
    app.config['TRAP_HTTP_EXCEPTIONS'] = True
    app.config['SWAGGER'] = SWAGGER_CONFIG
    Swagger(app)

    # Base Route
    @app.route('/')
    def base_route():
        return redirect("/apidocs/", code=302)

    app.register_blueprint(api_routes, url_prefix='/api')
    app.register_blueprint(api_errors)


    return app


if __name__ == '__main__':

    app = create_app()
    app.debug=True
    app.run(host='0.0.0.0', port=5000)