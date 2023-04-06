from flask import Blueprint
from flask_restful import Api
from .resources import ProductResource, ProductItemResource, LivroResource, LivroItemResource, PaginaResource, PaginaItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(ProductResource, "/product/")
api.add_resource(ProductItemResource, "/product/<product_id>")

bp2 = Blueprint("restapi2", __name__, url_prefix="/api/v2")
api2 = Api(bp2)
api2.add_resource(LivroResource, "/livro/")
api2.add_resource(LivroItemResource, "/livro/<livro_id>")

bp3 = Blueprint("restapi3", __name__, url_prefix="/api/v3")
api3 = Api(bp3)
api3.add_resource(PaginaResource, "/pagina/")
api3.add_resource(PaginaItemResource, "/pagina/<pagina_id>")

def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(bp2)
    app.register_blueprint(bp3)
