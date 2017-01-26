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
tef_c1=0.1
qc_c1 = 0.14
qf_c1 = 0.06
yy_c1 = 0.051
k_c1 = 0.007
Fabs_c1 = 0.885
ey_c1 = e*yy_c1
Vf_c1 = 257.6
Vc_c1 = 1840-Vf_c1

#1,2,3,7,8-PeCDF (c2)
tef_c2 = 0.03
qc_c2 = 0.14 
qf_c2 = 0.06
yy_c2 = 0.051
k_c2 = 0.007
Fabs_c2 = 0.885
ey_c2 = e*yy_c2
Vf_c2 = 257.6
Vc_c2 = 1840-Vf_c2

#1,2,3,7,8-PeCDF (c3)
tef_c3 = 0.3
qc_c3 = 0.14 
qf_c3 = 0.06
yy_c3 = 0.051
k_c3 = 0.007
Fabs_c3 = 0.885
ey_c3 = e*yy_c3
Vf_c3 = 257.6
Vc_c3 = 1840-Vf_c3

#1,2,3,4,7,8-HxCDF (c4)
tef_c4 = 0.1
qc_c4 = 0.14 
qf_c4 = 0.06
yy_c4 = 0.051
k_c4 = 0.007
Fabs_c4 = 0.885
ey_c4 = e*yy_c4
Vf_c4 = 257.6
Vc_c4 = 1840-Vf_c4

#1,2,3,6,7,8-HxCDF (c5)
tef_c5 = 0.1
qc_c5 = 0.14 
qf_c5 = 0.06
yy_c5 = 0.051
k_c5 = 0.007
Fabs_c5 = 0.885
ey_c5 = e*yy_c5
Vf_c5 = 257.6
Vc_c5 = 1840-Vf_c5

#2,3,4,6,7,8-HxCDF (c6)
tef_c6 =0.1
qc_c6 = 0.14 
qf_c6 = 0.06
yy_c6 = 0.051
k_c6 = 0.007
Fabs_c6 = 0.885
ey_c6 = e*yy_c6
Vf_c6 = 257.6
Vc_c6 = 1840-Vf_c6

#1,2,3,7,8,9-HxCDF  (c7)
tef_c7 = 0.1
qc_c7 = 0.14 
qf_c7 = 0.06
yy_c7 = 0.051
k_c7 = 0.007
Fabs_c7 = 0.885
ey_c7 = e*yy_c7
Vf_c7 = 257.6
Vc_c7 = 1840-Vf_c7

#1,2,3,4,6,7,8-HpCDF (c8)
tef_c8  =0.01
qc_c8 = 0.14 
qf_c8 = 0.06
yy_c8 = 0.051
k_c8 = 0.007
Fabs_c8 = 0.885
ey_c8 = e*yy_c8
Vf_c8 = 257.6
Vc_c8 = 1840-Vf_c8

#1,2,3,4,7,8,9-HpCDF (c9)
tef_c9 =0.01
qc_c9 = 0.14 
qf_c9 = 0.06
yy_c9 = 0.051
k_c9 = 0.007
Fabs_c9 = 0.885
ey_c9 = e*yy_c9
Vf_c9 = 257.6
Vc_c9 = 1840-Vf_c9

#1,2,3,4,6,7,8,9-OCDF (c10)
tef_c10 =0.0003
qc_c10 = 0.14 
qf_c10 = 0.06
yy_c10 = 0.051
k_c10 = 0.007
Fabs_c10 = 0.885
ey_c10 = e*yy_c10
Vf_c10 = 257.6
Vc_c10 = 1840-Vf_c10

#2,3,7,8-TCDD (c11)
tef_c11 =1
qc_c11 = 0.14 
qf_c11 = 0.06
yy_c11 = 0.051
k_c11 = 0.007
Fabs_c11 = 0.885
ey_c11 = e*yy_c11
Vf_c11 = 257.6
Vc_c11 = 1840-Vf_c11

#1,2,3,7,8-PeCDD(c12)
tef_c12 =1 
qc_c12 = 0.14 
qf_c12 = 0.06
yy_c12 = 0.051
k_c12 = 0.007
Fabs_c12 = 0.885
ey_c12 = e*yy_c12
Vf_c12 = 257.6
Vc_c12 = 1840-Vf_c12

