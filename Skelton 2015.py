##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from decimal import Decimal


##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white'
 
##Assigning raw data to variables##
ouse = pd.read_csv('Skelton 2015.csv') 
day = ouse['Day in December 2015'] 
height = ouse['Stage'] 
flow = ouse['Flow']

##Defining h_t & h_m
h_T=5.87

HM = []
for i in height:
    if i>=h_T:
        HM.append(i)
h_m=sum(HM)/len(HM)

##Defining a polynomial fitting function
rtcrv=np.polyfit(height,flow,3)
p=np.poly1d(rtcrv)

Flow=list(p(height))

scaled_Flow = []
for i in Flow:
    scaled_Flow.append((i-min(Flow))/(max(Flow)-min(Flow)))

##Finding Q_T & Q_m
Q_T=p(h_T)
Q_m=p(h_m)
Q_max=p(max(height))

##Defining a scale function##
def scale(x,y):return ((x-min(y))/(max(y)-min(y)))

##Scaling variables in preparation for plotting as subplots##
scaled_day=(scale(day,day))
scaled_flow=(scale(flow,flow))
neg_scaled_height=-(scale(height,height))
neg_scaled_day=-(scaled_day)

##Scaling h_T,h_m,Q_T,Q_m
scaled_h_T=scale(h_T,height)
scaled_h_m=scale(h_m,height)
scaled_Q_T=scale(Q_T,Flow)
scaled_Q_m=scale(Q_m,Flow)


##Renaming command##
fig,ax=plt.subplots()

##Filling in region##
QT=[]
for i in scaled_Flow:
    i = float(scaled_Q_T)
    QT.append(i)
    
SF=np.array(scaled_Flow)
e=np.array(QT)
    
ax.fill_between(scaled_day,SF,e,where=SF>=e,facecolor='cornflowerblue')

##Finding T_f
idx = np.argwhere(np.diff(np.sign(SF - e))).flatten()

T_f1=scaled_day[idx[0]]
T_f2=scaled_day[idx[-1]]

T_f=(T_f2-T_f1)*(max(day)-min(day))*24*(60**2)

##Finding FEV using estimate 1
FEV1=(Q_m-Q_T)*T_f

##Finding FEV using estimate 2
time_increment=(day[1]-day[0])*24*3600

FLOW = []
for i in Flow:
    if i>=Q_T:
        FLOW.append((i-Q_T)*(time_increment))

FEV2=sum(FLOW)

FEV=max(FEV1,FEV2)

##Plotting subplots##
ax.plot(scaled_day,scaled_Flow,'black', linewidth=1)
ax.plot(scaled_day,scaled_flow,'grey', linewidth=0.5)
ax.plot(neg_scaled_height, scaled_flow,'+',color='grey',markersize=2)
ax.plot(neg_scaled_height,neg_scaled_day,'black', linewidth=1)
ax.plot(neg_scaled_height,scaled_Flow,'black',linewidth=1)

###FORMATTING###
##Centering and formatting axes##
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x',color='black',direction='out',length=10,width=1)
ax.tick_params(axis='y',color='black',direction='out',length=10,width=1)

##Scaling and Labelling axes
ticks_x=[-scale(6.5,height),-scale(6,height),-scale(5.5,height),-scale(5,height),-scale(4.5,height),scale(26,day),scale(27,day),scale(28,day),scale(29,day),scale(30,day),scale(31,day)]
ax.set_xticks(ticks_x)
Ticks_x = [6.5,6,5.5,5,4.5,26,27,28,29,30,31]
ax.set_xticklabels(Ticks_x)

ticks_y=[-scale(31,day),-scale(30,day),-scale(29,day),-scale(28,day),-scale(27,day),scale(250,flow),scale(300,flow),scale(350,flow),scale(400,flow),scale(450,flow),scale(500,flow),scale(550,flow)]
ax.set_yticks(ticks_y)
Ticks_y = [31,30,29,28,27,250,300,350,400,450,500,550]
ax.set_yticklabels(Ticks_y)

##Titling the graph and axis
plt.title('Graph to show the flood event of the River Ouse (Skelton) in December 2015')
plt.text(-0.15, 0.9, 'Q $[m^3/s]$',style='italic',size=11)
plt.text(0.9,-0.15, 't [day]',style='italic',size=11)
plt.text(-1.05, -0.15, 'h $[m]$',style='italic',size=11)
plt.text(-0.24,-0.9, 't [day]',style='italic', size=11)

##Plotting and labelling points of interest##
ax.plot([-scaled_h_T,-scaled_h_T],[-1,scaled_Q_T],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_h_m,-scaled_h_m],[-1,scaled_Q_m],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_h_T,1],[scaled_Q_T,scaled_Q_T],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_h_m,1],[scaled_Q_m,scaled_Q_m],'black',linestyle='--',linewidth=1)
ax.plot([T_f1,T_f1,T_f1],[scaled_Q_T,scaled_Q_m,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([T_f2,T_f2,T_f2],[scaled_Q_T,scaled_Q_m,-1/5], 'black', linestyle='--', linewidth=1)

plt.text(-scaled_h_T+1/100, -1,'$h_T$', size=11)
plt.text(-scaled_h_m+1/100, -1,'$h_m$', size=11)
plt.text(1, scaled_Q_m,'$Q_m$', size=11)
plt.text(1, scaled_Q_T,'$Q_T$', size=11)
plt.text(((T_f1+T_f2)/2)-1/50,-0.18,'$T_f$',size=11)

##Plotting a box to represent FEV2
ax.plot([T_f1,T_f2],[scaled_Q_T,scaled_Q_T], 'black',linewidth=1.5)
ax.plot([T_f1,T_f1],[scaled_Q_T,scaled_Q_m], 'black',linewidth=1.5)
ax.plot([T_f1,T_f2],[scaled_Q_m,scaled_Q_m], 'black',linewidth=1.5)
ax.plot([T_f2,T_f2],[scaled_Q_T,scaled_Q_m], 'black',linewidth=1.5)

##Displaying final values##
plt.text(0.33, -0.5,'FEV ≈'+ str(round((FEV)/(10**6),2))+ '$Mm^3$', style='italic', size=12)
plt.text(0.33, -0.575,'$T_f$ ='+str(round(T_f/(60**2),2))+'$hrs$', style='italic', size=12)
plt.text(0.33, -0.650,'$h_T$='+str(round(h_T,2))+'m', style='italic', size=12)
plt.text(0.33, -0.725,'$h_m$ ='+str(round(h_m,2))+'m', style='italic', size=12)
plt.text(0.33, -0.80,'$Q_T=$'+str(round(Q_T,1))+'$m^3/s$',style='italic', size=12)
plt.text(0.33, -0.875,'$Q_m=$'+str(round(Q_m,1))+'$m^3/s$',style='italic', size=12)


plt.annotate(s='', xy=(T_f1-1/100,-1/5), xytext=(T_f2+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))


