import csv
from analysis.models import data


ifile  = open('Housingdata.csv', "rb")
reader = csv.reader(ifile)

rownum = 0
total = 0
num = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
	rownum += 1
    else:
        colnum = 0
	try:
#		print row[0] + "   " + row[1] + "dsfsdfi :" + row[2]
		p=data(city=row[0],location=row[1],q1_2010=int(row[2]),q2_2010=int(row[3]),q3_2010=int(row[4]),q4_2010=int(row[5]),q1_2011=int(row[6]),q2_2011=int(row[7]),q3_2011=int(row[8]),q4_2011=int(row[9]),q1_2012=int(row[10]),q2_2012=int(row[11]),q3_2012=int(row[12]),q4_2012=int(row[13]))
		p.save()
	except:
		print "Error in storing info for city : " + row[0] + "  Location  : " + row[1]

'''        for col in row:
	    print '%-8s: %s' % (header[colnum], col)
	    if colnum==2:
	    	try:
	    		total = total + int(col)
			num=num+1
		except:
			num=num
            colnum += 1
	    '''
            
	    


ifile.close()
