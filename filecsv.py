import csv, os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('mpd2019.csv', skipinitialspace=True, na_values=[''] )

in_array = (data["cgdppc"].values.reshape(-1, 1))
x = np.log(in_array)
y = (data["countrycode"])

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(x, y)  # perform linear regression
y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()

#csvFilename = 'mpd2018.csv' fields = ['countrycode']


# Read the CSV file in (skipping first row).
#csvRows = []
#csvFileObj = open(csvFilename)
#readerObj = csv.reader(csvFileObj)
#  for row in readerObj:
#    if readerObj.line_num == 1:
#    continue
# skip first row
#csvRows.append(row)
#csvFileObj.close()
