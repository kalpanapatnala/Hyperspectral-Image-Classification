# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('indian_liver_patient.csv')

dataset['Albumin_and_Globulin_Ratio'].fillna(dataset['Albumin_and_Globulin_Ratio'].mean(), inplace=True)

dataset['Gender'].replace(['Male','Female'],[1,0],inplace=True)

dataset['Dataset'].replace([1,2],[0,1],inplace=True)

X = dataset.iloc[:,:7]


y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.ensemble import RandomForestClassifier
rmf = RandomForestClassifier(max_depth=3, random_state=0)
rmf_c = rmf.fit(X, y)


# Saving model to disk
pickle.dump(rmf_c, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[65, 0, 0.7, 16, 6.8, 3.3, 0.9]]))