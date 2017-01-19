# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.integrate import odeint
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import sys
import os, time, glob

Vegg = 5.76
e = 0.9

#Total_teq_model
qc = 0.14
qf = 0.06
yy = 0.051
k = 0.007
Fabs = 0.885
ey = e*yy
Vf = 257.6
Vc = 1840- Vf

#2,3,7,8-TCDF (c1)
qc_c1 = 0.31
qf_c1 = 0.205
yy_c1 = 0.029
k_c1 = 0.012
Fabs_c1 = 0.7
ey_c1 = e*yy_c1
Vf_c1 = 280
Vc_c1 = 1840-Vf_c1

#1,2,3,7,8-PeCDF (c2)
qc_c2 = 0.14 
qf_c2 = 0.06
yy_c2 = 0.051
k_c2 = 0.007
Fabs_c2 = 0.885
ey_c2 = e*yy_c2
Vf_c2 = 257.6
Vc_c2 = 1840-Vf_c2

#1,2,3,7,8-PeCDF (c3)
qc_c3 = 0.14 
qf_c3 = 0.06
yy_c3 = 0.051
k_c3 = 0.007
Fabs_c3 = 0.885
ey_c3 = e*yy_c3
Vf_c3 = 257.6
Vc_c3 = 1840-Vf_c3

#1,2,3,7,8-PeCDF (c4)
qc_c4 = 0.14 
qf_c4 = 0.06
yy_c4 = 0.051
k_c4 = 0.007
Fabs_c4 = 0.885
ey_c4 = e*yy_c4
Vf_c4 = 257.6
Vc_c4 = 1840-Vf_c4

#1,2,3,7,8-PeCDF (c5)
qc_c5 = 0.14 
qf_c5 = 0.06
yy_c5 = 0.051
k_c5 = 0.007
Fabs_c5 = 0.885
ey_c5 = e*yy_c5
Vf_c5 = 257.6
Vc_c5 = 1840-Vf_c5

#1,2,3,7,8-PeCDF (c6)
qc_c6 = 0.14 
qf_c6 = 0.06
yy_c6 = 0.051
k_c6 = 0.007
Fabs_c6 = 0.885
ey_c6 = e*yy_c6
Vf_c6 = 257.6
Vc_c6 = 1840-Vf_c6

#1,2,3,7,8-PeCDF (c7)
qc_c7 = 0.14 
qf_c7 = 0.06
yy_c7 = 0.051
k_c7 = 0.007
Fabs_c7 = 0.885
ey_c7 = e*yy_c7
Vf_c7 = 257.6
Vc_c7 = 1840-Vf_c7

#1,2,3,7,8-PeCDF (c8)
qc_c8 = 0.14 
qf_c8 = 0.06
yy_c8 = 0.051
k_c8 = 0.007
Fabs_c8 = 0.885
ey_c8 = e*yy_c2
Vf_c8 = 257.6
Vc_c8 = 1840-Vf_c8

#1,2,3,7,8-PeCDF (c9)
qc_c9 = 0.14 
qf_c9 = 0.06
yy_c9 = 0.051
k_c9 = 0.007
Fabs_c9 = 0.885
ey_c9 = e*yy_c9
Vf_c9 = 257.6
Vc_c9 = 1840-Vf_c9

#1,2,3,7,8-PeCDF (c10)
qc_c10 = 0.14 
qf_c10 = 0.06
yy_c10 = 0.051
k_c10 = 0.007
Fabs_c10 = 0.885
ey_c10 = e*yy_c10
Vf_c10 = 257.6
Vc_c10 = 1840-Vf_c10

#1,2,3,7,8-PeCDF (c11)
qc_c11 = 0.14 
qf_c11 = 0.06
yy_c11 = 0.051
k_c11 = 0.007
Fabs_c11 = 0.885
ey_c11 = e*yy_c11
Vf_c11 = 257.6
Vc_c11 = 1840-Vf_c11

#1,2,3,7,8-PeCDF (c12)
qc_c12 = 0.14 
qf_c12 = 0.06
yy_c12 = 0.051
k_c12 = 0.007
Fabs_c12 = 0.885
ey_c12 = e*yy_c12
Vf_c12 = 257.6
Vc_c12 = 1840-Vf_c12

#1,2,3,7,8-PeCDF (c13)
qc_c13 = 0.14 
qf_c13 = 0.06
yy_c13 = 0.051
k_c13 = 0.007
Fabs_c13 = 0.885
ey_c13 = e*yy_c13
Vf_c13 = 257.6
Vc_c13 = 1840-Vf_c13

#1,2,3,7,8-PeCDF (c14)
qc_c14 = 0.14 
qf_c14 = 0.06
yy_c14 = 0.051
k_c14 = 0.007
Fabs_c14 = 0.885
ey_c14 = e*yy_c14
Vf_c14 = 257.6
Vc_c14 = 1840-Vf_c14

#1,2,3,7,8-PeCDF (c15)
qc_c15 = 0.14 
qf_c15 = 0.06
yy_c15 = 0.051
k_c15 = 0.007
Fabs_c15 = 0.885
ey_c15 = e*yy_c15
Vf_c15 = 257.6
Vc_c15 = 1840-Vf_c15


