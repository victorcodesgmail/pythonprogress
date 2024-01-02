import os

path = "/home/boniface/Desktop/pythoncourse/theory/files/files.py"


if os.path.exist(path):
    print("Location is visible!")
    
else:
    print("That location exist")

