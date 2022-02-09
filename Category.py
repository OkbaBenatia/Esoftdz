import datetime  # To use time lib


class Category:
    '''this class for Category'''

    create_at = datetime.datetime.now()  # category create date
    update_at = None  # category update date

    def __init__(self, name):
        '''allow to create object automatically'''
        self.name = name
