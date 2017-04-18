# -*- coding: utf-8 -*-
import csv

s = 'var data = { "chartTitle":"Predátorské časopisy ve Scopusu", "yLabel":"Scimago Journal Rank", "xLabel": "% autorů z rozvinutých zemí", "points" :{'

jrns = []

i=0
with open('inputData.csv') as f:
    rd = csv.DictReader(f)
    for row in rd:
        s += '"' + str(row['ISSN']) + '":' + str(row).replace("'",'"').replace('samostatné ?asopisy','samostatné časopisy')
        if i != 239:
            s += ','

        i+=1

print(rd)
s += '}}'

print(s)
#f = open('predatori.js','w',encoding='utf-8')
#f.write(s)
#f.close()
