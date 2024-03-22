from flask import Flask

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

@app.route("/api/authors")
def get_author_list():
    return "Get a List of All Authors"

@app.route("/api/books")
def get_book_list():
    return "Get a List of All Books"

@app.route("/api/authors/<author_id>")
def get_author_by_Id(author_id):
    return f'getting author by {author_id=}'

@app.route("/api/authors/<author_id>/books")
def get_books_by_author(author_id):
    return f'getting books by {author_id=}'


@app.route("/api/authors",methods=["POST"])
def add_author():
    return "Adding new Author Author"


@app.route("/api/authors/<author_id>",methods=['PUT','PATCH'])
def update_author(author_id):
    return f'getting books by {author_id=}'

@app.route("/api/authors/delete/<author_id>",methods=['DELETE'])
def delete_author(author_id):
    return f'Deleting Author {author_id=}'


if __name__ == '__main__':
    app.run(debug=True)


