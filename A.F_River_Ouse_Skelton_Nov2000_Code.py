##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white' 
 
##Assigning raw data to variables##
ouse = pd.read_csv('A.F_River_Ouse_Skelton_Nov2000_Data.csv') 
day = ouse['Day in November 2000'] 
height = ouse['Stage'] 
flow = ouse['Discharge']

 
##Defining a scale function##
def scale(x,y):return ((x-min(y))/(max(y)-min(y)))

##Scaling variables in preparation for plotting as subplots##
scaled_day=scale(day,day)
scaled_flow=scale(flow,flow)

neg_scaled_height=-(scale(height,height))
neg_scaled_day=-(scaled_day)

##Renaming command##
fig,ax=plt.subplots()


    
##Plotting subplots##
ax.plot(scaled_day,scaled_flow,'black', linewidth=2)
ax.plot(neg_scaled_height, scaled_flow,'gray', linewidth=1.5)
ax.plot(neg_scaled_height,neg_scaled_day,'black', linewidth=2)


##Centering and formatting axes##
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x',color='black',direction='out',length=10,width=1)
ax.tick_params(axis='y',color='black',direction='out',length=10,width=1)

##Scaling and Labelling axes
ticks_x=[-scale(6.75,height),-scale(6.5,height),-scale(6.25,height),-scale(6.0,height),-scale(5.75,height),-scale(5.5,height),scale(31,day),scale(32,day),scale(33,day),scale(34,day),scale(35,day),scale(36,day),scale(37,day)]
ax.set_xticks(ticks_x)
Ticks_x = [6.75,6.5,6.25,6.0,5.75,5.5,0,1,2,3,4,5,6]
ax.set_xticklabels(Ticks_x)

ticks_y=[-scale(37,day),-scale(36,day),-scale(35,day),-scale(34,day),-scale(33,day),-scale(32,day),-scale(31,day),scale(350,flow),scale(400,flow),scale(450,flow),scale(500,flow),scale(550,flow)]
ax.set_yticks(ticks_y)
Ticks_y = [6,7,5,4,3,2,1,350,400,450,500,550]
ax.set_yticklabels(Ticks_y)

##Titling the graph and axis
plt.title('Graph to show the flood event of the River Ouse (Skelton) in November 2000')
plt.text(-0.25, 1.0, 'Discharge,Q $[m^3/s]$',style='italic',size=10)
plt.text(0.75,-0.15, 't [day]',style='italic',size=10)
plt.text(-1.1, -0.15, 'Stage, h $[m]$',style='italic',size=10)
plt.text(-0.24,-1.09, 't [day]',style='italic', size=10)

plt.text(0.33, -0.5,'F.E.V≈?? $Mm^3$', style='italic', size=12)
plt.text(0.33, -0.55,'$T_f=??hrs$', style='italic', size=12)
plt.text(0.33, -0.6,'$h_T=??m$', style='italic', size=12)
plt.text(0.33, -0.65,'$h_m=??m$', style='italic', size=12)
plt.text(0.33, -0.7,'$Q_T=??m^3/s$',style='italic', size=12)
plt.text(0.33, -0.75,'$Q_m=??m^3/s$',style='italic', size=12)
