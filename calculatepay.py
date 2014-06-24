# create the function computepay
def computepay(x,y):
	if x > 40:
		ot = (x-40)*1.5
		pay = ot * y + 40 * y
	else:
		pay = x	* y
	return pay
#ask user for input
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
# run the function	
print computepay(h,r)

