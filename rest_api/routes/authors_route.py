from flask import Blueprint,jsonify, request
from models.author import authorManager
from utils import error_mapper

authors=Blueprint('authors',__name__)
author=Blueprint('author',__name__)

@authors.route('/')
def get_all_authors():
    return jsonify(authorManager.get_all()) #by defaul 200

@authors.route('/', methods=['POST'])
def add_author():
    print(f'{request.json=}')
    author=request.json
    author=authorManager.add_author(author)
    return jsonify(author),201 #status code


@author.route('/<id>')
@error_mapper(KeyError, message="Author Not Found")
def get_author_by_id(id):
    a= authorManager.get_by_id(id)
    return jsonify(authorManager.get_by_id(id))
    

@author.route('/<id>',methods=['PUT','PATCH'])
@error_mapper(KeyError, message="Author Not Found")
def update_author(id):
    author=request.json
    author =authorManager.update_author(id,author)
    return jsonify(author), 202

# @author.route('/<id>',methods=['DELETE'])
# def delete_author(id):
#     try:
#         authorManager.remove_author(id)
#         #return dict(status="deleted successfully", id=id)
#         return jsonify(None), 204
#     except KeyError as e:
#         return jsonify(dict(error=f'author {id} not found',id=id)), 404

@author.route('/<id>',methods=['DELETE'])
@error_mapper(KeyError, message="Author Not Found")
def delete_author(id):
    authorManager.remove_author(id)
    #return dict(status="deleted successfully", id=id)
    return jsonify(None), 204



#@author.route('/<id>/books')
def get_books_by_author(id):    
    return f'get books by author {id=}'
