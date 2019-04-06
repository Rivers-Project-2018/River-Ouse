##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white'
 
##Assigning raw data to variables##
ouse = pd.read_csv('Skelton 2015.csv') 
day = ouse['Day'] 
height = ouse['Stage'] 
flow = ouse['Flow']

##Defining h_t & h_m
h_T=6.17


##Defining a polynomial fitting function
rtcrv=np.polyfit(height,flow,3)
p=np.poly1d(rtcrv)

Flow=list(p(height))

scaled_Flow = []
for i in Flow:
    scaled_Flow.append((i-min(Flow))/(max(Flow)-min(Flow)))

##Finding Q_T & Q_m
Q_T=p(h_T)


##Defining a scale function##
def scale(x,y):return ((x-min(y))/(max(y)-min(y)))

##Scaling variables in preparation for plotting as subplots##
scaled_day=(scale(day,day))
scaled_flow=(scale(flow,flow))
neg_scaled_height=-(scale(height,height))
neg_scaled_day=-(scaled_day)

##Scaling h_T,h_m,Q_T,Q_m
scaled_h_T=scale(h_T,height)
scaled_Q_T=scale(Q_T,Flow)



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


##Finding FEV##
time_increment=(day[1]-day[0])*24*3600

FLOW = []
for i in Flow:
    if i>=Q_T:
        FLOW.append((i-Q_T)*(time_increment))

FEV=sum(FLOW)

##Defining Q_m and h_m##
Q_m=Flow-Q_T
scaled_Q_m=scale(Q_m,Flow)

##Plotting subplots##
ax.plot(scaled_day,scaled_Flow,'black', linewidth=1.5)
ax.plot(scaled_day,scaled_flow,'none', linewidth=0.5)
ax.plot(neg_scaled_height, scaled_flow,'+',color='none',markersize=1)
ax.plot(neg_scaled_height,neg_scaled_day,'black', linewidth=1.5)
ax.plot(neg_scaled_height,scaled_Flow,color='cornflowerblue',linewidth=1.25)

###FORMATTING###
##Centering and formatting axes##
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x',color='black',direction='out',length=10,width=1)
ax.tick_params(axis='y',color='black',direction='out',length=10,width=1)

##Scaling and Labelling axes
ticks_x=[-scale(6.5,height),-scale(6,height),-scale(5.5,height),-scale(5,height),-scale(4.5,height),scale(0,day),scale(1,day),scale(2,day),scale(3,day),scale(4,day),scale(5,day)]
ax.set_xticks(ticks_x)
Ticks_x = [6.5,6,5.5,5,4.5,0,1,2,3,4,5]
ax.set_xticklabels(Ticks_x)

ticks_y=[-scale(5,day),-scale(4,day),-scale(3,day),-scale(2,day),-scale(1,day),scale(250,Flow),scale(300,Flow),scale(350,Flow),scale(400,Flow),scale(450,Flow),scale(500,Flow),scale(550,Flow)]
ax.set_yticks(ticks_y)
Ticks_y = [5,4,3,2,1,250,300,350,400,450,500,550]
ax.set_yticklabels(Ticks_y)

##Titling the graph and axis
plt.title('Graph to show the flood event of the River Ouse (Skelton) in December 2015',size=14)
plt.text(-0.25, 0.92, 'Q $[m^3/s]$',style='italic',size=12)
plt.text(0.9,-0.15, 't [day]',style='italic',size=12)
plt.text(-1.05, -0.15, '$\overline {h}$ $[m]$',style='italic',size=12)
plt.text(-0.24,-0.9, 't [day]',style='italic', size=12)

