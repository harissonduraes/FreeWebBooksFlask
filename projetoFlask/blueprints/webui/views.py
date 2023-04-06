from flask import abort, render_template
from projetoFlask.ext.database import Product
from projetoFlask.ext.database import Livro
from projetoFlask.ext.database import Pagina
from flask import request

def index():
    products = Product.query.all()
    livros = Livro.query.all()
    paginas = Pagina.query.all()
    return render_template("index.html", products=products, livros=livros, paginas=paginas)

def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)

def livro(livro_id):
    livro = Livro.query.filter_by(id=livro_id).first() or abort(
        404, "livro nao encontrado"
    )
    paginas = Pagina.query.filter_by(id_livro=livro_id).all() or abort(
        404, "produto nao encontrado"
    )
    pagina_atual = request.args.get("pagina_atual", default=1, type=int)
    pagina_anterior = max(1, pagina_atual - 1)
    pagina_seguinte = min(len(paginas), pagina_atual + 1)
    return render_template("livro.html", livro=livro, paginas=paginas, pagina_atual=pagina_atual, pagina_anterior=pagina_anterior, pagina_seguinte=pagina_seguinte)

def pagina(pagina_id):
    paginas = Pagina.query.filter_by(id=pagina_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("livro.html", paginas=paginas)
