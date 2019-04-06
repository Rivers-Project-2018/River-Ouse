##Importing matplotlib, pandas and numpy##
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import bisect

##Defining the characteristics of the graph parameters##
plt.rcParams["figure.figsize"] = [10,10] 
plt.rcParams['axes.edgecolor']='white'
 
##Assigning raw data to variables##
ouse = pd.read_csv('Skelton 2000.csv') 
time = ouse['Day'] 
height = ouse['Stage'] 
flow = ouse['Flow']

##Formatting the graph
fig, ax = plt.subplots()
plt.rcParams['axes.edgecolor']='white'
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

##Defining h_t & h_m
h_T=6.17
HM = []
for i in height:
    if i>=h_T:
        HM.append(i)
h_m=sum(HM)/len(HM)
##Defining a polynomial fitting function
rtcrv=np.polyfit(height,flow,4)
print(rtcrv)
p=np.poly1d(rtcrv)
Q_T=p(h_T)
Q_m=p(h_m)

time_increment=(time[1]-time[0])*24*3600

number_of_days=int((len(time)*(time[1]-time[0])))

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))

scaledtime=scale(time)
scaledheight=scale(height)

    
Flow = list(p(height))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))

negheight=-scaledheight
negday=-(scaledtime)

#To change the colour, change 'conrflowerblue' to another colour such as 'pink'.
ax.plot(negheight,scaledFlow,'black',linewidth=1.5)
ax.plot([0,-1],[0,1],'firebrick',linestyle='--',marker='',linewidth=1.5)
ax.plot(scaledtime, scaledFlow,'black',linewidth=1.5)
ax.plot(negheight, negday,'black',linewidth=1.5)

scaledht = (h_T-min(height))/(max(height)-min(height))
scaledhm = (h_m-min(height))/(max(height)-min(height))
scaledqt = (Q_T-min(Flow))/(max(Flow)-min(Flow))
scaledqm = (Q_m-min(Flow))/(max(Flow)-min(Flow))


QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)

SF=np.array(scaledFlow)
e=np.array(QT)
    
ax.fill_between(scaledtime,SF,e,where=SF>=e,facecolor='firebrick')

idx = np.argwhere(np.diff(np.sign(SF - e))).flatten()

f=scaledtime[idx[0]]
g=scaledtime[idx[-1]]

def unscaletime(x):
    return (((max(time)-min(time))*x)+min(time))

time_increment=(time[1]-time[0])*24*3600

flow = []
for i in Flow:
    if i>=Q_T:
        flow.append((i-Q_T)*(time_increment))

FEV=sum(flow)

Tfa1=(1.575-min(time))/(max(time)-min(time))
Tfa2=(6.415-min(time))/(max(time)-min(time))
Tfa=(Tfa2-Tfa1)
Tfb1=(8.155-min(time))/(max(time)-min(time))
Tfb2=(10.465-min(time))/(max(time)-min(time))
Tfb=(Tfb2-Tfb1)


ax.plot([-scaledht,-scaledht],[-1,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm],'black',linestyle='--',linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm],'black',linestyle='--',linewidth=1)

