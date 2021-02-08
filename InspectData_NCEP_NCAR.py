import netCDF4 as nc
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

#get data set...print metadata
myNCEPData = 'air.sig995.mon.mean.nc'
dsNCEP = nc.Dataset(myNCEPData)
print(dsNCEP)
for var in dsNCEP.variables.values():
     print(var)

#airtemp is (time, lat, lon)
print(dsNCEP['air'].shape)  #airtemp is 877, 73, 144... 73 + 1/12 years... 12 months... 877 data points...

#actual min is approx -75 and actual max is approx 45 within the full dataset
myColor = 'gist_ncar'
myMin = -75
myMax = 45

#jan80 - 384.... dec89 - 504
eightiesAIR = dsNCEP['air'][384:396]
eightiesAVG = np.mean(eightiesAIR, axis=0)
#print(eightiesAVG.shape)
plt.imshow(eightiesAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('NCEP_air_eighties.png')

#jan00 - 624.... dec09 - 744
thousandsAIR = dsNCEP['air'][624:744]
thousandsAVG = np.mean(thousandsAIR, axis=0)
#print(thousandsAVG.shape)
plt.imshow(thousandsAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('NCEP_air_thousands.png')

#jan80 - 384.... dec09 - 744
allAIR = dsNCEP['air'][384:744]
allAVG = np.mean(allAIR, axis=0)
#print(allAVG.shape)
plt.imshow(allAVG, cmap=myColor, vmin=myMin, vmax=myMax)
#plt.show()
plt.savefig('NCEP_air_all.png')

diffMin = -5
diffMax = 5
diffAVG = thousandsAVG-eightiesAVG
plt.imshow(diffAVG, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('NCEP_air_thousands_less_eighties.png')

#dec80 - 396.... Feb81 - 399
eighties_Wint_AIR = dsNCEP['air'][396:399]
eighties_Wint_AIR_avg = np.mean(eighties_Wint_AIR, axis=0)
#jun80 - 390.... aug00 - 393
eighties_Summer_AIR = dsNCEP['air'][390:393]
eighties_Summer_AIR_avg = np.mean(eighties_Summer_AIR, axis=0)
#dec00 - 636.... Feb01 - 639
thousands_Wint_AIR = dsNCEP['air'][636:639]
thousands_Wint_AIR_avg = np.mean(thousands_Wint_AIR, axis=0)
#jun00 - 630.... aug00 - 633
thousands_Summer_AIR = dsNCEP['air'][630:633]
thousands_Summer_AIR_avg = np.mean(thousands_Summer_AIR, axis=0)

wint_diff_AIR = thousands_Wint_AIR_avg - eighties_Wint_AIR_avg
plt.imshow(wint_diff_AIR, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('NCEP_air_wint_diff_thousands_less_eighties.png')


summ_diff_AIR = thousands_Summer_AIR_avg - eighties_Summer_AIR_avg
plt.imshow(summ_diff_AIR, cmap=myColor, vmin=diffMin, vmax=diffMax)
#plt.show()
plt.savefig('NCEP_air_summ_diff_thousands_less_eighties.png')