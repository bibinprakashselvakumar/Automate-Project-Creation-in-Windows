@echo off
python "path to create.py" %1
cd /d "Path where ur project is saved"%1
echo "#" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/username/%1.git
git push -u origin master
code .