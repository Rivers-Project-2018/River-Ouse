##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white' 
 
##Assigning raw data to variables##
calder=pd.read_csv('A.F_River_Calder_Mytholmroyd_2015_Data.csv') 
day = calder['Day in December '] 
height = calder['Height/m'] 
 
##Defining a scale function##
def scale(x,y):return((x-min(y))/(max(y)-min(y)))

##Defining ht and finding hm##
ht=4.5
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

##Defining a flow function Q(x) using the Rating Curve##
def Q(x):
    if 0.342<=x<=2.107:
        y = (8.459*((x-0.342)**2.239))
    elif 2.107<=x<=3.088:
        y = (21.5*((x-0.826)**1.37))
    elif 3.088<=x<=max(height):
        y = (2.086*((x+0.856)**2.515))
    return(y)
qt = Q(ht)
qm = Q(hm)   

##Generating a list of Flow variables from height##
Flow = []
for i in height:
    if 0.342<=i<=2.107:
        Flow.append(8.459*((i-0.342)**2.239))
    elif 2.107<=i<=3.088:
        Flow.append(21.5*((i-0.826)**1.37))
    elif 3.088<=i<=max(height):
        Flow.append(2.086*((i+0.856)**2.515))

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
ax.plot([0,-1],[0,1], 'darkorange',linestyle='--',marker='',linewidth=1.5)


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
position_x_ticks=[-533/638,-2731/4466,-1731/4466,-731/4466,0,1/4,2/4,3/4,1]
position_y_ticks=[-1,-3/4,-2/4,-1/4,0,2143/11593,4643/11593,7143/11593,9643/11593]
ax.set_xticks(position_x_ticks)
ax.set_yticks(position_y_ticks)
label_x_ticks=[5,4,3,2,25,26,27,28,29]
label_y_ticks=[29,28,27,26,0,50,100,150,200]
ax.set_xticklabels(label_x_ticks)
ax.set_yticklabels(label_y_ticks)

##Giving the graph a title and labelling the axes##
plt.title('Graph to show the flood event of the River Calder (Mytholmroyd) in December 2015',size=12)
plt.text(0.05, 1.05, 'Q $[m^3/s]$',style='italic',size=10)
plt.text(0.75,-0.15, 't [day]',style='italic',size=10)
plt.text(-1.1, -0.15, 'Stage $[m]$',style='italic',size=10)
plt.text(-0.35,-1.09, 't [day]',style='italic', size=10)

##Defining points of interest on the graph##
scaled_ht=scale(4.50,height)
scaled_hm=scale(5.25,height)
scaled_qt=scale(142.0,Flow)
scaled_qm=scale(197.5,Flow)

##Highlighting and labelling regions of interest##
ax.plot([-scaled_ht,-scaled_ht],[-1,scaled_qt],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_hm,-scaled_hm],[-1,scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_ht,1],[scaled_qt,scaled_qt],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_hm,1],[scaled_qm,scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([scale(26.34375,day),scale(26.34375,day)],[-0.2, scaled_qm],'black',linestyle='--',linewidth=1)
ax.plot([scale(26.677083,day),scale(26.677083,day)],[-0.2, scaled_qm],'black',linestyle='--',linewidth=1)
plt.text(-scaled_ht, -1.05, '$h_T$', style='italic', size=11)
plt.text(-scaled_hm, -1.05, '$h_m$', style='italic', size=11)
plt.text(1.05, scaled_qt, '$Q_T$', style='italic', size=11)
plt.text(1.05, scaled_qm, '$Q_m$', style='italic', size=11)
plt.text(0.36,-0.25,'$T_f$',style='italic', size=11)

##Plotting an area which estimates the F.E.V##
##Vertices of square F.E.V region were found by manually extrapolating data points with values closest to h_m,h_T, Q_m and Q_T##
##Data values were then scaled##
ax.plot([scale(26.34375,day),scale(26.34375,day)],[scaled_qt, scaled_qm],'black',linewidth=2)
ax.plot([scale(26.677083,day),scale(26.677083,day)],[scaled_qt, scaled_qm],'black',linewidth=2)
ax.plot([scale(26.34375,day),scale(26.677083,day)],[scaled_qt, scaled_qt],'black',linewidth=2)
ax.plot([scale(26.34375,day),scale(26.677083,day)],[scaled_qm, scaled_qm],'black',linewidth=2)
plt.text(0.5,0.7,'F.E.V',style='italic', size=11)

##Listing important variables in the bottom-right quandrant##
plt.text(0.33, -0.5,'F.E.V≈1.65 $Mm^3$', style='italic', size=12)
plt.text(0.33, -0.55,'$T_f=8.25hrs$', style='italic', size=12)
plt.text(0.33, -0.6,'$h_T=4.50m$', style='italic', size=12)
plt.text(0.33, -0.65,'$h_m=5.25m$', style='italic', size=12)
plt.text(0.33, -0.7,'$Q_T=142.0 m^3/s$',style='italic', size=12)
plt.text(0.33, -0.75,'$Q_m=197.5 m^3/s$',style='italic', size=12)

##Filling in the F.E.V by formatting qt into a list and then array inorder to use ax.fill_between() function##
QT=[]
for i in scaledFlow:
    i = scaled_qt
    QT.append(i)

a=np.array(scaledFlow)
b=np.array(QT)

ax.fill_between(scaled_day,a,b,where=a>=b,facecolor='darkorange')
