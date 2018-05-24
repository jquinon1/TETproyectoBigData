#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This scripy verify is all lines start with the correct structure
#\#,id,title,publication,author,date,year,month,url,content

import re
import os

file_name = 'articles'
for i in range(1,4):
    with open("{}{}.csv".format(file_name,i)) as f:
        counter = 1
        bad = 0
        for line in f:
            if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                counter = counter+1
            else:
                #print("Bad line in {}".format(counter))
                counter = counter+1
                bad = bad+1

    print("Number of bad lines {}".format(bad))
    print("Creating a file with the standard {}{}".format(file_name,i))
    with open("{}{}_cleaned.csv".format(file_name,i),'w') as w:
        with open("{}{}.csv".format(file_name,i)) as f:
            for line in f:
                if not re.match(r'^\s*$', line):
                    if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                        w.write("\n{}".format(line.rstrip().replace('\r','')))
                    else:
                        w.write(line.rstrip().replace('\r',''))
    print("Creating a filtered file {}{}".format(file_name,i))
    with open("{}{}_cleaned.csv".format(file_name,i)) as f:
        with open("{}{}_filtered.csv".format(file_name,i),'w') as w:
            cont = 0
            for line in f:
                to_wr = re.split(r'\,(\d{4}[\-\/]\d{1,2}[\-\/]\d{1,2}|nan|date)?\,(\d{4}\.\d|nan|year)?\,(\d+\.\d|nan|month)?\,\s*\"?\s*(url|https?://(\w+\.)?\w+\.\w+(\/[\w\d\-\.\=\?\&\+\(\)\%\s\#]+)+\/?)*\s*\"?\s*\,',line)
                ready = ",".join(to_wr[0::len(to_wr)-1]) if len(to_wr) > 1 else to_wr[0]
                w.write(ready)
    print("Removing temporal file")
    os.remove("{}{}_cleaned.csv".format(file_name,i))
