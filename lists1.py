fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for item in words:
        if item in lst : continue
        lst.append(item)
lst.sort()
print lst