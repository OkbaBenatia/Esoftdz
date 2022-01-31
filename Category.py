import datetime



class Category:
    '''this class for Category'''

    create_at = datetime.datetime.now()
    update_at = None
    
    def __init__(self,name):
        self.name = name
