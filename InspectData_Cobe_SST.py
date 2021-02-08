import netCDF4 as nc
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

#get data set...print metadata
myCobeData = 'sst.mon.mean.nc'
dsCobe = nc.Dataset(myCobeData)
print(dsCobe)
for var in dsCobe.variables.values():
     print(var)

#sst is (time, lat, lon)
print(dsCobe['sst'].shape)  #sst is 1560, 180, 360... 130 years... 12 months... 1560 data points...
#colormap options -- https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

#min is -5 and max is 40 within the full dataset
myColor = 'gist_ncar'
myMin = -5
myMax = 40


#jan80 - 1080.... dec89 - 1200
eightiesSST = dsCobe['sst'][1080:1200]
#print(eightiesSST.shape)
eightiesAVG = np.mean(eightiesSST, axis=0)
#print(eightiesAVG.shape)
plt.imshow(eightiesAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('cobeSST_eighties.png')

#jan00 - 1320.... dec09 - 1440
thousandsSST = dsCobe['sst'][1320:1440]
#print(thousandsSST.shape)
thousandsAVG = np.mean(thousandsSST, axis=0)
#print(thousandsAVG.shape)
plt.imshow(thousandsAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('cobeSST_thousands.png')

#jan80 - 1080.... dec09 - 1440
allSST = dsCobe['sst'][1080:1440]
#print(allSST.shape)
allAVG = np.mean(allSST, axis=0)
#print(allAVG.shape)
plt.imshow(allAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('cobeSST_all.png')

diffMin = -2
diffMax = 2
diffAVG = thousandsAVG-eightiesAVG
plt.imshow(diffAVG, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('cobeSST_thousands_less_eighties.png')

#dec80 - 1092.... Feb81 - 1095
eighties_Wint_SST = dsCobe['sst'][1092:1095]
eighties_Wint_SST_avg = np.mean(eighties_Wint_SST, axis=0)
#jun80 - 1086.... aug00 - 1089
eighties_Summer_SST = dsCobe['sst'][1086:1089]
eighties_Summer_SST_avg = np.mean(eighties_Summer_SST, axis=0)
#dec00 - 1331.... Feb01 - 1334
thousands_Wint_SST = dsCobe['sst'][1331:1334]
thousands_Wint_SST_avg = np.mean(thousands_Wint_SST, axis=0)
#jun00 - 1326.... aug00 - 1329
thousands_Summer_SST = dsCobe['sst'][1326:1329]
thousands_Summer_SST_avg = np.mean(thousands_Summer_SST, axis=0)

wint_diff_SST = thousands_Wint_SST_avg - eighties_Wint_SST_avg
plt.imshow(wint_diff_SST, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('cobeSST_wint_diff_thousands_less_eighties.png')


summ_diff_SST = thousands_Summer_SST_avg - eighties_Summer_SST_avg
plt.imshow(summ_diff_SST, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('cobeSST_summ_diff_thousands_less_eighties.png')



