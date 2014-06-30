from __future__ import print_function

import glob

import csv

from collections import Counter



l=list()
writer = csv.writer(open('appended_output.csv', 'wb'))
for files in glob.glob("*.csv"):
    reader = csv.reader(open(files, 'rb'))
    for row in reader:
        writer.writerow(row)
        l.append(row)
        

#f=csv.reader(open('appended_output.csv','rb'))

rep=Counter()
for row in l:
    rep+=Counter([row[0]])

rep=str(rep)
rep=rep.split(',')
rep[0]=rep[0].split('Counter({')

with open('Results.txt','w') as t:
    for each_element in rep:
        if isinstance(each_element,list):
            each_element=each_element[1]
        
        t.write(each_element+'\n\n')
        
