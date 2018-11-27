import numpy as np
import csv
from apyori import apriori


DataX = []
# DataY = []

# Entities={
# 	"66": {},    # LanguageWorkedWith
# }

# eindex = [66]
# xindex = [6,103,126,4]
# yindex = 13

print("Loading data..."),

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:		
		try:
			values = row[66].split(";")
			DataX.append(np.asarray(values))			
		except ValueError:
			pass
			    
print("done")

DataX=np.asarray(DataX[:300])
# print(DataX)

association_rules = list(apriori(DataX,min_support=0.09, min_confidence=0.9, min_lift=3, min_length=3))

for item in association_rules:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")






