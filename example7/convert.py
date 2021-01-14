#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable called `polls`
with open('input.csv') as f:
    reader = csv.DictReader(f)
    polls = list(reader)

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['date','approve'])

    # 3. Loop through each row of `polls` 
    for row in polls:
		# 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
 		## Visited https://strftime.org/ to find date format 
		# hint: to read the date you will need to use
	    date = datetime.datetime.strptime((row['enddate']), "%m/%d/%Y") 
	    # and to write the date you will need to use something like 
	    updated_date = date.strftime("%-d-%b-%y")       
	    # 5. write a new row of data with the transformed date and value for "approve" 
	    writer.writerow([updated_date, row['approve']])
