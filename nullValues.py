import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

data1 = pd.read_csv("iris.csv")

data1["variety"].fillna("a",inplace=True)

print(data1)
# data1.plot(x='sepal.length',y='variety',kind='scatter')
# plt.show()