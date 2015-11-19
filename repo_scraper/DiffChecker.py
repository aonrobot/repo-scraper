from repo_scraper import matchers
from repo_scraper.Result import * #need to find a better way to do this

class DiffChecker:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
    def check(self):
        #Check the number of additions, if there are too many
        #send a warning and skip, this may be due to a big data file addition
        
        #Check file extension, if it's a text file continue, if it's not,
        #send a warning and skip
        
        #Start applying rules...
        #First check if additions contain base64, if there is remove it
        
        #Now check for passwords
        has_pwd, matches = matchers.password_matcher(self.content)

        if has_pwd:
            return Result(self.filename, MATCH, matches)
        else:
            return Result(self.filename, NOT_MATCH)