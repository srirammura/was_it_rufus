import git
import datetime
import argparse
import os


class was_it_rufus:

    def __init__(self, git_directory):

        self.repo = git.Repo(git_directory)

        self.active_branch = self.repo.active_branch.name
        self.local_changes = self.repo.is_dirty()
        self.recent_commit = (datetime.datetime.now().date() - self.repo.head.commit.authored_datetime.date()) < datetime.timedelta(
            weeks=1)
        self.blame_rufus = self.repo.head.commit.author.name == "Rufus"

    def git_status(self):
        print("active branch: ", self.active_branch)
        print("local changes: ", self.local_changes)
        print("recent commit: ", self.recent_commit)
        print("blame Rufus: ", self.blame_rufus)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Was it rufus?')
    parser.add_argument('git_directory', type=str,
                        help='name of the git repo directory')

    args = parser.parse_args()

    if os.path.isdir(args.git_directory):
        rufus_obj = was_it_rufus(args.git_directory)
        rufus_obj.git_status()
    else:
        print(args.git_directory, "Invalid directory.")
