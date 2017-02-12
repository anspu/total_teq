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
qc_c1 = 0.31
qf_c1 = 0.205
yy_c1 = 0.0345
k_c1 = 0.006
Fabs_c1 = 0.85
ey_c1 = e*yy_c1
Vf_c1 = 240
Vc_c1 = 1840-Vf_c1

#1,2,3,7,8-PeCDF (c2)
tef_c2 = 0.03
qc_c2 = 0.19
qf_c2 = 0.073
yy_c2 = 0.0665
k_c2 = 0.0115
Fabs_c2 = 0.885
ey_c2 = e*yy_c2
Vf_c2 = 255
Vc_c2 = 1840-Vf_c2

#1,2,3,7,8-PeCDF (c3)
tef_c3 = 0.3
qc_c3 = 0.1 
qf_c3 = 0.057
yy_c3 = 0.047
k_c3 = 0.008
Fabs_c3 = 0.885
ey_c3 = e*yy_c3
Vf_c3 = 230
Vc_c3 = 1840-Vf_c3

#1,2,3,4,7,8-HxCDF (c4)
tef_c4 = 0.1
qc_c4 = 0.08
qf_c4 = 0.029
yy_c4 = 0.088
k_c4 = 0.0215
Fabs_c4 = 0.8
ey_c4 = e*yy_c4
Vf_c4 = 245
Vc_c4 = 1840-Vf_c4

#1,2,3,6,7,8-HxCDF (c5)
tef_c5 = 0.1
qc_c5 = 0.08 
qf_c5 = 0.031
yy_c5 = 0.0845
k_c5 = 0.0245
Fabs_c5 = 0.775
ey_c5 = e*yy_c5
Vf_c5 = 250
Vc_c5 = 1840-Vf_c5

#2,3,4,6,7,8-HxCDF (c6)
tef_c6 =0.1
qc_c6 = 0.1 
qf_c6 = 0.034
yy_c6 = 0.095
k_c6 = 0.036
Fabs_c6 = 0.725
ey_c6 = e*yy_c6
Vf_c6 = 325
Vc_c6 = 1840-Vf_c6

#1,2,3,7,8,9-HxCDF  (c7)
tef_c7 = 0.1
qc_c7 = 0.1 
qf_c7 = 0.04
yy_c7 = 0.0795
k_c7 = 0.024
Fabs_c7 = 0.77
ey_c7 = e*yy_c7
Vf_c7 = 255
Vc_c7 = 1840-Vf_c7

#1,2,3,4,6,7,8-HpCDF (c8)
tef_c8  =0.01
qc_c8 = 0.06 
qf_c8 = 0.034
yy_c8 = 0.1075
k_c8 = 0.0745
Fabs_c8 = 0.59
ey_c8 = e*yy_c8
Vf_c8 = 460
Vc_c8 = 1840-Vf_c8

#1,2,3,4,7,8,9-HpCDF (c9)
tef_c9 =0.01
qc_c9 = 0.04 
qf_c9 = 0.018
yy_c9 = 0.1035
k_c9 = 0.063
Fabs_c9 = 0.62
ey_c9 = e*yy_c9
Vf_c9 = 380
Vc_c9 = 1840-Vf_c9

#1,2,3,4,6,7,8,9-OCDF (c10)
tef_c10 =0.0003
qc_c10 = 0.14 
qf_c10 = 0.06
yy_c10 = 0.0505
k_c10 = 0.0065
Fabs_c10 = 0.885
ey_c10 = e*yy_c10
Vf_c10 = 257.6
Vc_c10 = 1840-Vf_c10

#2,3,7,8-TCDD (c11)
tef_c11 =1
qc_c11 = 0.35 
qf_c11 = 0.23
yy_c11 = 0.0375
k_c11 = 0.0045
Fabs_c11 = 0.89
ey_c11 = e*yy_c11
Vf_c11 = 240
Vc_c11 = 1840-Vf_c11

#1,2,3,7,8-PeCDD(c12)
tef_c12 =1 
qc_c12 = 0.14 
qf_c12 = 0.07
yy_c12 = 0.048
k_c12 = 0.007
Fabs_c12 = 0.875
ey_c12 = e*yy_c12
Vf_c12 = 260
Vc_c12 = 1840-Vf_c12

