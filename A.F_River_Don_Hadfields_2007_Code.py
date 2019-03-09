##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white' 
 
##Assigning raw data to variables##
don=pd.read_csv('A.F_River_Don_Hadfields_2007_Data.csv') 
day = don['Day in June'] 
height = don['Height/m'] 
 
##Defining a scale function##
def scale(x,y):return((x-min(y))/(max(y)-min(y)))

##Defining ht and finding hm##
ht=2.9
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

##Defining a flow function Q(x) using the Rating Curve##
def Q(x):
    if 0<=x<=0.52:
        y = (78.4407*((x-0.223)**1.7742))
    elif 0.52<=x<=0.931:
        y = (77.2829*((x-0.3077)**1.3803))
    elif 0.931<=x<=1.436:
        y = (79.5956*((x-0.34)**1.2967))
    elif 1.436<=x<=max(height):
        y = (41.3367*((x+0.5767)**1.1066))
    return(y)
qt = Q(ht)
qm = Q(hm)   

##Generating a list of Flow variables from height##
Flow = []
for i in height:
    if 0<=i<=0.52:
        Flow.append(78.4407*((i-0.223)**1.7742))
    elif 0.52<=i<=0.931:
        Flow.append(77.2829*((i-0.3077)**1.3803))
    elif 0.931<=i<=1.436:
        Flow.append(79.5956*((i-0.34)**1.2967))
    elif 1.436<=i<=max(height):
        Flow.append(41.3367*((i+0.5767)**1.1066))
        
##Scaling variables in preparation for plotting as subplots##     
scaled_day=scale(day,day)
scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))
neg_scaled_height=-(scale(height,height))
neg_scaled_day=-(scaled_day)

##Renaming command##
fig,ax=plt.subplots()

##Plotting subplots##
ax.plot(scaled_day,scaledFlow,'black', linewidth=2)
ax.plot(neg_scaled_height, scaledFlow,'black', linewidth=2)
ax.plot(neg_scaled_height,neg_scaled_day,'black', linewidth=2)
ax.plot([0,-1],[0,1], 'mediumslateblue',linestyle='--',marker='',linewidth=1.5)

##Centering and formatting axes##
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x',color='black',direction='out',length=10,width=1)
ax.tick_params(axis='y',color='black',direction='out',length=10,width=1)

##Labelling the axis by scaling them in each quadrant. Tick locations calculated by the following equation##
##f(x)=((intended tick label value)-min(variable)/(max(variable)-min(variable))) where variable can be day,flow,heigh##
##Where axis are reversed, the above function was negated.##
##Each quadrant was considered independently##
position_x_ticks=[-3481/4156,-2481/4156,-1481/4156,-481/4156,0,1/4,2/4,3/4,1]
position_y_ticks=[-1,-3/4,-2/4,-1/4,0,1024/6249,758/2083,3524/6249,4774/6249,2008/2038]
ax.set_xticks(position_x_ticks)
ax.set_yticks(position_y_ticks)
label_x_ticks=[4,3,2,1,25,26,27,28,29]
label_y_ticks=[29,28,27,26,0,50,100,150,200,250]
ax.set_xticklabels(label_x_ticks)
ax.set_yticklabels(label_y_ticks)

##Giving the graph a title and labelling the axes##
plt.title('Graph to show the flood event of the River Don (Hadfields)in June 2007',size=12)
plt.text(0.05, 1.05, 'Q $[m^3/s]$',style='italic',size=10)
plt.text(0.75,-0.15, 't [day]',style='italic',size=10)
plt.text(-1.1, -0.15, 'Stage $[m]$',style='italic',size=10)
plt.text(-0.35,-1.09, 't [day]',style='italic', size=10)

##Defining points of interest on the graph##
scaled_ht=scale(2.90,height)
scaled_hm=scale(4.06,height)
scaled_qt=scale(164.1,Flow)
scaled_qm=scale(225.9,Flow)

##Highlighting and labelling regions of interest##
ax.plot([-scaled_ht,-scaled_ht],[-1,scaled_qt],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_hm,-scaled_hm],[-1,scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_ht,1],[scaled_qt,scaled_qt],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_hm,1],[scaled_qm,scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([scale(25.5,day),scale(25.5,day)],[-0.2, scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([scale(26.072917,day),scale(26.072917,day)],[-0.2, scaled_qm],'black',linestyle='--',linewidth=1)
plt.text(-scaled_ht, -1.05, '$h_T$', style='italic', size=11)
plt.text(-scaled_hm, -1.05, '$h_m$', style='italic', size=11)
plt.text(1.05, scaled_qt, '$Q_T$', style='italic', size=11)
plt.text(1.05, scaled_qm, '$Q_m$', style='italic', size=11)
plt.text(0.18,-0.25,'$T_f$',style='italic', size=11)


##Plotting an area which estimates the F.E.V##
##Vertices of square F.E.V region were found by manually extrapolating data points with values closest to h_m,h_T, Q_m and Q_T##
##Data values were then scaled##
ax.plot([scale(25.5,day),scale(25.5,day)],[scaled_qt, scaled_qm],'black',linewidth=2)
ax.plot([scale(26.072917,day),scale(26.072917,day)],[scaled_qt, scaled_qm],'black',linewidth=2)
ax.plot([scale(25.5,day),scale(25.5,day)],[scaled_qt, scaled_qt],'black',linewidth=2)
ax.plot([scale(25.5,day),scale(26.072917,day)],[scaled_qm, scaled_qm],'black',linewidth=2)
plt.text(0.5,0.7,'F.E.V',style='italic', size=11)

##Listing important variables in the bottom-right quandrant##
plt.text(0.33, -0.5,'F.E.V≈3.00 $Mm^3$', style='italic', size=12)
plt.text(0.33, -0.55,'$T_f=13.50hrs$', style='italic', size=12)
plt.text(0.33, -0.6,'$h_T=2.90m$', style='italic', size=12)
plt.text(0.33, -0.65,'$h_m=4.06m$', style='italic', size=12)
plt.text(0.33, -0.7,'$Q_T=164.1 m^3/s$',style='italic', size=12)
plt.text(0.33, -0.75,'$Q_m=225.9 m^3/s$',style='italic', size=12)

##Filling in the F.E.V by formatting qt into a list and then array inorder to use ax.fill_between() function##
QT=[]
for i in scaledFlow:
    i = scaled_qt
    QT.append(i)

a=np.array(scaledFlow)
b=np.array(QT)

ax.fill_between(scaled_day,a,b,where=a>=b,facecolor='mediumslateblue')