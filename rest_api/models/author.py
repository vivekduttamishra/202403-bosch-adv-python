class AuthorManager:
    def __init__(self):
        self.authors={} # author collection
        self.seed_authors()

    def seed_authors(self):
        self.add_author(dict(id='vivek-dutta-mishra', name='Vivek Dutta Mishra',biography='The Author of The Lost Epic series and Manas', photograph='vivek.jpg', tags=['epic','indian','english','best-seller']))
        self.add_author(dict(id='mahatma-gandhi', name='Mahatma Gandhi',biography='The father of the nation for India', photograph='gandhi.jpg', tags=['leader','indian','english','best-seller']))
        self.add_author(dict(id='ramdhari-singh-dinkar', name='Ramdhari Sing Dinkar',biography='National Poet of India', photograph='dinkar.jpg', tags=['poetry','essays','indian','hindi']))
        self.add_author(dict(id='jeffrey-archer', name='Jeffrey Archer',biography='Leading bestseller in English Fiction', photograph='archer.jpg', tags=['fiction','british','english','best-seller']))
        self.add_author(dict(id='john-grisham', name='John Grisham',biography='Leading best seller of Legal Fiction', photograph='grisham.jpg', tags=['legal-fiction','USA','english','best-seller']))
        self.add_author(dict(id='jkrowling', name='JK Rowling',biography='The author of Harry Potter', photograph='jkr.jpg', tags=['harry-potter','british','english','best-seller']))

    def _validate_author(self,author):
        return True

    def add_author(self, author): #author is a dictionary
        self._validate_author(author)
        self.authors[author['id']] = author
        return author

    def get_all(self):
        return [author for author in self.authors.values()]
    
    def get_by_id(self, author_id):
        return self.authors.get(author_id)
    
    def remove_author(self, id):
        del self.author[id]

    def update_author(self,id, author):
        old=self.authors[id]
        self.authors[id]=author
        return author
    
#this is the singleton instance of authorManager that we will use
authorManager=AuthorManager()