#1,2,3,4,7,8-HxCDD (c13)
tef_c13 =0.1
qc_c13 = 0.09 
qf_c13 = 0.03
yy_c13 = 0.0815
k_c13 = 0.0195
Fabs_c13 = 0.805
ey_c13 = e*yy_c13
Vf_c13 = 250
Vc_c13 = 1840-Vf_c13

#1,2,3,6,7,8-HxCDD (c14)
tef_c14 = 0.1
qc_c14 = 0.09 
qf_c14 = 0.036
yy_c14 = 0.084
k_c14 = 0.0215
Fabs_c14 = 0.795
ey_c14 = e*yy_c14
Vf_c14 = 220
Vc_c14 = 1840-Vf_c14

#1,2,3,7,8,9-HxCDD (c15)
tef_c15 =0.1
qc_c15 = 0.07   
qf_c15 = 0.032
yy_c15 = 0.084
k_c15 = 0.034
Fabs_c15 = 0.71
ey_c15 = e*yy_c15
Vf_c15 = 255
Vc_c15 = 1840-Vf_c15

#1,2,3,4,6,7,8-HpCDD (c16)
tef_c16 =0.01
qc_c16 = 0.14 
qf_c16 = 0.06
yy_c16 = 0.0505
k_c16 = 0.0065
Fabs_c16 = 0.885
ey_c16 = e*yy_c16
Vf_c16 = 257.6
Vc_c16 = 1840-Vf_c16

#1,2,3,4,6,7,8,9-OCDD (c17)
tef_c17 =0.0003
qc_c17 = 0.14 
qf_c17 = 0.06
yy_c17 = 0.0505
k_c17 = 0.0065
Fabs_c17 = 0.885
ey_c17 = e*yy_c17
Vf_c17 = 257.6
Vc_c17 = 1840-Vf_c17

#3,4,4',5-TCB (PCB 81) (c18)
tef_c18 =0.0003
qc_c18 = 0.11 
qf_c18 = 0.121
yy_c18 = 0.023
k_c18 = 0.001
Fabs_c18 = 0.96
ey_c18 = e*yy_c18
Vf_c18 = 195
Vc_c18 = 1840-Vf_c18

#3,3',4,4'-TCB (PCB 77) (c19)
tef_c19 =0.0001
qc_c19 = 0.25 
qf_c19 = 0.136
yy_c19 = 0.0415
k_c19 = 0.0025
Fabs_c19 = 0.945
ey_c19 = e*yy_c19
Vf_c19 = 255
Vc_c19 = 1840-Vf_c19

#3,3',4,4',5-PeCB (PCB 126) (c20)
tef_c20 =0.1
qc_c20 = 0.13 
qf_c20 = 0.067
yy_c20 = 0.038
k_c20 = 0
Fabs_c20 = 1
ey_c20 = e*yy_c20
Vf_c20 = 270
Vc_c20 = 1840-Vf_c20

#3,3',4,4',5,5'-HxCB (PCB 169) (c21)
tef_c21 =0.03
qc_c21 = 0.11 
qf_c21 = 0.029
yy_c21 = 0.0745
k_c21 = 0.006
Fabs_c21 = 0.925
ey_c21 = e*yy_c21
Vf_c21 = 240
Vc_c21 = 1840-Vf_c21

#2',3,4,4',5-PeCB (PCB 123) (c22)
tef_c22 =0.00003
qc_c22 = 0.14 
qf_c22 = 0.06
yy_c22 = 0.0505
k_c22 = 0.0065
Fabs_c22 = 0.885
ey_c22 = e*yy_c22
Vf_c22 = 257.6
Vc_c22 = 1840-Vf_c22

#2,3',4,4',5-PeCB (PCB 118)(c23)
tef_c23 =0.00003
qc_c23 = 0.12 
qf_c23 = 0.063
yy_c23 = 0.0405
k_c23 = 0.0005
Fabs_c23 = 0.99
ey_c23 = e*yy_c23
Vf_c23 = 235
Vc_c23 = 1840-Vf_c23

