import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
import operator

CarSatAge = {}

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:		
		# a = list(map(float, row))
		if (row[8] in CarSatAge) == False:
			CarSatAge[row[8]] = {}
		try:
			if (row[124] in CarSatAge[row[8]]) == False and row[124] != "NA":
				CarSatAge[row[8]][row[124]] = 0

			if (row[124] in CarSatAge[row[8]]):
				CarSatAge[row[8]][row[124]] += 1
			
		except ValueError:
		    pass


allsat = {}

for sat in CarSatAge:
	x = sorted(CarSatAge[sat].items(), key=operator.itemgetter(0), reverse=False)
	allsat[sat] = dict(x)


for sat in allsat:
	allsat[sat]["0 - 18 years of age"] = (allsat[sat]).pop("Under 18 years old")

for sat in allsat:
	x = sorted(allsat[sat].items(), key=operator.itemgetter(0), reverse=False)
	allsat[sat] = dict(x)


labels = list(allsat.keys())
age = []
for sat in allsat:
	# labels.append(list(allsat[sat].keys())) 
	age.append(list(allsat[sat].values()))

# print(allsat)



x = [18,24,34,44,54,64,100]

lines = []
for y,label in zip(age,labels):
	
	pltx, = plt.plot(x,y,'.-',label=label)
	lines.append(pltx)

plt.legend(lines, labels, loc="best")	

plt.xlabel('Age')
plt.ylabel('Num Users')
plt.title('Age vs Company Size')
 
plt.show()







