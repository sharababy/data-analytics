import numpy as np
import csv
import pyfpgrowth



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

DataX=np.asarray(DataX[:10000])
# print(DataX)

# association_rules = list(apriori(DataX,min_support=0.009, min_confidence=0.9, min_lift=3, min_length=3))

patterns = pyfpgrowth.find_frequent_patterns(DataX, 90)

rules = pyfpgrowth.generate_association_rules(patterns, 0.99)

print("number of frequent itemsets:",len(list(rules.keys())))

for item in rules:

    # first index of the inner list
    # Contains base item and add item
    print(item)

    print("=====================================")






