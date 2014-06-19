hrs = raw_input('Enter Hours: ')
try:
    h = float(hrs)
except:
    print "Please enter a numeric value."	
    exit()
rte = raw_input('Enter Rate: ') 
try:
    r = float(rte)
except:
    print "Please enter a numeric value."	
    exit()
if h > 40:
    ot = (h-40)*1.5
    pay = ot * r + 40 * r
else:
    pay = h	* r
print pay