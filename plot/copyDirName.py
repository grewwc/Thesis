import os
import sys


def isDir(path):
    return os.path.isdir(path)


def show(path):
    path = os.path.join(os.getcwd(), path)
    allNames = os.listdir(path)
    for name in allNames:
        name = os.path.join(path, name)
        if isDir(name):
            yield os.path.abspath(name)


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    elif len(sys.argv) == 1:
        path = '.'
    else:
        print("0 or 1 parameter")
        sys.exit(0)
    for name in show(path):
        print(name)



# print(os.path.isdir('/Users/grewwc/'))
main()
