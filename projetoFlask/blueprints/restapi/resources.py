from flask import jsonify, abort
from flask_restful import Resource
from projetoFlask.ext.database import Product
from projetoFlask.ext.database import Livro
from projetoFlask.ext.database import Pagina

class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {'products':[ 
                {
                    'id':product.id,
                    'name':product.name,
                    'description':product.description,
                    'price':product.price,
                    'type': product.type.description
                }
                for product in products
            ]}
        )

class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(
            404
        )
        
        return jsonify(product.to_dict())


class LivroResource(Resource):
    def get(self):
        livros = Livro.query.all() or abort(204)
        return jsonify(
            {'livros':[
                {
                    'id':livro.id,
                    'name':livro.name,
                    'description':livro.description,
                    'image_url':livro.image_url,
                }
                for livro in livros
            ]}
        )

class LivroItemResource(Resource):
    def get(self, livro_id):
        livro = Livro.query.filter_by(id=livro_id).first() or abort(
            404
        )

        return jsonify(livro.to_dict())

class PaginaResource(Resource):
    def get(self):
        paginas = Pagina.query.all() or abort(204)
        return jsonify(
            {'paginas':[
                {
                    'id':pagina.id,
                    'number':pagina.number,
                    'content':pagina.content,
                    'livro_id':pagina.livro_id,
                }
                for pagina in paginas
            ]}
        )

class PaginaItemResource(Resource):
    def get(self, pagina_id):
        pagina = Pagina.query.filter_by(id=pagina_id).first() or abort(
            404
        )

        return jsonify(pagina.to_dict())
