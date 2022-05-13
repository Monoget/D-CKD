# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv('CKD.csv')
print(dataset)

# viewing the first few rows of the dataset
dataset.head()

# viewing statistical info about dataset
dataset.describe()

# dropping duplicate values
dataset = dataset.drop_duplicates()

print(dataset)

dataset.describe()

# checking for missing values
dataset.isnull()

# checking the number of missing data
dataset.isnull().sum()

# Dropping categorical data rows with missing values
dataset.dropna(how='any', subset=['AGE','BP','SPECIFIC GRAVITY','ALBUMIN','SUGAR','RED BLOOD CELLS','PUS CELL','PUS CELL CLUMPS','BACTERIA','BLOOD GLUCOSE RANDOM','BLOOD UREA','SERUM CREATININE','SODIUM','POTASSIUM','HEMAGLOBIN','PACKED CELL VOLUME','WHITE BLOOD CELL COUNT','RED BLOOD CELL COUNT','HYPERTENSION','DIABETES MELLITUS','CORONARY ARTERY DISEASE','APPETITE','PEDAL EDEMA','ANEMIA','CLASS'], inplace=True)

print(dataset)

dataset.describe()

# Splitting dataset into independent and dependent variable
X = dataset[['AGE','BP','SPECIFIC GRAVITY','ALBUMIN','SUGAR','RED BLOOD CELLS','PUS CELL','PUS CELL CLUMPS','BACTERIA','BLOOD GLUCOSE RANDOM','BLOOD UREA','SERUM CREATININE','SODIUM','POTASSIUM','HEMAGLOBIN','PACKED CELL VOLUME','WHITE BLOOD CELL COUNT','RED BLOOD CELL COUNT','HYPERTENSION','DIABETES MELLITUS','CORONARY ARTERY DISEASE','APPETITE','PEDAL EDEMA','ANEMIA','CLASS']].values
y = dataset[['HYPERTENSION','DIABETES MELLITUS','CORONARY ARTERY DISEASE','PEDAL EDEMA','PEDAL EDEMA']].values

print(X)
