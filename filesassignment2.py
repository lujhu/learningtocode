# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	atpos = line.find(":")
	extract = line[atpos+1:]
	extract.lstrip()
	extract.rstrip()
	total = total + float(extract)
	count = count + 1
average = (total/count)
print "Average spam confidence:", average
