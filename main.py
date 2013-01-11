#!/usr/bin/python

import sys
import re
#import time
import datetime
import os
from dateutil.parser import *

#reg expression for date
link_re = re.compile('([0-9][0-9]\-[0-9][0-9]-[0-9\:\-\ ]*)')
dataArray =[]
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    if  file.endswith(".properties"):
        with open(file) as f:
            for line in f:
                links = link_re.findall(line)
            
                if str(links) != "[]":
                    playertime =parse(links[0].strip())
                    #print playertime
                    tuplesdata=playertime, line
                    dataArray.append(tuplesdata)


dataArray.sort(key=lambda tup: tup[0])
output=map(lambda x: x[1], dataArray)
#print output
f = open('./output.txt','w')
f.writelines(output)
f.flush()
f.close()