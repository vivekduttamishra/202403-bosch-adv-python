from flask import Blueprint

books=Blueprint('books',__name__)
book=Blueprint('book',__name__)


@books.route('/')
def get_all_books():
    return "Get All books"

@books.route('/', methods=['POST'])
def add_book():
    return "Adding New book"


@book.route('/<id>')
def get_book_by_id(id):
    return f'get book by {id=}'



@book.route('/<id>',methods=['PUT','PATCH'])
def update_book(id):
    return f'update book by {id=}'

@book.route('/<id>',methods=['DELETE'])
def delete_book(id):
    return f'update book by {id=}'



