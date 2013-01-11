#!/usr/bin/python

import sys
import re
#import time
import datetime

#reg expression for date
link_re = re.compile('([0-9][0-9]\-[0-9][0-9]-[0-9\:\-\ ]*)')
dataArray =[]
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
for file in sys.argv:
    with open(file) as f:
        for line in f:
            links = link_re.findall(line)
            
            if str(links) != "[]":
                playertime =datetime.datetime.strptime(links[0].strip(), "%d-%m-%Y %H:%M:%S")
                #print playertime
                tuplesdata=playertime, line
                dataArray.append(tuplesdata)
                #print time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
                #print links[0]

dataArray.sort(key=lambda tup: tup[0])
output=map(lambda x: x[1], dataArray)
#print output
f = open('./output.txt','w')
f.writelines(output)
f.flush()
f.close()