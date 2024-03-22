import time
import json
import os

db_name="authors.json"


def make_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class AuthorManager:
    def __init__(self):
        self.authors={} # author collection
        self._load_db()


    def _load_db(self):
        if os.path.exists(db_name):
            with open(db_name) as f:
                self.authors=json.load(f)
            print(f'Loaded {len(self.authors)} records from database')
        else:
            self._seed_authors()
            self._save()
            print(f'Created and seeded new database with {len(self.authors)} records')

    def _save(self):
        with open(db_name, 'w') as f:
            json.dump(self.authors, f,indent=3)


    def _seed_authors(self):
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
        author['meta']=dict(created=make_time_str())
        if 'id' not in author:
            author['id']= '-'.join(author['name'].lower().split())

        self.authors[author['id']] = author
        self._save()
        return author

    def get_all(self):
        return [author for author in self.authors.values()]
    
    def get_by_id(self, author_id):

        return self.authors[author_id] # raises KeyError
    
    def remove_author(self, id):
        del self.authors[id]
        self._save()

    def update_author(self,id, author):
        old=self.authors[id]
        
        for k,v in author.items():
            old[k]=v

        old["meta"]["updated"]=make_time_str()
        self._save()
        return old
    
#this is the singleton instance of authorManager that we will use
authorManager=AuthorManager()