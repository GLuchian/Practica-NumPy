
##======================================================##
##                                                      ##
##   Numpy - Datos A                                    ##
##                                                      ##
##   Autor: George Ababei                               ##
##   Universidad: Universitat de les Illes Balears      ##
##                                                      ##
##======================================================##

#Cargamos la libreria numpy con la que vamos a trabajar y matplotlib para las representaciones
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

#Definimos la función para eliminar el problema de números cuyos miles estan separados por punto
# y el programa lo interpreta como decimal (este método SOLO funciona para este dataset)
def punto_travieso(x):
   x=float(x)
   if x.is_integer():
       return(x)
   else:
       return(x*1000)

#Obtenemos el número y nombre de las columnas del dataset
datos_str = np.loadtxt("data/datos_A.csv", delimiter=";", dtype=str)
nom_col=datos_str[0]
numero_col=nom_col.size

formats=[]

#Miramos el tipo de cada columna para luego cargar los datos con dicho tipo
for i in range(numero_col):
	try:
		columna = np.genfromtxt("data/datos_A.csv", delimiter=";", dtype=None, encoding=None,
		 skip_header=1, usecols=i, filling_values='0')
		formats.append(columna.dtype.str)
	except:
		formats.append("U64")


#Cargamos los datos
data = np.genfromtxt("data/datos_A.csv", delimiter=";", 
	dtype={'names': nom_col,'formats': formats},
	 skip_header=1, filling_values='0', converters={2: punto_travieso})

#Indicadores
# 0: nacidos vivos por residencia materna
# 1: muertes fetales tardías por residencia materna
# 2: matrimonios por el lugar en que han fijado residencia
# 3: fallecidos por el lugar de residencia
# 4: crecimiento vegetativo

print(" "*3)
print("---- 1. Series por nacidos vivos por residencia materna ----")
print(" "*3)
print("*Ver figura*")

municipio = data[0::5][nom_col[0]]
#Como sabemos que el indicador se repite una vez cada 5, haciendo saltos de 5, siempre cogeremos el mismo indicador
nacidos_vivos = data[0::5][nom_col[2]] 

# plot
x = municipio
y = nacidos_vivos

plt.plot(x, y, marker='o', linestyle='--')
plt.xticks(rotation=90)
plt.xlabel(nom_col[0])
plt.title("Nacidos vivos por residencia materna")

plt.show()


print(" "*3)
print("---- 2. Serie ordenada por fallecidos por el luegar de residencia ----")
print(" "*3)
print("*Ver figura*")

fallecidos = data[3::5][nom_col[2]]

#Para poder ordenar los municipios, tendremos que empaquetarlos junto a los datos de fallecidos, los cuales si podemos ordenar
mun_fall = list(zip(fallecidos,municipio))
mun_fall.sort()
fall_ordenado, mun_ordenado = zip(*mun_fall)

# plot
x = mun_ordenado
y = fall_ordenado

plt.plot(x, y, marker='o', linestyle='--')
plt.xticks(rotation=90)
plt.xlabel(nom_col[0])
plt.title("Serie ordenada por fallecidos por el luegar de residencia")

plt.show()

print(" "*3)
print("---- 3. Media de cada indicador----")
print(" "*3)

#Calculamos la media de cada indicador
media_nacidos = round(np.mean(data[0::5][nom_col[2]]), 3)
print("Media nacidos vivos por residencia materna: ", media_nacidos)

media_muertes = round(np.mean(data[1::5][nom_col[2]]), 3)
print("Media muertes fetales tardías por residencia materna: ", media_muertes)

media_matrimonios = round(np.mean(data[2::5][nom_col[2]]), 3)
print("Media matrimonios por el lugar en que han fijado residencia: ", media_matrimonios)

media_fallecidos = round(np.mean(data[3::5][nom_col[2]]), 3)
print("Media fallecidos por el lugar de residencia: ", media_fallecidos)

media_crecimiento = round(np.mean(data[4::5][nom_col[2]]), 3)
print("Media crecimiento vegetativo: ", media_crecimiento)


print(" "*3)
print("---- 4. Desviación de cada indicador----")
print(" "*3)

#Calculamos la desviación de cada indicador
desv_nacidos = round(np.std(data[0::5][nom_col[2]]), 3)
print("Desviación nacidos vivos por residencia materna: ", desv_nacidos)

desv_muertes = round(np.std(data[1::5][nom_col[2]]), 3)
print("Desviación muertes fetales tardías por residencia materna: ", desv_muertes)

desv_matrimonios = round(np.std(data[2::5][nom_col[2]]), 3)
print("Desviación matrimonios por el lugar en que han fijado residencia: ", desv_matrimonios)

desv_fallecidos = round(np.std(data[3::5][nom_col[2]]), 3)
print("Desviación fallecidos por el lugar de residencia: ", desv_fallecidos)

desv_crecimiento = round(np.std(data[4::5][nom_col[2]]), 3)
print("Desviación crecimiento vegetativo: ", desv_crecimiento)