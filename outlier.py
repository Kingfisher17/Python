import numpy as np
import pandas as pd

data = pd.DataFrame()

data['price'] = [2500000,4700000,7800000,10000000,6348561]
data['room'] = ['1RK','1BHK','2BHK','3BHK','2.5BHK']
data['area'] = [325,500,750,1100,820]

print(data)

print(data[data['price']<10000000])

data['outlier'] = np.where(data['price']<10000000,0,1)

print(data)

data['log'] = [np.log(x) for x in data['area']]
print(data)