##Plotting and labelling points of interest##
ax.plot([-scaled_h_T,-scaled_h_T],[-1,scaled_Q_T],'black',linestyle='--',linewidth=1)
#ax.plot([-scaled_h_m,-scaled_h_m],[-1,scaled_Q_m],'black',linestyle='--',linewidth=1)
ax.plot([-scaled_h_T,1],[scaled_Q_T,scaled_Q_T],'black',linestyle='--',linewidth=1)
#ax.plot([-scaled_h_m,1],[scaled_Q_m,scaled_Q_m],'black',linestyle='--',linewidth=1)
#ax.plot([T_f1,T_f1,T_f1],[scaled_Q_T,scaled_Q_m,-1/5], 'black', linestyle='--', linewidth=1)
#ax.plot([T_f2,T_f2,T_f2],[scaled_Q_T,scaled_Q_m,-1/5], 'black', linestyle='--', linewidth=1)

plt.text(-scaled_h_T+1/100, -1,'$h_T$', size=12)
#plt.text(-scaled_h_m+1/100, -1,'$h_m$', size=12)
#plt.text(1, scaled_Q_m,'$Q_m$', size=12)
plt.text(1, scaled_Q_T,'$Q_T$', size=12)
plt.text(((T_f1+T_f2)/2)-1/50,-0.18,'$T_f$',size=12)

##Plotting a box to represent FEV2
ax.plot([T_f1,T_f2],[scaled_Q_T,scaled_Q_T], 'black',linewidth=1.5)
#ax.plot([T_f1,T_f1],[scaled_Q_T,scaled_Q_m], 'black',linewidth=1.5)
#ax.plot([T_f1,T_f2],[scaled_Q_m,scaled_Q_m], 'black',linewidth=1.5)
#ax.plot([T_f2,T_f2],[scaled_Q_T,scaled_Q_m], 'black',linewidth=1.5)

##Displaying final values##
plt.text(0.33, -0.5,'FEV ≈'+ str(round((FEV)/(10**6),2))+ '$Mm^3$', style='italic', size=12)
plt.text(0.33, -0.575,'$T_f$ ='+str(round(T_f/(60**2),2))+'$hrs$', style='italic', size=12)
plt.text(0.33, -0.650,'$h_T$='+str(round(h_T,2))+'m', style='italic', size=12)
#plt.text(0.33, -0.725,'$h_m$ ='+str(round(h_m,2))+'m', style='italic', size=12)
plt.text(0.33, -0.80,'$Q_T=$'+str(round(Q_T,1))+'$m^3/s$',style='italic', size=12)
#plt.text(0.33, -0.875,'$Q_m=$'+str(round(Q_m,1))+'$m^3/s$',style='italic', size=12)


plt.annotate(s='', xy=(T_f1-1/100,-1/5), xytext=(T_f2+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))


##Plotting the Squarelake##
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1)*0.7)
ax = Axes3D(fig)

plt.rcParams['axes.edgecolor']='white'
plt.rcParams["figure.figsize"] = [10,8]

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

sl = (FEV/2)**(0.5)

v_1= [sl, sl]
v_2= [sl, sl]
v_3= [2, 0]

v_4= [sl, 0]
v_5 = [sl, sl]
v_6 = [0, 0]

v_7 = [sl, sl]
v_8= [sl, 0]
v_9 = [0, 0]

ax.plot(v_1, v_2, v_3, '--', color = 'k')
ax.plot(v_4, v_5, v_6, '--', color = 'k')
ax.plot(v_7, v_8, v_9, '--', color = 'k')

x = [sl, sl, sl, 0, 0, 0, sl, sl, 0, 0, 0, 0]
y = [sl, 0, 0, 0, 0, sl, sl, 0, 0, 0, sl, sl]
z = [2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2]

ax.plot(x, y, z, color = 'k')

ax.text(sl/2, -sl/2, 0, 'Side-length [m]',style='italic', size=12)
ax.text(-sl/4,sl/4,0, 'Side-length [m]', style='italic',size=12)
ax.text(-0.02*sl, 1.01*sl,0.8, 'Depth [m]',style='italic',size=12)

ax.text(sl/1.7,sl/2.2,1,'('+str(int(round(sl)))+' m)$^2$', size=14)

ax.set_zticks([0, 2])

ax.set_xlim(sl,0)
ax.set_ylim(0,sl)
ax.set_zlim(0,10)
