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



rep2=rep
print (type(rep2))
text=str(rep2)
text=str(str(text.split("{")[1]).split("}")[0]).split(",")  # To convert collections.counter to type list


with open('Results.txt','w') as t:
    for each_element in text:
        t.write(each_element+'\n\n')
