import pandas as pd
import numpy as np

df = pd.read_csv("HealthIndicatorONE.csv",delimiter=",",
	usecols=[
	"YY_Crude_Death_Rate_Cdr_Total_Person",
	"YY_Crude_Death_Rate_Cdr_Total_Male",
	"YY_Crude_Death_Rate_Cdr_Total_Female",
	"YY_Crude_Death_Rate_Cdr_Rural_Person",
	"YY_Crude_Death_Rate_Cdr_Rural_Male",
	# "YY_Crude_Death_Rate_Cdr_Rural_Female",
	# "YY_Crude_Death_Rate_Cdr_Urban_Person",
	# "YY_Crude_Death_Rate_Cdr_Urban_Male",
	# "YY_Crude_Death_Rate_Cdr_Urban_Female"
	])

df = df.fillna(0)

def roundup(x):
	return np.floor(x)

ndf = roundup(df.values)

np.savetxt("transaction_data.csv",ndf,delimiter=",",fmt="%d")


