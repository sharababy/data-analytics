import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
import operator


X = {}

with open('../survey_results_public.csv') as csvfile:
# with open('train-01.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV)  # Skip header line
	for row in readCSV:
		ides = row[73].split(";");
		for i in ides:
			# a = list(map(float, row))
			if (i in X) == False:
				X[i] = 0
			try:
				X[i] += 1
			except ValueError:
			    pass


x = sorted(X.items(), key=operator.itemgetter(1), reverse=True)

X = dict(x)

labels = list(X.keys())
size = list(X.values())


tot = np.sum(size)

# for x in range(len(labels)):
# 	# print(str(float(float(X[x])/tot)))
# 	labels[x] += " - %1.1f%%"%(float(float(X[labels[x]])/tot) * 100.0)

# patches, texts = plt.pie(x=size, shadow=False, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.title("IDE Used by Developers")
# plt.show()

plt.figure(figsize=(25, 5))
y_pos = np.arange(len(labels))
plt.bar(y_pos, size,width=0.3, align='center', alpha=0.6)
plt.xticks(y_pos, labels,rotation=90)
plt.ylabel('Usage')
plt.title('IDEs Used by Developers')
 
plt.show()







