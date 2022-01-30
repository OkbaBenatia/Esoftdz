import datetime



class User:
    '''this class for user'''

    create_at = datetime.datetime.now()
    update_at = None
    status = False
    user_type = "01"
    
    def __init__(self,name,email,password,phone,picture):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.picture = picture
        