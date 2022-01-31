import datetime # To use time lib

class Category:
    '''this class for Category'''

    create_at = datetime.datetime.now() #To know when the category was created
    update_at = None #To know if we did any update was done

#The fontion __init__ to give a name to a category, it will be created automatically with the creation of any obj and it take name as attribute
    def __init__(self,name): 
        self.name = name