#2,3,4,4',5-PeCB (PCB 114)(c24)
tef_c24 =0.00003
qc_c24 = 0.2 
qf_c24 = 0.09
yy_c24 = 0.0575
k_c24 = 0.0035
Fabs_c24 = 0.945
ey_c24 = e*yy_c24
Vf_c24 = 290
Vc_c24 = 1840-Vf_c24

#2,3,3',4,4'-PeCB (PCB 105)(c25)
tef_c25 =0.00003
qc_c25 = 0.12 
qf_c25 = 0.084
yy_c25 = 0.0355
k_c25 = 0.0025
Fabs_c25 = 0.96
ey_c25 = e*yy_c25
Vf_c25 = 220
Vc_c25 = 1840-Vf_c25

#2,3',4,4',5,5'-HxCB (PCB 167)(c26)
tef_c26 =0.00003
qc_c26 = 0.1
qf_c26 = 0.095
yy_c26 = 0.062
k_c26 = 0
Fabs_c26 = 1
ey_c26 = e*yy_c26
Vf_c26 = 70
Vc_c26 = 1840-Vf_c26

#2,3,3',4,4',5-HxCB (PCB 156)(c27)
tef_c27 =0.00003
qc_c27 = 0.11 
qf_c27 = 0.039
yy_c27 = 0.0605
k_c27 = 0.0025
Fabs_c27 = 0.96
ey_c27 = e*yy_c27
Vf_c27 = 230
Vc_c27 = 1840-Vf_c27

#2,3,3',4,4',5'-HxCB (PCB 157)(c28)
tef_c28 =0.00003
qc_c28 = 0.16 
qf_c28 = 0.051
yy_c28 = 0.0875
k_c28 = 0.0065
Fabs_c28 = 0.93
ey_c28 = e*yy_c28
Vf_c28 = 205
Vc_c28 = 1840-Vf_c28

#2,3,3',4,4',5,5'-HpCB (PCB 189)(c29)
tef_c29 =0.00003
qc_c29 = 0.06 
qf_c29 = 0.017
yy_c29 = 0.092
k_c29 = 0.01
Fabs_c29 = 0.80
ey_c29 = e*yy_c29
Vf_c29 = 215
Vc_c29 = 1840-Vf_c29