#1,2,3,4,7,8-HxCDD (c13)
tef_c13 =0.1
qc_c13 = 0.14 
qf_c13 = 0.06
yy_c13 = 0.051
k_c13 = 0.007
Fabs_c13 = 0.885
ey_c13 = e*yy_c13
Vf_c13 = 257.6
Vc_c13 = 1840-Vf_c13

#1,2,3,6,7,8-HxCDD (c14)
tef_c14 = 0.1
qc_c14 = 0.14 
qf_c14 = 0.06
yy_c14 = 0.051
k_c14 = 0.007
Fabs_c14 = 0.885
ey_c14 = e*yy_c14
Vf_c14 = 257.6
Vc_c14 = 1840-Vf_c14

#1,2,3,7,8,9-HxCDD (c15)
tef_c15 =0.1
qc_c15 = 0.14 
qf_c15 = 0.06
yy_c15 = 0.051
k_c15 = 0.007
Fabs_c15 = 0.885
ey_c15 = e*yy_c15
Vf_c15 = 257.6
Vc_c15 = 1840-Vf_c15

#1,2,3,4,6,7,8-HpCDD (c16)
tef_c16 =0.01
qc_c16 = 0.14 
qf_c16 = 0.06
yy_c16 = 0.051
k_c16 = 0.007
Fabs_c16 = 0.885
ey_c16 = e*yy_c16
Vf_c16 = 257.6
Vc_c16 = 1840-Vf_c16

#1,2,3,4,6,7,8,9-OCDD (c17)
tef_c17 =0.0003
qc_c17 = 0.14 
qf_c17 = 0.06
yy_c17 = 0.051
k_c17 = 0.007
Fabs_c17 = 0.885
ey_c17 = e*yy_c17
Vf_c17 = 257.6
Vc_c17 = 1840-Vf_c17

#3,4,4',5-TCB (PCB 81) (c18)
tef_c18 =0.0003
qc_c18 = 0.14 
qf_c18 = 0.06
yy_c18 = 0.051
k_c18 = 0.007
Fabs_c18 = 0.885
ey_c18 = e*yy_c18
Vf_c18 = 257.6
Vc_c18 = 1840-Vf_c18

#3,3',4,4'-TCB (PCB 77) (c19)
tef_c19 =0.0001
qc_c19 = 0.14 
qf_c19 = 0.06
yy_c19 = 0.051
k_c19 = 0.007
Fabs_c19 = 0.885
ey_c19 = e*yy_c19
Vf_c19 = 257.6
Vc_c19 = 1840-Vf_c19

#3,3',4,4',5-PeCB (PCB 126) (c20)
tef_20 =0.1
qc_c20 = 0.14 
qf_c20 = 0.06
yy_c20 = 0.051
k_c20 = 0.007
Fabs_c20 = 0.885
ey_c20 = e*yy_c20
Vf_c20 = 257.6
Vc_c20 = 1840-Vf_c20

#3,3',4,4',5,5'-HxCB (PCB 169) (c21)
tef_c21 =0.03
qc_c21 = 0.14 
qf_c21 = 0.06
yy_c21 = 0.051
k_c21 = 0.007
Fabs_c21 = 0.885
ey_c21 = e*yy_c21
Vf_c21 = 257.6
Vc_c21 = 1840-Vf_c21

#2',3,4,4',5-PeCB (PCB 123) (c22)
tef_c22 =0.00003
qc_c22 = 0.14 
qf_c22 = 0.06
yy_c22 = 0.051
k_c22 = 0.007
Fabs_c22 = 0.885
ey_c22 = e*yy_c22
Vf_c22 = 257.6
Vc_c22 = 1840-Vf_c22

#2,3',4,4',5-PeCB (PCB 118)(c23)
tef_23 =0.00003
qc_c23 = 0.14 
qf_c23 = 0.06
yy_c23 = 0.051
k_c23 = 0.007
Fabs_c23 = 0.885
ey_c23 = e*yy_c23
Vf_c23 = 257.6
Vc_c23 = 1840-Vf_c23

