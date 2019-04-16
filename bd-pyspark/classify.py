from sklearn import tree
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np 
import pandas as pd

X = pd.read_csv("HealthIndicatorONE.csv",delimiter=",",

usecols=["TT_Children_Aged_12_23_Months_Having_Immunization_Card_Rural",
"TT_Children_Aged_12_23_Months_Having_Immunization_Card_Urban",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Total",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Rural",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Bcg_Urban",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Total",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Rural",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Polio_Vaccine_Urban",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Total",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Rural",
"TT_Children_Aged_12_23_Months_Who_Have_Received_3_Doses_Of_Dpt_Vaccine_Urban",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Total",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Rural",
"TT_Children_Aged_12_23_Months_Who_Have_Received_Measles_Vaccine_Urban",
"TT_Children_Aged_12_23_Months_Fully_Immunized_Total",
"TT_Children_Aged_12_23_Months_Fully_Immunized_Rural",
"TT_Children_Aged_12_23_Months_Fully_Immunized_Urban",
"TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Total",
"TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Rural",
"TT_Children_Who_Have_Received_Polio_Dose_At_Birth_Urban",
"TT_Children_Who_Did_Not_Receive_Any_Vaccination_Total",
"TT_Children_Who_Did_Not_Receive_Any_Vaccination_Rural",
"TT_Children_Who_Did_Not_Receive_Any_Vaccination_Urban",
"TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Total",
"TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Rural",
"TT_Children_Aged_6_35_Months_Who_Received_At_Least_One_Vitamin_A_Dose_During_Last_Six_Months_Urban",
"TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Total",
"TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Rural",
"TT_Children_Aged_6_35_Months_Who_Received_Ifa_Tablets_Syrup_During_Last_3_Months_Urban",
"TT_Children_Whose_Birth_Weight_Was_Taken_Total",
"TT_Children_Whose_Birth_Weight_Was_Taken_Rural",
"TT_Children_Whose_Birth_Weight_Was_Taken_Urban",
"TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Total",
"TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Rural",
"TT_Children_With_Birth_Weight_Less_Than_2_5_Kg_Urban",
"UU_Children_Suffering_From_Diarrhoea_Total",
"UU_Children_Suffering_From_Diarrhoea_Rural",
"UU_Children_Suffering_From_Diarrhoea_Urban",
"UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Total",
"UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Rural",
"UU_Children_Suffering_From_Diarrhoea_Who_Received_Haf_Ors_Ort_Urban",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Total",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Rural",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Urban",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Total",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Rural",
"UU_Children_Suffering_From_Acute_Respiratory_Infection_Who_Sought_Treatment_Urban",
"UU_Children_Suffering_From_Fever_Total",
"UU_Children_Suffering_From_Fever_Rural",
"UU_Children_Suffering_From_Fever_Urban",
"UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Total",
"UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Rural",
"UU_Children_Suffering_From_Fever_Who_Sought_Treatment_Urban",
"VV_Children_Breastfed_Within_One_Hour_Of_Birth_Total",
"VV_Children_Breastfed_Within_One_Hour_Of_Birth_Rural",
"VV_Children_Breastfed_Within_One_Hour_Of_Birth_Urban",
"VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Total",
"VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Rural",
"VV_Children_Aged_6_35_Months_Exclusively_Breastfed_For_At_Least_Six_Months_Urban",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Total",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Rural",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Water_Urban",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Total",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Rural",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Animal_Formula_Milk_Urban",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Total",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Rural",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Semi_Solid_Mashed_Food_Urban",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Total",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Rural",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Solid_Adult_Food_Urban",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Total",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Rural",
"VV_Children_Who_Received_Foods_Other_Than_Breast_Milk_During_First_6_Months_Vegetables_Fruits_Urban",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Total",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Rural",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Water_Urban",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Total",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Rural",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Animal_Formula_Milk_Urban",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Total",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Rural",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Semi_Solid_Mashed_Food_Urban",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Total",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Rural",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Solid_Adult_Food_Urban",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Total",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Rural",
"VV_Average_Month_By_Which_Children_Received_Foods_Other_Than_Breast_Milk_Vegetables_Fruits_Urban",
])


X = X.fillna(0)

Y = pd.read_csv("HealthIndicatorONE.csv",delimiter=",",
usecols=["YY_Infant_Mortality_Rate_Imr_Total_Person"])

Y = Y.fillna(0)


Xtrain = X.values[:-30,:]
Ytrain = Y.values[:-30,:]

Xtest = X.values[-30:,:]
Ytest = Y.values[-30:,:]



clf = tree.DecisionTreeRegressor()
clf = clf.fit(Xtrain,Ytrain)
k = clf.predict(Xtest)
print(k)
s = clf.score(Xtest,Ytest)
print("Decision Tree Accuracy",s)



est = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
    max_depth=10, random_state=7, loss='ls').fit(Xtrain, Ytrain)
s = est.score(Xtest,Ytest)
print("Gradient Boosting Trees Accuracy: ",s)
