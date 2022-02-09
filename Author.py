import datetime


class Author:
    # this class for auther
    create_at = datetime.datetime.now()  # author create date
    update_at = None  # Author update date

    def __init__(self, name, phone, email, country, address, website_url,
                 twitter_url, user_id):
        '''allow to create object automatically'''

        self.name = name
        self.phone = phone
        self.email = email
        self.country = country
        self.address = address
        self.website_url = website_url
        self.twitter_url = twitter_url
        self.user_id = user_id  # Log the user who created the author object