def main(feed_intake,exposure_time,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15):
    contamination_level = c1+c2+c3+c4+c5
    
    def GivenDose(t):
        if t <= exposure_time:
                GivenDose = contamination_level*feed_intake*1000
        else:
                GivenDose = 0
        return GivenDose
        
    def GivenDose_c1(t):
        if t <= exposure_time:
                GivenDose_c1 = c1*feed_intake*1000
        else:
                GivenDose_c1 = 0
        return  GivenDose_c1
    
    def GivenDose_c2(t):
        if t <= exposure_time:
                GivenDose_c2 = c2*feed_intake*1000
        else:
                GivenDose_c2 = 0
        return  GivenDose_c2
        
    def GivenDose_c3(t):
        if t <= exposure_time:
                GivenDose_c3 = c3*feed_intake*1000
        else:
                GivenDose_c3 = 0
        return  GivenDose_c3
        
    def GivenDose_c4(t):
        if t <= exposure_time:
                GivenDose_c4 = c4*feed_intake*1000
        else:
                GivenDose_c4 = 0
        return  GivenDose_c4
    
    def GivenDose_c5(t):
        if t <= exposure_time:
                GivenDose_c5 = c5*feed_intake*1000
        else:
                GivenDose_c5 = 0
        return  GivenDose_c5
    
    def GivenDose_c6(t):
        if t <= exposure_time:
                GivenDose_c6 = c6*feed_intake*1000
        else:
                GivenDose_c6 = 0
        return  GivenDose_c6
    
    def GivenDose_c7(t):
        if t <= exposure_time:
                GivenDose_c7 = c7*feed_intake*1000
        else:
                GivenDose_c7 = 0
        return  GivenDose_c7
        
    def GivenDose_c8(t):
        if t <= exposure_time:
                GivenDose_c8 = c8*feed_intake*1000
        else:
                GivenDose_c8 = 0
        return  GivenDose_c8
  
    def GivenDose_c9(t):
        if t <= exposure_time:
                GivenDose_c9 = c9*feed_intake*1000
        else:
                GivenDose_c9 = 0
        return  GivenDose_c9
   
    def GivenDose_c10(t):
        if t <= exposure_time:
                GivenDose_c10 = c10*feed_intake*1000
        else:
                GivenDose_c10 = 0
        return  GivenDose_c10
        
    def GivenDose_c11(t):
        if t <= exposure_time:
                GivenDose_c11 = c11*feed_intake*1000
        else:
                GivenDose_c11 = 0
        return  GivenDose_c11
    
    def GivenDose_c12(t):
        if t <= exposure_time:
                GivenDose_c12 = c12*feed_intake*1000
        else:
                GivenDose_c12 = 0
        return  GivenDose_c12
        
    def GivenDose_c13(t):
        if t <= exposure_time:
                GivenDose_c13 = c13*feed_intake*1000
        else:
                GivenDose_c13 = 0
        return  GivenDose_c13
        
    def GivenDose_c14(t):
        if t <= exposure_time:
                GivenDose_c14 = c14*feed_intake*1000
        else:
                GivenDose_c14 = 0
        return  GivenDose_c14
    
    def GivenDose_c15(t):
        if t <= exposure_time:
                GivenDose_c15 = c15*feed_intake*1000
        else:
                GivenDose_c15 = 0
        return  GivenDose_c15

    def myModel (y,t,GivenDose):
        dAcdt = Fabs*GivenDose(t)-(qc + k + ey)*y[0]+ qf*y[1]
        dAfdt = qc*y[0]-qf*y[1] 
        dAeggdt = yy*y[0]-y[2]
        
        dAcdt1 = Fabs_c1*GivenDose_c1(t)-(qc_c1 + k_c1 + ey_c1)*y[3]+ qf_c1*y[4]
        dAfdt1 = qc_c1*y[3]-qf_c1*y[4] 
        dAeggdt1 = yy_c1*y[3]-y[5]
        
        dAcdt2 = Fabs_c1*GivenDose_c2(t)-(qc_c1 + k_c1 + ey_c1)*y[6]+ qf_c1*y[7]
        dAfdt2 = qc_c1*y[6]-qf_c1*y[7] 
        dAeggdt2 = yy_c1*y[6]-y[8]
        
        return [dAcdt,dAfdt,dAeggdt,dAcdt1,dAfdt1,dAeggdt1,dAcdt2,dAfdt2,dAeggdt2]
        

    timeGrid = np.arange(0,400,0.01)
    GivenDose = (GivenDose,)
    yinit = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    (y,d) = odeint (myModel, yinit, timeGrid, GivenDose, full_output=1)
    plt.figure()
    plt.plot(timeGrid, y[:,2]/Vegg) # y[:,0] is the first column of y
    plt.plot(timeGrid, (y[:,5]+y[:,8])/Vegg)
    blue_patch = mpatches.Patch(color='blue', label='Total teq model')
    green_patch = mpatches.Patch(color='green', label='Congener specific models')
    plt.legend(handles=[blue_patch, green_patch])
    plt.xlabel('time (days)')
    plt.ylabel('Cegg (pg TEQ/g yolk fat)')
    
    if not os.path.isdir('static'):
            os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
        plotfile = os.path.join('static', str(time.time()) + '.png')
        plt.savefig(plotfile)
        return plotfile

pass
if __name__ == '__main__':
    int(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4],
        sys.argv[5],sys.argv[6], sys.argv[7],sys.argv[8],
        sys.argv[9], sys.argv[10], sys.argv[11],sys.argv[12],
        sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16], sys.argv[17])
