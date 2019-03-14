##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='black' 
 
##Assigning raw data to variables##
ouse = pd.read_csv('Skelton 2015.csv') 
day = ouse['Day in December 2015'] 
height = ouse['Stage'] 
flow = ouse['Flow']


##Defining a polynomial fitting function
rtcrv=np.polyfit(height,flow,3)
p=np.poly1d(rtcrv)

##Defining an array to input into polynomial fit
h=np.arange(4.,7.5,0.001)

##Plotting raw data as '+' and polynomial fit as'-'
plt.plot(height,flow,'+',h,p(h),'black',linewidth=1.0)
plt.ylim(200,600)
plt.xlim(4,7)

##Titling graph and labelling axes
plt.title('Graph to show the flood event of the River Ouse (Skelton) in December 2015')
plt.xlabel('Stage, h $[m]$',style='italic',size=10)
plt.ylabel('Discharge,Q $[m^3/s]$',style='italic',size=10)

Q_t=p(h_t)
Print