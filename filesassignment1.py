# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
textstring = fh.read()
allcaps = textstring.upper()
print allcaps.rstrip()

