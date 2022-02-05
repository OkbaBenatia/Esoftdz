import datetime


class Author:
    """ class for the Author object"""

    create_At = datetime.datetime.now()  # Object creation date and time
    update_At = None

    def __init__(self, name, phone, email, country, address, websiteurl,
                 twitterurl, userid):
        self.name = name
        self.phone = phone
        self.email = email
        self.country = country
        self.address = address
        self.websiteurl = websiteurl
        self.twitterurl = twitterurl
        self.userid = userid  # Log the user who created the author object
