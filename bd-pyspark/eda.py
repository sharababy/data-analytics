import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("HealthIndiactorTWO.csv",delimiter=",")


# Handle Missing Values

# Method 1
df = df.dropna()

#  Method 2
df = df.fillna(0)

# Method 3
df = df.replace(np.NaN,0)



print("Dataset Shape",df.shape)

# Descriptive Statistics:

# State_Name vs AA_Population_Total
# bar graph

plt.figure(figsize=(13,5))
plt.bar(df["State_Name"].values,df["AA_Population_Total"].values)

plt.xlabel('State_Name', fontsize=12)
plt.ylabel('Population_Total', fontsize=12)




'''
CC_Sex_Ratio_At_Birth_Total,
CC_Sex_Ratio_At_Birth_Rural,
CC_Sex_Ratio_At_Birth_Urban,
CC_Sex_Ratio_0_4_Years_Total,
CC_Sex_Ratio_0_4_Years_Rural,
CC_Sex_Ratio_0_4_Years_Urban,
CC_Sex_Ratio_All_Ages_Total,
CC_Sex_Ratio_All_Ages_Rural,
CC_Sex_Ratio_All_Ages_Urban
stacked bar graph vs State_Name

'''
plt.figure(figsize=(13,5))
p1 = plt.bar(df["State_Name"].values,df["CC_Sex_Ratio_All_Ages_Rural"].values)
p2 = plt.bar(df["State_Name"].values,df["CC_Sex_Ratio_All_Ages_Urban"].values,bottom=df["CC_Sex_Ratio_All_Ages_Rural"].values)

plt.xlabel('State_Name', fontsize=12)
plt.ylabel('Sex_Ratio_All_Ages', fontsize=12)
plt.legend((p1[0], p2[0]), ('Rural', 'Urban'))



'''
FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Total,
FF_Children_Currently_Attending_School_Age_6_17_Years_Female_Total,

stacked bar graph vs State_Name

'''

plt.figure(figsize=(13,5))
p1 = plt.bar(df["State_Name"].values,df["FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Total"].values)
p2 = plt.bar(df["State_Name"].values,df["FF_Children_Currently_Attending_School_Age_6_17_Years_Female_Total"].values,bottom=df["FF_Children_Currently_Attending_School_Age_6_17_Years_Male_Total"].values)

plt.xlabel('State_Name', fontsize=12)
plt.ylabel('Children_Currently_Attending_School_Age_6_17_Years', fontsize=12)
plt.legend((p1[0], p2[0]), ('Male', 'Female'))





'''
UU_Children_Suffering_From_Diarrhoea_Total
UU_Children_Suffering_From_Diarrhoea_Rural
UU_Children_Suffering_From_Diarrhoea_Urban
U_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Total
UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Rural
UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Urban
UU_Children_Suffering_From_Acute_Respiratory_Infection_Total
UU_Children_Suffering_From_Acute_Respiratory_Infection_Rural
UU_Children_Suffering_From_Acute_Respiratory_Infection_Urban
UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Total
UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Rural
UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Urban
UU_Children_Suffering_From_Fever_Total
UU_Children_Suffering_From_Fever_Rural
UU_Children_Suffering_From_Fever_Urban
UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Total
UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Rural
UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Urban

venn diagram per state

'''

plt.figure(figsize=(13,5))
p1 = plt.bar(df["State_Name"].values,df["UU_Children_Suffering_From_Diarrhoea_Total"].values)
p2 = plt.bar(df["State_Name"].values,df["UU_Children_Suffering_From_Acute_Respiratory_Infection_Total"].values,bottom=df["UU_Children_Suffering_From_Diarrhoea_Total"].values)
p3 = plt.bar(df["State_Name"].values,df["UU_Children_Suffering_From_Fever_Total"].values,bottom=(df["UU_Children_Suffering_From_Diarrhoea_Total"].values+df["UU_Children_Suffering_From_Acute_Respiratory_Infection_Total"].values))


plt.xlabel('State_Name', fontsize=12)
plt.ylabel('Children_Currently_Attending_School_Age_6_17_Years', fontsize=12)
plt.legend((p1[0], p2[0],p3[0]), ('Diarrhoea', 'Respiratory_Infection','Fever'))




plt.show()