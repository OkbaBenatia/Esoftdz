import datetime


class Author:
    # this class for auther
    create_At = datetime.datetime.now()  # author create date
    update_At = None # user update date

    def __init__(self, name, phone, email, country, address, websiteurl,
                 twitterurl, userid):
        '''define the attribute in __init__ allow to create the object easly'''

        self.name = name
        self.phone = phone
        self.email = email
        self.country = country
        self.address = address
        self.websiteurl = websiteurl
        self.twitterurl = twitterurl
        self.userid = userid  # Log the user who created the author object
