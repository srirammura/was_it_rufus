# Was it rufus?

## Project instructions
Your task is to create a program that prints specific facts about a local git repository. You can use any language, and you are welcome to import existing packages.

Your program should take in one argument:

git_dir: directory in which to assess git status


Your program should print the following things:

active branch (boolean)\
whether repository files have been modified (boolean)\
whether the current head commit was authored in the last week (boolean)\
whether the current head commit was authored by Rufus (boolean)\

## How to run this program

pip3 install -r requirements\
python3 main.py <git_directory_name>

for example :  python3 main.py /Users/srirammuralidharan/PycharmProjects/was_it_rufus/
