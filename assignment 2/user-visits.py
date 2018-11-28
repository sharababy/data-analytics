import random
import numpy as np
import matplotlib.pyplot as plt
import csv

X = {}

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:
		# a = list(map(float, row))
		if (row[102] in X) == False:
			X[row[102]] = 0
		try:
			X[row[102]] += 1
		except ValueError:
		    pass



labels = list(X.keys())
size = list(X.values())

tot = np.sum(size)

for x in range(len(labels)):
	# print(str(float(float(X[x])/tot)))
	labels[x] += " - %1.1f%%"%(float(float(X[labels[x]])/tot) * 100.0)

patches, texts = plt.pie(x=size, shadow=False, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title("Visits to StackOverflow")
plt.show()









