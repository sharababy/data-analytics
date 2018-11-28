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
		if (row[3] in X) == False:
			X[row[3]] = []
		try:
			if float(row[52]) != 0.0:
				X[row[3]].append(np.log(float(row[52])))
		except ValueError:  #raised if `y` is empty.
		    pass


def set_axis_style(ax, labels):
    ax.get_yaxis().set_tick_params(direction='out')
    ax.yaxis.set_ticks_position('left')
    ax.set_yticks(np.arange(1, len(labels) + 1))
    ax.set_yticklabels(labels)
    ax.set_ylim(0.2, len(labels) + 0.5)
    ax.set_ylabel('Countries')
    ax.set_xlabel('Log(Salaries)')



fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(1, 1))


Y = []
labels = []
i = 0

for x in X:
	if len(X[x]) > 1000:
		labels.append(x);
		Y.append(X[x])
		i+=1
	if i == 10: break
	
# print(np.asarray(Y))

# for x in X.keys():
try:
	axes.violinplot(Y,points=20,widths=0.5,vert=False,showmedians=True,showextrema=True,showmeans=False)
except ValueError:  #raised if `y` is empty.
    pass


# axes.set_title('', fontsize=10)

set_axis_style(axes, labels)

fig.suptitle("Violin Plot for Developer Salaries for top 10 Countries")
fig.subplots_adjust(hspace=0.4)

plt.show()