ax.plot([Tfa1,Tfa1],[-1/5, scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([Tfa2,Tfa2],[-1/5, scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([Tfb1,Tfb1],[-1/5, scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([Tfb2,Tfb2],[-1/5, scaledqt],'black',linestyle='--',linewidth=1)

ax.plot([Tfa1,Tfa1],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfa2,Tfa2],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfa1,Tfa2],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfa1,Tfa2],[scaledqm,scaledqm], 'black',linewidth=1.5)

ax.plot([Tfb1,Tfb1],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfb2,Tfb2],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfb1,Tfb2],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([Tfb1,Tfb2],[scaledqm,scaledqm], 'black',linewidth=1.5)


plt.annotate(s='', xy=(Tfa1-1/100,-1/5), xytext=(Tfa2+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))
plt.annotate(s='', xy=(Tfb1-1/100,-1/5), xytext=(Tfb2+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))

h=[]
for i in np.arange(1,number_of_days+1):
    h.append(i/number_of_days)

#If you wish to set the flow to be shown on the axis by a certain increment, change all 
#appearances of 50 in lines 153 and 157 to the desired increment, e.g 25 or 100.
#Otherwise leave as is.
l=np.arange(0,max(Flow)+50,50)
m=bisect.bisect(l,min(Flow))

n=[]
for i in np.arange(l[m],max(Flow)+50,50):
    n.append(int(i))

#If you wish to set the height to be shown on the axis by a certain increment, change all 
#appearances of 1 in lines 163 and 167 to the desired increment, e.g 0.25 or 0.5.
#Otherwise leave as is.
o=np.arange(0,max(height)+1,1)
p=bisect.bisect(o,min(height))

q=[]
for i in np.arange(o[p],max(height)+1,1):
    q.append(i)

k=[]
for i in q:
    k.append(-(i-min(height))/(max(height)-min(height))) 

j=[]
for i in n:
    j.append((i-min(Flow))/(max(Flow)-min(Flow)))

ticks_x=k+h

r=[]
for i in h:
    r.append(-i)

ticks_y=r+j


s=[]
for i in np.arange(1,number_of_days+1):
    s.append(i)

Ticks_x=q+s
Ticks_y=s+n
    
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)

ax.tick_params(axis='x',colors='black',direction='out',length=9,width=1)
ax.tick_params(axis='y',colors='black',direction='out',length=10,width=1)

plt.text(-scaledht+1/100, -1,'$h_T$', size=13)
plt.text(-scaledhm+1/100, -1,'$h_m$', size=13)
plt.text(1, scaledqm,'$Q_m$', size=13)
plt.text(1, scaledqt,'$Q_T$', size=13)
plt.text(((Tfa1+Tfa2)/2)-1/50,-0.18,'$T_{fa}$',size=13)
plt.text(((Tfb1+Tfb2)/2)-1/50,-0.18,'$T_{fb}$',size=13)


plt.text(0.01, 1.05,'$\hat{Q}$ [m$^3$/s]', size=13)
plt.text(0.95, -0.17,'$t$ [day]', size=13)
plt.text(0.01, -1.09,'$t$ [day]', size=13)
plt.text(-1.1, 0.02,'$\overline {h}$ [m]', size=13)

ax.scatter(0,0,color='white')

T_f=unscaletime(Tfa+Tfb)*24

A=round(FEV/(10**6),2)
B=round(T_f,2)
B1=round(Tfa,2)
B2=round(Tfb,2)
C=round(h_T,2)
D=round(h_m,2)
E=round(Q_T,1)
F=round(Q_m,1)

plt.text(0.4,-0.4,'$FEV$ ≈ '+ str(A) +'Mm$^3$', size=14)
plt.text(0.4,-0.475,'$T_f$ = '+ str(B) +'hrs', size=14)
plt.text(0.4,-0.55,'$h_T$ = '+ str(C) +'m', size=14)
plt.text(0.4,-0.625,'$h_m$ = '+ str(D) +'m', size=14)
plt.text(0.4,-0.7,'$Q_T$ = '+ str(E) +'m$^3$/s', size=14)
plt.text(0.4,-0.775,'$Q_m$ = '+ str(F) +'m$^3$/s', size=14)


#Plotting the Squarelake##
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1)*0.7)
ax = Axes3D(fig)


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

ax.text(sl/2, -sl/2, 0, 'Side-length [m]',style='italic', size=13)
ax.text(-sl/4,sl/4,0, 'Side-length [m]', style='italic',size=13)
ax.text(-0.02*sl, 1.01*sl,0.8, 'Depth [m]',style='italic',size=13)

ax.text(sl/1.7,sl/2.2,1,'('+str(int(round(sl)))+' m)$^2$', size=14)

ax.set_zticks([0, 2])

ax.set_xlim(sl,0)
ax.set_ylim(0,sl)
ax.set_zlim(0,10)

FEV1=FEV
FEV2=(Q_m-Q_T)*T_f*60*60
print('percentage difference='+str((FEV2-FEV1)/FEV1*100))
