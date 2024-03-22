from flask import Flask
from routes.authors_route import authors,author 
from routes.books_route import books, book

app = Flask(__name__)

@app.route('/') # this is when you don't include any path
def get_home():
    return '''
        <h1>Welcome to Book's Api Server</h1>
        <p>This is a simple API server for Book's API with following endponts</p>
        <ul>
            <li><a href="/api/authors">Get All Authors</a></li>
            <li><a href="/api/books">Get All Books</a></li>
        </ul>
    '''

app.register_blueprint(authors,url_prefix="/api/authors")
app.register_blueprint(author,url_prefix="/api/author")
app.register_blueprint(books,url_prefix="/api/books")
app.register_blueprint(book,url_prefix="/api/book")


if __name__ == '__main__':
    app.run(debug=True)
    

