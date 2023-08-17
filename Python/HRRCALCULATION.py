import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np 
import array as arr 
time_list =[0,5,10,15,20,25,30,35,40,45,50,55,60,65]
mlr_list=np.array([0.0044526,0.0084680,0.0097431,0.0098441,0.0103118,0.0076974,0.0081407,0.0088042,0.0095169,0.0081499,0.0075168,0.0094037,0.0078165,0.0061315])

huc = 48073 # Effective heat of combustion huc = 44590 KJ / kg
hrr_list = abs(mlr_list*huc) # calculate HRR from mass loss
hrr_list = np.concatenate(([0], hrr_list))
print(hrr_list)
print(f"&SURF ID = 'BURNER', HRRPUA = {max(hrr_list):.2f}, RAMP_Q = 'fireramp', COLOR = 'RASPBERRY' /")
for time, hrr in zip(time_list, hrr_list):
    print(f"&RAMP ID='fireramp', T={time}, F={hrr/max(hrr_list):.2f} /")