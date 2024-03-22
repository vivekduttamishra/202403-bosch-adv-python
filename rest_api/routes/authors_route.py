from flask import Blueprint,jsonify
from models.author import authorManager

authors=Blueprint('authors',__name__)
author=Blueprint('author',__name__)

@authors.route('/')
def get_all_authors():
    return jsonify(authorManager.get_all())

@authors.route('/', methods=['POST'])
def add_author():
    return "Adding New Author"


@author.route('/<id>')
def get_author_by_id(id):
    return jsonify(authorManager.get_by_id(id))

#@author.route('/<id>/books')
def get_books_by_author(id):
    return f'get books by author {id=}'

@author.route('/<id>',methods=['PUT','PATCH'])
def update_author(id):
    return f'update author by {id=}'

@author.route('/<id>',methods=['DELETE'])
def delete_author(id):
    authorManager.remove_author(id)
    return {"success": "Author Deleted", "id":id}



