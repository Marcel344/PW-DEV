from .parser import convert_to_pd
from os.path import join
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp


# This class will hold the tables of a given website, once the constructor is
# called, 8 processes will start and each of them will parse it's specified
# table, this speeds up the parsing by noticable amount of time
class Website:
    def __init__(self, path):
        self.Votes = None
        self.Users = None
        self.Tags = None
        self.PostLinks = None
        self.Posts = None
        self.PostHistory = None
        self.Comments = None
        self.Badges = None

        with ProcessPoolExecutor(
            mp_context=mp.get_context("fork")
        ) as executor:
            (
                self.Votes,
                self.Users,
                self.Tags,
                self.PostLinks,
                self.Posts,
                self.PostHistory,
                self.Comments,
                self.Badges,
            ) = executor.map(
                self.worker,
                [
                    join(path, "Votes.xml"),
                    join(path, "Users.xml"),
                    join(path, "Tags.xml"),
                    join(path, "PostLinks.xml"),
                    join(path, "Posts.xml"),
                    join(path, "PostHistory.xml"),
                    join(path, "Comments.xml"),
                    join(path, "Badges.xml"),
                ],
            )

        self.Name = path.split(".")[0]

    def worker(self, path):
        return convert_to_pd(path)
