# import matplotlib.pyplot as plt
# from scipy import stats

# # age = [18,25,30,34,40,42,51,55,60,65,70]
# # speed = [30,35,40,60,72,80,60,55,40,30,100]

# age = [18,20,25,30,35,40,45,50,55,60,65,70]
# speed = [30,35,40,42,45,55,50,50,45,45,40,35]

# slope, intercept,r ,p ,std_err =  stats.linregress(age,speed)

# def fun(age):
#     return slope * age + intercept

# model = list(map(fun,age))

# plt.scatter(age,speed)
# plt.suptitle("Age VS Speed")
# plt.plot(age,model)
# plt.show()

# # print(std_err)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 

dataset = pd.read_csv('Salary_Data.csv')
# print(dataset.head())

X = dataset.iloc[:,:-1].values  #independent variable array
y = dataset.iloc[:,1].values  #dependent variable vector

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

regressor = LinearRegression()
regressor.fit(X_train,y_train) #actually produces the linear eqn for the data
y_pred = regressor.predict(X_test) 
print(y_pred)
