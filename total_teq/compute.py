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
import matplotlib.mlab as mlab
import numpy as np
import sys
import os, time, glob

qf = 0.06
qc = 0.14
yy = 0.051
k = 0.007
Fabs = 0.885
e = 0.9
ey = e*yy
Vf = 257.6
Vc = 1840- Vf
Vegg = 5.76

def main(contamination_level,feed_intake,exposure_time):

    def GivenDose(t):
        if t <= exposure_time:
                GivenDose = contamination_level*feed_intake*1000
        else:
                GivenDose = 0
        return GivenDose

    def myModel (y,t,GivenDose):
        dAcdt = Fabs*GivenDose(t)-(qc + k + ey)*y[0]+ qf*y[1]
        dAfdt = qc*y[0]-qf*y[1] 
        dAeggdt = yy*y[0]-y[2]
        return [dAcdt,dAfdt,dAeggdt]
        

    timeGrid = np.arange(0,250,0.01)
    delay = np.arange(1,251,0.01)
    GivenDose = (GivenDose,)
    yinit = np.array([0.0,0.0,0.0])
    y = odeint (myModel, yinit, timeGrid, GivenDose)
    ind = mlab.cross_from_above(y[:,2]/Vegg, 5)
    legal_lim = delay[ind]
    plt.figure()
    plt.plot(delay, y[:,2]/Vegg) # y[:,0] is the first column of y
    plt.plot([0, 250], [5, 5],'r')
    plt.xlim(0, 250)
    blue_patch = mpatches.Patch(color='blue', label='Total TEQ model: %s days'%(legal_lim))
    red_patch = mpatches.Patch(color='red', label='Legal limit')
    plt.legend(handles=[blue_patch,red_patch])
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
    int(sys.argv[1], sys.argv[2], sys.argv[3])
