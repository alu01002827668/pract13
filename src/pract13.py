#!/src/bin/python
#!ecoding: UTF-8

import matplotlib.pylab as pl
import modulo
import time

nro_test=100
intervalos=[10, 50, 100, 150, 500, 550, 1000]
umbral=[1e-3, 1e-4, 1e-5, 1e-6, 1e-7]

p=[]
for n in intervalos:                           
  ci=time.clock()                                 
  e=modulo.error(n, nro_test, 1e-7)                                        
  cf=time.clock()                                       
  tp=cf-ci
  p=p+[tp]                                                
  
pl.figure(figsize=(10,10),dpi=80)


pl.plot(intervalos,p, 'r')
pl.subplot(2,1,1)
pl.xticks([10, 50, 100, 150, 500, 550, 1000])

pl.title('Tiempo respecto a los intervalos')
pl.xlabel('Intervalos')
pl.ylabel('Tiempo')
pl.legend(['10'])
pl.xlim(-10,1100)
pl.ylim(-0.001,0.15)



b=[]
for n in intervalos:
  porcentaje=[]
  for a in umbral:
    e = modulo.error(n,100,umbral)
    porcentaje=porcentaje + [e]
  b= b + [p]


pl.plot(umbral,color='black',label=10)
pl.plot(umbral,color='red', label=50)
pl.plot(umbral,color='blue', label=100)
pl.plot(umbral,color='yellow',label = 150)
pl.plot(umbral, color='
pl.title('Grafica')
pl.xlabel('Umbral')
pl.ylabel('Tiempos')
pl.legend(

pl.show()   
    
    
