""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run



# login credentials
insta_username = 'whatever123n'
insta_password = 'Bncwil89'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)


with smart_run(session):
    """ Activity flow """
    # general settings
   
    
    
    
    
    # activity
    session.like_by_tags(["natgeo"], amount=10)
    session.follow_user_followers(['eminem', 'machinegunkelly'], amount=100, randomize=True)




