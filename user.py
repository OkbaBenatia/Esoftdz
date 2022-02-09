import datetime


class User:
    # this class for user
    create_at = datetime.datetime.now()  # user create date
    update_at = None  # user create date
    status = False  # user status , True = active, False = deactive
    user_type = "01"  # user type '00': Admin, '01': student user

    def __init__(self, name, email, password, phone, picture):
        '''allow to create object automatically'''

        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.picture = picture
