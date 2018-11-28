from sklearn.cluster import AgglomerativeClustering
import numpy as np
import csv
from matplotlib import pyplot as plt

DataX = []
# DataY = []

Entities={
	"66": {},    # LanguageWorkedWith
	"13": {}     # JobSatisfaction
}


eindex = [66,13]
# xindex = [6,103,126,4]
# yindex = 13

print("Loading data..."),

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:		
		# a = list(map(float, row))
		for x in eindex:
			if x == 66:

				values = row[x].split(";")

				for value in values:
					if (value in Entities[str(x)]) == False:
						Entities[str(x)][value] = len(Entities[str(x)].keys())
				
			else:
				if (row[x] in Entities[str(x)]) == False:
					Entities[str(x)][row[x]] = len(Entities[str(x)].keys())

		datarow = []
		try:
			
			values = row[66].split(";")
			palues = []
			for value in values:
				palues.append(Entities[str(66)][value])
			p = np.sum(palues)/len(values)
			datarow.append(p)
			datarow.append(Entities[str(66)][value])
			DataX.append(np.asarray(datarow))
				
			
		except ValueError:
			pass
			    


features = ["LanguageWorkedWith","JobSatisfaction"]

print("Features: ",features)

print("Initializing Agglomerative Clustering")

DataX=np.asarray(DataX[:10000])
# print(DataX[:20])

linkage = "ward"
clustering = AgglomerativeClustering(linkage=linkage,n_clusters=6).fit(DataX)

plt.scatter(DataX.T[0],DataX.T[1] , c=clustering.labels_)



plt.show()