#2,3,4,4',5-PeCB (PCB 114)(c24)
tef_c24 =0.00003
qc_c24 = 0.14 
qf_c24 = 0.06
yy_c24 = 0.051
k_c24 = 0.007
Fabs_c24 = 0.885
ey_c24 = e*yy_c24
Vf_c24 = 257.6
Vc_c24 = 1840-Vf_c24

#2,3,3',4,4'-PeCB (PCB 105)(c25)
tef_d25 =0.00003
qc_c25 = 0.14 
qf_c25 = 0.06
yy_c25 = 0.051
k_c25 = 0.007
Fabs_c25 = 0.885
ey_c25 = e*yy_c25
Vf_c25 = 257.6
Vc_c25 = 1840-Vf_c25

#2,3',4,4',5,5'-HxCB (PCB 167)(c26)
tef_c26 =0.00003
qc_c26 = 0.14 
qf_c26 = 0.06
yy_c26 = 0.051
k_c26 = 0.007
Fabs_c26 = 0.885
ey_c26 = e*yy_c26
Vf_c26 = 257.6
Vc_c26 = 1840-Vf_c26

#2,3,3',4,4',5-HxCB (PCB 156)(c27)
tef_c27 =0.00003
qc_c27 = 0.14 
qf_c27 = 0.06
yy_c27 = 0.051
k_c27 = 0.007
Fabs_c27 = 0.885
ey_c27 = e*yy_c27
Vf_c27 = 257.6
Vc_c27 = 1840-Vf_c27

#2,3,3',4,4',5'-HxCB (PCB 157)(c28)
tef_c28 =0.00003
qc_c28 = 0.14 
qf_c28 = 0.06
yy_c28 = 0.051
k_c28 = 0.007
Fabs_c28 = 0.885
ey_c28 = e*yy_c28
Vf_c28 = 257.6
Vc_c28 = 1840-Vf_c28

#2,3,3',4,4',5,5'-HpCB (PCB 189)(c29)
tef_c29 =0.00003
qc_c29 = 0.14 
qf_c29 = 0.06
yy_c29 = 0.051
k_c29 = 0.007
Fabs_c29 = 0.885
ey_c29 = e*yy_c29
Vf_c29 = 257.6
Vc_c29 = 1840-Vf_c29



