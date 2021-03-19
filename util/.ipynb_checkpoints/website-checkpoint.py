from parser import convert_to_pd
from os.path import join

# This class will hold the tables of a given website
class Website:
    def __init__(self, path):
        self.Name = path.split(".")[0]
        self.Votes = convert_to_pd(join(path, "Votes.xml"))
        self.Users = convert_to_pd(join(path, "Users.xml"))
        self.Tags = convert_to_pd(join(path, "Tags.xml"))
        self.PostLinks = convert_to_pd(join(path, "PostLinks.xml"))
        self.Posts = convert_to_pd(join(path, "Posts.xml"))
        self.PostHistory = convert_to_pd(join(path, "PostHistory.xml"))
        self.Comments = convert_to_pd(join(path, "Comments.xml"))
        self.Badges = convert_to_pd(join(path, "Badges.xml"))
