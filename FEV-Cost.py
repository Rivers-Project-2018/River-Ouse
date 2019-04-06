import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams["figure.figsize"] = [10,10] 
plt.style.use('seaborn-whitegrid')

##Defining the % effectiveness, properties protected and the % of the budget in the 5 year and 50 year scenario##
FEV=0.97
prop=(140/2000)*100
Budget5=(3076830/(45200000))*100
Budget50=(4942710/(45200000))*100
print(prop)
print(FEV)
print(Budget5)
print(Budget50)

##Defining arbitary points to ploy y=x line##
x=np.arange(0,20,1)
y=np.arange(0,20,1)

##Defining 2 seperate y axes##
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

##Plotting the red region and scatter point which represent effectiveness##
ax1.fill_between(x,y,where=x>=y,facecolor='firebrick',alpha=0.6)
ax1.plot([Budget5,Budget50],[FEV,FEV],'o',color='blue',markersize=10)
ax2.plot([Budget5,Budget50], [prop,prop],'s',color='black',markersize=10)


##Labelling and formatting axes##
ax1.set_xlabel('% Budget Spent', size=13,color='black')
ax1.set_ylabel('% FEV Mitigated',size=13, color='blue')
ax2.set_ylabel('% Properties Protected',size=13,color='black')
ax1.set_xlim(0,15)
ax1.set_ylim(0,15)
ax2.set_ylim(0,15)

