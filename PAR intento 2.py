#!/usr/bin/env python
# coding: utf-8

# In[17]:


from numpy import * # de que se trata el * ????????????????????
from matplotlib.pyplot import * # --> do graphic whit plot()


import sys #--> view directory
import numpy as np #--> import data with open()
import pandas as pd
import matplotlib.pyplot as plt

import re
from natsort import natsorted,ns
from os import listdir #--> view directory

import scipy.signal
from scipy.interpolate import interp1d
import scipy.optimize as opt
import scipy.misc
from scipy import ndimage


# In[28]:


#Lectura de datos 
CurrentDirectory = get_ipython().run_line_magic('pwd', '')
homepath= CurrentDirectory + "\\DatosPAR\\"
fnames=listdir(homepath)
tdata=array([loadtxt(open(homepath+q).readlines()[2:-1], unpack=1,skiprows=0) for q in fnames])


# In[32]:


################################
################################
# First we set the graphs

# Figure control
figure(figsize=(25,25))

# subplot(row, column, position)
ax=plt.subplot(4,1,1)  # 'ax' is in the first position/column
ax1=plt.subplot(4,1,2) # 'ax1' is in the second position 
ax2=plt.subplot(4,1,3) # 'ax2' is in the third position
ax3=plt.subplot(4,1,4) # 'ax2' is in the third position

# Title and subtitles
plt.suptitle('Espectro solar')
ax.set_title('Archivo1')
ax1.set_title('Archivo2')
ax2.set_title('Archivo3')
ax3.set_title('Archivo4')

# Labels
Xlabel,XaxisU='$\lambda$',' (nm)'
Ylabel,YaxisU='Irradiancia',' ($W/m^2$)'

# xaxis label
ax.set_xlabel(Xlabel+XaxisU)
ax1.set_xlabel(Xlabel+XaxisU)
ax2.set_xlabel(Xlabel+XaxisU)
ax3.set_xlabel(Xlabel+XaxisU)

# yaxis label
ax.set_ylabel((Ylabel + YaxisU))
ax1.set_ylabel((Ylabel + YaxisU))
ax2.set_ylabel((Ylabel + YaxisU))
ax3.set_ylabel(Ylabel + YaxisU)
# plot 
ax.plot(tdata[0,0,:],tdata[0,1,:])
ax1.plot(tdata[1,0,:],tdata[1,1,:])
ax2.plot(tdata[2,0,:],tdata[2,1,:])
ax3.plot(tdata[3,0,:],tdata[3,1,:])


# In[ ]:




