from flask import Blueprint
from .views import index, product, livro, pagina

bp = Blueprint("webui", __name__, template_folder="templates",
    url_prefix="/"
)

bp.add_url_rule('/', view_func=index)
bp.add_url_rule(
    "/product/<product_id>", view_func=product, endpoint="productview"
)
bp.add_url_rule(
    "/livro/<livro_id>", view_func=livro, endpoint="livroview"
)
bp.add_url_rule(
    "/pagina/<pagina_id>", view_func=pagina, endpoint="paginaview"
)
bp.add_url_rule(
    "/admin/", view_func=pagina, endpoint="adminview"
)

def init_app(app):
    app.register_blueprint(bp)
