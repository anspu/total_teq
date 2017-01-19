# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.integrate import odeint
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
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

#1,2,3,7,8-PeCDF (c1)
qc_c2 = 0.14 
qf_c2 = 0.06
yy_c2 = 0.051
k_c2 = 0.007
Fabs_c2 = 0.885
ey_c2 = e*yy_c1
Vf_c2 = 257.6
Vc_c2 = 1840-Vf_c1

def main(c1, c2, feed_intake,exposure_time):
    contamination_level = c1+c2    
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
    print (main(2, 4, 3, 56))



    #int(sys.argv[1], sys.argv[2], sys.argv[3])