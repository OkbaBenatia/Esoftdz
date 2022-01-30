import datetime

# class for the Author object
class Author:
    create_At = datetime.datetime.now()
    update_At = None

    def __init__(self, name, phone, email , country , address , websiteurl , twitterurl , userid):
        self.name = name
        self.phone = phone
        self.email = email
        self.country = country
        self.address = address
        self.websiteurl = websiteurl
        self.twitterurl = twitterurl
        self.userid = userid