def main(feed_intake,exposure_time,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15):
    contamination_level = (c1*tef_c1)+(c2*tef_c2)+(c3*tef_c3)+(c4*tef_c4)+(c5*tef_c5)+c6*tef_c6+c7*tef_c7+c8*tef_c8+c9*tef_c9+c10*tef_c10+c11*tef_c11+c12*tef_c12+(c13*tef_c13)+c14*tef_c14+c15*tef_c15
    
    def GivenDose(t):
        if t <= exposure_time:
                GivenDose = contamination_level*feed_intake*1000
        else:
                GivenDose = 0
        return GivenDose
        
    def GivenDose_c1(t):
        if t <= exposure_time:
                GivenDose_c1 = c1*tef_c1*feed_intake*1000
        else:
                GivenDose_c1 = 0
        return  GivenDose_c1
    
    def GivenDose_c2(t):
        if t <= exposure_time:
                GivenDose_c2 = c2*tef_c2*feed_intake*1000
        else:
                GivenDose_c2 = 0
        return  GivenDose_c2
        
    def GivenDose_c3(t):
        if t <= exposure_time:
                GivenDose_c3 = c3*tef_c3*feed_intake*1000
        else:
                GivenDose_c3 = 0
        return  GivenDose_c3
        
    def GivenDose_c4(t):
        if t <= exposure_time:
                GivenDose_c4 = c4*tef_c4*feed_intake*1000
        else:
                GivenDose_c4 = 0
        return  GivenDose_c4
    
    def GivenDose_c5(t):
        if t <= exposure_time:
                GivenDose_c5 = c5*tef_c5*feed_intake*1000
        else:
                GivenDose_c5 = 0
        return  GivenDose_c5
    
    def GivenDose_c6(t):
        if t <= exposure_time:
                GivenDose_c6 = c6*tef_c6*feed_intake*1000
        else:
                GivenDose_c6 = 0
        return  GivenDose_c6
    
    def GivenDose_c7(t):
        if t <= exposure_time:
                GivenDose_c7 = c7*tef_c7*feed_intake*1000
        else:
                GivenDose_c7 = 0
        return  GivenDose_c7
        
    def GivenDose_c8(t):
        if t <= exposure_time:
                GivenDose_c8 = c8*tef_c8*feed_intake*1000
        else:
                GivenDose_c8 = 0
        return  GivenDose_c8
  
    def GivenDose_c9(t):
        if t <= exposure_time:
                GivenDose_c9 = c9*tef_c9*feed_intake*1000
        else:
                GivenDose_c9 = 0
        return  GivenDose_c9
   
    def GivenDose_c10(t):
        if t <= exposure_time:
                GivenDose_c10 = c10*tef_c10*feed_intake*1000
        else:
                GivenDose_c10 = 0
        return  GivenDose_c10
        
    def GivenDose_c11(t):
        if t <= exposure_time:
                GivenDose_c11 = c11*tef_c11*feed_intake*1000
        else:
                GivenDose_c11 = 0
        return  GivenDose_c11
    
    def GivenDose_c12(t):
        if t <= exposure_time:
                GivenDose_c12 = c12*tef_c12*feed_intake*1000
        else:
                GivenDose_c12 = 0
        return  GivenDose_c12
        
    def GivenDose_c13(t):
        if t <= exposure_time:
                GivenDose_c13 = c13*tef_c13*feed_intake*1000
        else:
                GivenDose_c13 = 0
        return  GivenDose_c13
        
    def GivenDose_c14(t):
        if t <= exposure_time:
                GivenDose_c14 = c14*tef_c14*feed_intake*1000
        else:
                GivenDose_c14 = 0
        return  GivenDose_c14
    
    def GivenDose_c15(t):
        if t <= exposure_time:
                GivenDose_c15 = c15*tef_c15*feed_intake*1000
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
        
        dAcdt2 = Fabs_c2*GivenDose_c2(t)-(qc_c2 + k_c2 + ey_c2)*y[6]+ qf_c2*y[7]
        dAfdt2 = qc_c2*y[6]-qf_c2*y[7] 
        dAeggdt2 = yy_c2*y[6]-y[8]

        dAcdt3 = Fabs_c3*GivenDose_c3(t)-(qc_c3 + k_c3 + ey_c3)*y[9]+ qf_c3*y[10]
        dAfdt3 = qc_c3*y[9]-qf_c3*y[10] 
        dAeggdt3 = yy_c3*y[9]-y[11]

        dAcdt4 = Fabs_c4*GivenDose_c4(t)-(qc_c4 + k_c4 + ey_c4)*y[12]+ qf_c4*y[13]
        dAfdt4 = qc_c4*y[12]-qf_c4*y[13] 
        dAeggdt4 = yy_c4*y[12]-y[14]

        dAcdt5 = Fabs_c5*GivenDose_c5(t)-(qc_c5 + k_c5 + ey_c5)*y[15]+ qf_c5*y[16]
        dAfdt5 = qc_c5*y[15]-qf_c5*y[16] 
        dAeggdt5 = yy_c5*y[15]-y[17]

        dAcdt6 = Fabs_c6*GivenDose_c6(t)-(qc_c6 + k_c6 + ey_c6)*y[18]+ qf_c6*y[19]
        dAfdt6 = qc_c6*y[18]-qf_c6*y[19] 
        dAeggdt6 = yy_c6*y[18]-y[20]

        dAcdt7 = Fabs_c7*GivenDose_c7(t)-(qc_c7 + k_c7 + ey_c7)*y[21]+ qf_c7*y[22]
        dAfdt7 = qc_c7*y[21]-qf_c7*y[22] 
        dAeggdt7 = yy_c7*y[21]-y[23]

        dAcdt8 = Fabs_c8*GivenDose_c8(t)-(qc_c8 + k_c8 + ey_c8)*y[24]+ qf_c8*y[25]
        dAfdt8 = qc_c8*y[24]-qf_c8*y[25] 
        dAeggdt8 = yy_c8*y[24]-y[26]

        dAcdt9 = Fabs_c9*GivenDose_c9(t)-(qc_c9 + k_c9 + ey_c9)*y[27]+ qf_c9*y[28]
        dAfdt9 = qc_c9*y[27]-qf_c9*y[28] 
        dAeggdt9 = yy_c9*y[27]-y[29]

        dAcdt10 = Fabs_c10*GivenDose_c10(t)-(qc_c10 + k_c10 + ey_c10)*y[30]+ qf_c10*y[31]
        dAfdt10 = qc_c10*y[30]-qf_c10*y[31] 
        dAeggdt10 = yy_c10*y[30]-y[32]

        dAcdt11 = Fabs_c11*GivenDose_c11(t)-(qc_c11 + k_c11 + ey_c11)*y[33]+ qf_c11*y[34]
        dAfdt11 = qc_c11*y[33]-qf_c11*y[34] 
        dAeggdt11 = yy_c11*y[33]-y[35]

        dAcdt12 = Fabs_c12*GivenDose_c12(t)-(qc_c12 + k_c12 + ey_c12)*y[36]+ qf_c12*y[37]
        dAfdt12 = qc_c12*y[36]-qf_c12*y[37] 
        dAeggdt12 = yy_c12*y[36]-y[38]

        dAcdt13 = Fabs_c13*GivenDose_c13(t)-(qc_c13 + k_c13 + ey_c13)*y[39]+ qf_c13*y[40]
        dAfdt13 = qc_c13*y[39]-qf_c13*y[40] 
        dAeggdt13 = yy_c13*y[39]-y[41]

        dAcdt14 = Fabs_c14*GivenDose_c14(t)-(qc_c14 + k_c14 + ey_c14)*y[42]+ qf_c14*y[43]
        dAfdt14 = qc_c14*y[42]-qf_c14*y[43] 
        dAeggdt14 = yy_c14*y[42]-y[44]

        dAcdt15 = Fabs_c15*GivenDose_c15(t)-(qc_c15 + k_c15 + ey_c15)*y[45]+ qf_c15*y[46]
        dAfdt15 = qc_c15*y[45]-qf_c15*y[46] 
        dAeggdt15 = yy_c15*y[45]-y[47]
        
        
        return [dAcdt,dAfdt,dAeggdt,
                dAcdt1,dAfdt1,dAeggdt1,
                dAcdt2,dAfdt2,dAeggdt2,
                dAcdt3,dAfdt3,dAeggdt3,
                dAcdt4,dAfdt4,dAeggdt4,
                dAcdt5,dAfdt5,dAeggdt5,
                dAcdt6,dAfdt6,dAeggdt6,
                dAcdt7,dAfdt7,dAeggdt7,
                dAcdt8,dAfdt8,dAeggdt8,
                dAcdt9,dAfdt9,dAeggdt9,
                dAcdt10,dAfdt10,dAeggdt10,
                dAcdt11,dAfdt11,dAeggdt11,
                dAcdt12,dAfdt12,dAeggdt12,
                dAcdt13,dAfdt13,dAeggdt13,
                dAcdt14,dAfdt14,dAeggdt14,
                dAcdt15,dAfdt15,dAeggdt15
                ]
        

    timeGrid = np.arange(0,250,0.01)
    delay = np.arange(1,251,0.01)
    GivenDose = (GivenDose,)
    yinit = np.array([0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0,
                      0.0,0.0,0.0])
    (y,d) = odeint (myModel, yinit, timeGrid, GivenDose, full_output=1)
    plt.figure()
    plt.plot(delay, y[:,2]/Vegg) # y[:,0] is the first column of y
    plt.plot(delay, (y[:,5]+y[:,8]+y[:,11]+y[:,14]+y[:,17]+y[:,20]+y[:,23]+y[:,26]+y[:,29]+y[:,32]+y[:,35]+y[:,38]+y[:,41]+y[:,44]+y[:,47])/Vegg)
    plt.xlim(0, 250)
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
