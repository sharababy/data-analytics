import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import sys

df = pd.read_csv("HealthIndicatorONE.csv",delimiter=",")

# Handle Missing Values

# Method 1
# df = df.dropna()

#  Method 2
df = df.fillna(0)

state = sys.argv[1]

# Method 3
df = df.replace(np.NaN,0)

print("Dataset Shape",df.shape)

# Descriptive Statistics:

# State_Name vs AA_Population_Total
# bar graph

fig, ax1 = plt.subplots(figsize=(13, 8))

plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

ax1.set_title('Different Kinds of Mortality Rates across Different Districs in '+state)

plt.boxplot(
	[
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Total_Person"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Total_Male"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Total_Female"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Rural_Person"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Rural_Male"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Rural_Female"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Urban_Person"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Urban_Male"],
df.loc[df['State_Name'] == state]["YY_Crude_Death_Rate_Cdr_Urban_Female"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Total_Person"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Total_Male"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Total_Female"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Rural_Person"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Rural_Male"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Rural_Female"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Urban_Person"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Urban_Male"],
df.loc[df['State_Name'] == state]["YY_Infant_Mortality_Rate_Imr_Urban_Female"],
df.loc[df['State_Name'] == state]["YY_Neo_Natal_Mortality_Rate_Total"],
df.loc[df['State_Name'] == state]["YY_Neo_Natal_Mortality_Rate_Rural"],
df.loc[df['State_Name'] == state]["YY_Neo_Natal_Mortality_Rate_Urban"],
df.loc[df['State_Name'] == state]["YY_Post_Neo_Natal_Mortality_Rate_Total"],
df.loc[df['State_Name'] == state]["YY_Post_Neo_Natal_Mortality_Rate_Rural"],
df.loc[df['State_Name'] == state]["YY_Post_Neo_Natal_Mortality_Rate_Urban"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Total_Person"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Total_Male"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Total_Female"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Rural_Person"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Rural_Male"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Rural_Female"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Urban_Person"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Urban_Male"],
df.loc[df['State_Name'] == state]["YY_Under_Five_Mortality_Rate_U5MR_Urban_Female"],
	
	],
 	notch=True)


labels = [
"Cdr_Total_Person",
"Cdr_Total_Male",
"Cdr_Total_Female",
"Cdr_Rural_Person",
"Cdr_Rural_Male",
"Cdr_Rural_Female",
"Cdr_Urban_Person",
"Cdr_Urban_Male",
"Cdr_Urban_Female",
"Imr_Total_Person",
"Imr_Total_Male",
"Imr_Total_Female",
"Imr_Rural_Person",
"Imr_Rural_Male",
"Imr_Rural_Female",
"Imr_Urban_Person",
"Imr_Urban_Male",
"Imr_Urban_Female",
"NNM_Total",
"NNM_Rural",
"NNM_Urban",
"PNNM_Total",
"PNNM_Rural",
"PNNM_Urban",
"U5MR_Total_Person",
"U5MR_Total_Male",
"U5MR_Total_Female",
"U5MR_Rural_Person",
"U5MR_Rural_Male",
"U5MR_Rural_Female",
"U5MR_Urban_Person",
"U5MR_Urban_Male",
"U5MR_Urban_Female"]

xtickNames = plt.setp(ax1, xticklabels=labels)
plt.setp(xtickNames, rotation=90, fontsize=8)

# plt.xlabel('State_Name',fontsize=12)
# plt.ylabel('Population_Total', fontsize=12)

plt.show()


