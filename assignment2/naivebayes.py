from sklearn.naive_bayes import ComplementNB
import numpy as np
import csv

DataX = []
DataY = []

Entities={
	"6": {},    # Employment
	"103": {},  # StackOverflowVisit
	"126": {},  # Age
	"4": {},    # Country
	"13": {}     # JobSatisfaction
}

classNames = {}

# Features={
# 	"6": {},    # Employment
# 	"103": {},  # StackOverflowVisit
# 	"126": {},  # Age
# 	"4": {},    # Country
# 	"13": {}     # JobSatisfaction
# }

eindex = [6,103,126,4,13]
xindex = [6,103,126,4]
yindex = 13

print("Loading data..."),

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:		
		# a = list(map(float, row))
		for x in eindex:
			if (row[x] in Entities[str(x)]) == False:
				Entities[str(x)][row[x]] = len(Entities[str(x)].keys())
				if x == 13:
					classNames[row[x]] = 0	

		datarow = []
		try:
			for x in xindex:	
				datarow.append(Entities[str(x)][row[x]])
			DataX.append(datarow)
			DataY.append(Entities[str(yindex)][row[yindex]])
			# if (row[x] in Entities[str(x)]) == False:
			# 	classNames[row[yindex]] = 
		except ValueError:
			pass
			    

features = ["Employment",
"StackOverflowVisit",
"Age",
"Country",]

print("Features: ",features)

print("classnames:",list(classNames.keys()))



print("Initializing Naive Bayes Classifier")

DataX=np.asarray(DataX)
DataY=np.asarray(DataY)

gnb = ComplementNB()
y_pred = gnb.fit(DataX, DataY).predict(DataX)

print("Classification complete.")

TotalPoints = float(DataX.shape[0])
mislabeled = float((DataY == y_pred).sum())

print("Number of mislabeled points out of a total %d points : %d" % (TotalPoints,mislabeled))

print("Classification Accuracy: ", (mislabeled/TotalPoints)*100.0)



