
##======================================================##
##                                                      ##
##   Numpy - Datos C                                    ##
##                                                      ##
##   Autor: George Ababei                               ##
##   Universidad: Universitat de les Illes Balears      ##
##                                                      ##
##======================================================##

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

#Recogemos el nombre y número de columnas
datos_str = np.loadtxt("data/datos_C.csv", delimiter=",", dtype=str)
nom_col=datos_str[0]
numero_col=nom_col.size

formats=[]

#Buscamos el tipo de datos de cada columna
for i in range(numero_col):	
	try:
		columna = np.loadtxt("data/datos_C.csv", delimiter=",", dtype=None, encoding=None, skiprows=1, usecols=i)
		formats.append(columna.dtype.str)
	except:
		formats.append("U64")


#Cargamos los datos
data = np.genfromtxt("data/datos_C.csv", delimiter=",", 
	dtype={'names': nom_col,'formats': formats},
	 skip_header=1, filling_values='0')



print(" "*3)
print("---- 1. COFOG de Rumania entre los años 2012 y 2020----")
print(" "*3)

RO = np.where(data["geo"]=="RO")

# plot
x = data[RO]["TIME_PERIOD"].astype(int)
y = data[RO]["OBS_VALUE"]

plt.bar(x, y, width=0.7, edgecolor="black", linewidth=0.5)
plt.xticks(rotation=70)
plt.xlabel("Año")
plt.ylabel("Gasto")
plt.title("COFOG de Rumania")

plt.show()


print(" "*3)
print("---- Media de gasto europeo entre los años 2012 y 2020 ----")
print(" "*3)

valores=[]

for i in range(2012, 2021):
	a = np.where(data["TIME_PERIOD"]==i)
	valores.append(round(np.mean(data[a]["OBS_VALUE"]), 2))

anyos = data[RO]["TIME_PERIOD"].astype(int)

# plot
x = anyos
y = valores

plt.bar(x, y, width=0.7, edgecolor="black", linewidth=0.5)
plt.xticks(rotation=70)
plt.xlabel("Año")
plt.ylabel("Gasto")
plt.title("COFOG europeo entre 2012 y 2020")

plt.show()


print(" "*3)
print("---- ¿Qué país gastó más durante el año 2019?----")
print(" "*3)

anyo = np.where(data["TIME_PERIOD"]==2019)
mayor_gasto = max(data[anyo]["OBS_VALUE"])

valor = np.where(data["OBS_VALUE"]==mayor_gasto)
pais_mayor_gasto=data[np.intersect1d(anyo, valor)]["geo"]

print("El/Los pais/es con el mayor gasto durante el año 2019 fue:",pais_mayor_gasto)

print(" "*3)
print("---- Serie ordenada del gasto de los paises en el año 2015 ----")
print(" "*3)

paises = np.unique(data["geo"])
anyo = np.where(data["TIME_PERIOD"]==2015)
gasto = data[anyo]["OBS_VALUE"]
gasto_2015 = list(zip(gasto,paises))
gasto_2015.sort()
y, x = zip(*gasto_2015)


# plot
plt.bar(x, y, width=0.7, edgecolor="black", linewidth=0.5)
plt.xticks(rotation=70)
plt.xlabel("Pais")
plt.ylabel("Gasto")
plt.title("Serie ordenada del gasto de los paises en el año 2015")

plt.show()