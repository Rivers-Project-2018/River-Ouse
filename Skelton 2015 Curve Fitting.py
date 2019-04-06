##Importing relevant programmes## Adapted from https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
import matplotlib.pyplot as plt 
import pandas as pd 
import operator
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='k'
plt.style.use('seaborn-whitegrid')
 
##Assigning raw data to variables##
ouse = pd.read_csv('Skelton 2015.csv') 
day = ouse['Day'] 
height = ouse['Stage'] 
flow = ouse['Flow']

##Defining h_t##
h_T=6.17


##Plotting raw data##
x = height
y = flow
plt.plot(x, y,'+',color='grey')

##Plotting  polynomial of degree 2
x = height
y = flow
x2 = x[:, np.newaxis]
y2 = y[:, np.newaxis]
polynomial_features= PolynomialFeatures(degree=2)
x_poly2 = polynomial_features.fit_transform(x2)
model = LinearRegression()
model.fit(x_poly2, y2)
y_poly2_pred = model.predict(x_poly2)

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x2,y_poly2_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x2, y_poly2_pred, color='blue', linewidth=1.0,label='Poly2')

p2_rmse = np.sqrt(mean_squared_error(y2,y_poly2_pred))
p2_r2 = r2_score(y2,y_poly2_pred)
print('PolyFit of Degree 2:')
print('RMSE='+str(p2_rmse))
print('R^2='+str(p2_r2))

##Plotting  polynomial of degree 3
x = height
y = flow
x3 = x[:, np.newaxis]
y3 = y[:, np.newaxis]
polynomial_features= PolynomialFeatures(degree=3)
x_poly3 = polynomial_features.fit_transform(x3)
model = LinearRegression()
model.fit(x_poly3, y3)
y_poly3_pred = model.predict(x_poly3)

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x3,y_poly3_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x3, y_poly3_pred, color='green', linewidth=1.0, label='Poly3')

p3_rmse = np.sqrt(mean_squared_error(y3,y_poly3_pred))
p3_r2 = r2_score(y3,y_poly3_pred)
print('PolyFit of Degree 3:')
print('RMSE='+str(p3_rmse))
print('R^2='+str(p3_r2))


##Plotting  polynomial of degree 4
x = height
y = flow
x4 = x[:, np.newaxis]
y4 = y[:, np.newaxis]
polynomial_features= PolynomialFeatures(degree=4)
x_poly4 = polynomial_features.fit_transform(x4)
model = LinearRegression()
model.fit(x_poly4, y4)
y_poly4_pred = model.predict(x_poly4)

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x4,y_poly4_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x4, y_poly4_pred, color='firebrick', linewidth=1.0, label='Poly4')

p4_rmse = np.sqrt(mean_squared_error(y4,y_poly4_pred))
p4_r2 = r2_score(y4,y_poly4_pred)
print('PolyFit of Degree 4:')
print('RMSE='+str(p4_rmse))
print('R^2='+str(p4_r2))

##Plotting  polynomial of degree 5
x = height
y = flow
x5 = x[:, np.newaxis]
y5 = y[:, np.newaxis]
polynomial_features= PolynomialFeatures(degree=5)
x_poly5 = polynomial_features.fit_transform(x5)
model = LinearRegression()
model.fit(x_poly5,y5)
y_poly5_pred = model.predict(x_poly5)

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x5,y_poly5_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x5, y_poly5_pred, color='orange', linewidth=1.0, label='Poly5')


p5_rmse = np.sqrt(mean_squared_error(y5,y_poly5_pred))
p5_r2 = r2_score(y5,y_poly5_pred)
print('PolyFit of Degree 5:')
print('RMSE='+str(p5_rmse))
print('R^2='+str(p5_r2))

plt.xlabel('$\overline {h}$$ [m]$')
plt.ylabel('$Q$ [m$^3$s$^{-1}$]')
plt.xlim(min(height),max(height))
plt.ylim(min(flow),max(flow))
plt.legend()
plt.show()