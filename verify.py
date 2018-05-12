#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This scripy verify is all lines start with the correct structure
#\#,id,title,publication,author,date,year,month,url,content

import re

file_name = 'articles3'
with open("{}.csv".format(file_name)) as f:
    counter = 1
    bad = 0
    for line in f:
        if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            counter = counter+1
        else:
            print("Bad line in {}".format(counter))
            counter = counter+1
            bad = bad+1
print("Number of bad lines {}".format(bad))
print("Creating a file with the standard")
with open("{}_cleaned.csv".format(file_name),'w') as w:
    with open("{}.csv".format(file_name)) as f:
        for line in f:
            if not re.match(r'^\s*$', line):
                if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                    w.write("\n{}".format(line.rstrip().replace("\"","").replace("”","").replace("\'","").replace("’","")))
                else:
                    w.write(line.rstrip().replace("\"","").replace("”","").replace("\'","").replace("’",""))
