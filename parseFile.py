from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("GEO_studies"):
    f.extend(filenames)
    break

for item in f:
    _file = open(item, "r")
    print(_file.readline)