def main(feed_intake,exposure_time,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29):

    contamination_level = (c1*tef_c1+c2*tef_c2+c3*tef_c3+c4*tef_c4+c5*tef_c5
    +c6*tef_c6+c7*tef_c7+c8*tef_c8+c9*tef_c9+c10*tef_c10+c11*tef_c11+c12*tef_c12
    +c13*tef_c13+c14*tef_c14+c15*tef_c15+c16*tef_c16+c17*tef_c17+c18*tef_c18
    +c19*tef_c19+c20*tef_c20+c21*tef_c21+c22*tef_c22+c23*tef_c23+c24*tef_c24
    +c25*tef_c25+c26*tef_c26+c27*tef_c27+c28*tef_c28+c29*tef_c29)
    
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
    
    def GivenDose_c16(t):
        if t <= exposure_time:
                GivenDose_c16 = c16*tef_c16*feed_intake*1000
        else:
                GivenDose_c16 = 0
        return  GivenDose_c16
        
    def GivenDose_c17(t):
        if t <= exposure_time:
                GivenDose_c17 = c17*tef_c17*feed_intake*1000
        else:
                GivenDose_c17 = 0
        return  GivenDose_c17
    
    def GivenDose_c18(t):
        if t <= exposure_time:
                GivenDose_c18 = c18*tef_c18*feed_intake*1000
        else:
                GivenDose_c18 = 0
        return  GivenDose_c18
        
    def GivenDose_c19(t):
        if t <= exposure_time:
                GivenDose_c19 = c19*tef_c19*feed_intake*1000
        else:
                GivenDose_c19 = 0
        return  GivenDose_c19
        
    def GivenDose_c20(t):
        if t <= exposure_time:
                GivenDose_c20 = c20*tef_c20*feed_intake*1000
        else:
                GivenDose_c20 = 0
        return  GivenDose_c20
    
    def GivenDose_c21(t):
        if t <= exposure_time:
                GivenDose_c21 = c21*tef_c21*feed_intake*1000
        else:
                GivenDose_c21 = 0
        return  GivenDose_c21
    
    def GivenDose_c22(t):
        if t <= exposure_time:
                GivenDose_c22 = c22*tef_c22*feed_intake*1000
        else:
                GivenDose_c22 = 0
        return  GivenDose_c22
    
    def GivenDose_c23(t):
        if t <= exposure_time:
                GivenDose_c23 = c23*tef_c23*feed_intake*1000
        else:
                GivenDose_c23 = 0
        return  GivenDose_c23
        
    def GivenDose_c24(t):
        if t <= exposure_time:
                GivenDose_c24 = c24*tef_c24*feed_intake*1000
        else:
                GivenDose_c24 = 0
        return  GivenDose_c24
  
    def GivenDose_c25(t):
        if t <= exposure_time:
                GivenDose_c25 = c25*tef_c25*feed_intake*1000
        else:
                GivenDose_c25 = 0
        return  GivenDose_c25
   
    def GivenDose_c26(t):
        if t <= exposure_time:
                GivenDose_c26 = c26*tef_c26*feed_intake*1000
        else:
                GivenDose_c26 = 0
        return  GivenDose_c26
        
    def GivenDose_c27(t):
        if t <= exposure_time:
                GivenDose_c27 = c27*tef_c27*feed_intake*1000
        else:
                GivenDose_c27 = 0
        return  GivenDose_c27
    
    def GivenDose_c28(t):
        if t <= exposure_time:
                GivenDose_c28 = c28*tef_c28*feed_intake*1000
        else:
                GivenDose_c28 = 0
        return  GivenDose_c28
        
    def GivenDose_c29(t):
        if t <= exposure_time:
                GivenDose_c29 = c29*tef_c29*feed_intake*1000
        else:
                GivenDose_c29 = 0
        return  GivenDose_c29
  

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

        dAcdt16 = Fabs_c16*GivenDose_c16(t)-(qc_c16 + k_c16 + ey_c16)*y[48]+ qf_c16*y[49]
        dAfdt16 = qc_c16*y[48]-qf_c16*y[49] 
        dAeggdt16 = yy_c16*y[48]-y[50]

        dAcdt17 = Fabs_c17*GivenDose_c17(t)-(qc_c17 + k_c17 + ey_c17)*y[51]+ qf_c17*y[52]
        dAfdt17 = qc_c17*y[51]-qf_c17*y[52] 
        dAeggdt17 = yy_c17*y[51]-y[53]

        dAcdt18 = Fabs_c18*GivenDose_c18(t)-(qc_c18 + k_c18 + ey_c18)*y[54]+ qf_c18*y[55]
        dAfdt18 = qc_c18*y[54]-qf_c18*y[55] 
        dAeggdt18 = yy_c18*y[54]-y[56]

        dAcdt19 = Fabs_c19*GivenDose_c19(t)-(qc_c19 + k_c19 + ey_c19)*y[57]+ qf_c19*y[58]
        dAfdt19 = qc_c19*y[57]-qf_c19*y[58] 
        dAeggdt19 = yy_c19*y[57]-y[59]

        dAcdt20 = Fabs_c20*GivenDose_c20(t)-(qc_c20 + k_c20 + ey_c20)*y[60]+ qf_c20*y[61]
        dAfdt20 = qc_c20*y[60]-qf_c20*y[61] 
        dAeggdt20 = yy_c20*y[60]-y[62]

        dAcdt21 = Fabs_c21*GivenDose_c21(t)-(qc_c21 + k_c21 + ey_c21)*y[63]+ qf_c21*y[64]
        dAfdt21 = qc_c21*y[63]-qf_c21*y[64] 
        dAeggdt21 = yy_c21*y[63]-y[65]

        dAcdt22 = Fabs_c22*GivenDose_c22(t)-(qc_c22 + k_c22 + ey_c22)*y[66]+ qf_c22*y[67]
        dAfdt22 = qc_c22*y[66]-qf_c22*y[67] 
        dAeggdt22 = yy_c22*y[66]-y[68]

        dAcdt23 = Fabs_c23*GivenDose_c23(t)-(qc_c23 + k_c23 + ey_c23)*y[69]+ qf_c23*y[70]
        dAfdt23 = qc_c23*y[69]-qf_c23*y[70] 
        dAeggdt23 = yy_c23*y[69]-y[71]

        dAcdt24 = Fabs_c24*GivenDose_c24(t)-(qc_c24 + k_c24 + ey_c24)*y[72]+ qf_c24*y[73]
        dAfdt24 = qc_c24*y[72]-qf_c24*y[73] 
        dAeggdt24 = yy_c24*y[72]-y[74]

        dAcdt25 = Fabs_c25*GivenDose_c25(t)-(qc_c25 + k_c25 + ey_c25)*y[75]+ qf_c25*y[76]
        dAfdt25 = qc_c25*y[75]-qf_c25*y[76] 
        dAeggdt25 = yy_c25*y[75]-y[77]

        dAcdt26 = Fabs_c26*GivenDose_c26(t)-(qc_c26 + k_c26 + ey_c26)*y[78]+ qf_c26*y[79]
        dAfdt26 = qc_c26*y[78]-qf_c26*y[79] 
        dAeggdt26 = yy_c26*y[78]-y[80]

        dAcdt27 = Fabs_c27*GivenDose_c27(t)-(qc_c27 + k_c27 + ey_c27)*y[81]+ qf_c27*y[82]
        dAfdt27 = qc_c27*y[81]-qf_c27*y[82] 
        dAeggdt27 = yy_c27*y[81]-y[83]

        dAcdt28 = Fabs_c28*GivenDose_c28(t)-(qc_c28 + k_c28 + ey_c28)*y[84]+ qf_c28*y[85]
        dAfdt28 = qc_c28*y[84]-qf_c28*y[85] 
        dAeggdt28 = yy_c28*y[84]-y[86]

        dAcdt29 = Fabs_c29*GivenDose_c29(t)-(qc_c29 + k_c29 + ey_c29)*y[87]+ qf_c29*y[88]
        dAfdt29 = qc_c29*y[87]-qf_c29*y[88] 
        dAeggdt29 = yy_c29*y[87]-y[89]
        
        
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
                dAcdt15,dAfdt15,dAeggdt15,
                dAcdt16,dAfdt16,dAeggdt16,
                dAcdt17,dAfdt17,dAeggdt17,
                dAcdt18,dAfdt18,dAeggdt18,
                dAcdt19,dAfdt19,dAeggdt19,
                dAcdt20,dAfdt20,dAeggdt20,
                dAcdt21,dAfdt21,dAeggdt21,
                dAcdt22,dAfdt22,dAeggdt22,
                dAcdt23,dAfdt23,dAeggdt23,
                dAcdt24,dAfdt24,dAeggdt24,
                dAcdt25,dAfdt25,dAeggdt25,
                dAcdt26,dAfdt26,dAeggdt26,
                dAcdt27,dAfdt27,dAeggdt27,
                dAcdt28,dAfdt28,dAeggdt28,
                dAcdt29,dAfdt29,dAeggdt29,
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
                      0.0,0.0,0.0,])
    (y,d) = odeint (myModel, yinit, timeGrid, GivenDose, full_output=1)
    plt.figure()
    plt.plot(delay, y[:,2]/Vegg) # y[:,0] is the first column of y
    plt.plot(delay, (y[:,5]+y[:,8]+y[:,11]+y[:,14]+y[:,17]+y[:,20]+y[:,23]+y[:,26]+y[:,29]+y[:,32]+y[:,35]+y[:,38]+y[:,41]+y[:,44]+y[:,47]+y[:,50]+y[:,53]+y[:,56]+y[:,59]
                     +y[:,62]+y[:,65]+y[:,68]+y[:,71]+y[:,74]+y[:,77]+y[:,80]+y[:,83]+y[:,86]+y[:,89])/Vegg)
    plt.xlim(0, 250)
    blue_patch = mpatches.Patch(color='blue', label='Total TEQ model')
    green_patch = mpatches.Patch(color='green', label='Sum of congener specific models')
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
        sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16], sys.argv[17], sys.argv[18],
        sys.argv[19],sys.argv[20], sys.argv[21],sys.argv[22],
        sys.argv[23], sys.argv[24], sys.argv[25],sys.argv[26],
        sys.argv[27], sys.argv[28], sys.argv[29], sys.argv[30], sys.argv[31])
