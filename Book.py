import datetime


class Book:
    '''book class'''

    create_at = datetime.datetime.now()  # book create date
    update_at = None  # book update date

    def __init__(self, name, version, numpage, abstract, yearpublish, numviews,
                 language, picture, path, author_id, category_id):
        '''allow to create object automatically'''
        
        self.name = name
        self.version = version
        self.numpage = numpage
        self.abstract = abstract
        self.yearpublish = yearpublish
        self.numviews = numviews
        self.language = language
        self.picture = picture
        self.path = path
        self.category_id = category_id
        self.author_id = author_id
