import sys
import os
from github import Github

filename = str(sys.argv[1])
path = "Path where u want to save your Project" + filename
os.makedirs(path)
userName = "Your GitHub userName"
password = "Your GitHub password"

g = Github(userName, password)
user = g.get_user()
repo = user.create_repo(filename)
print("Succesfully created repository {} in GitHub".format(filename))


