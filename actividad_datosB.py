
##======================================================##
##                                                      ##
##   Numpy - Datos B                                    ##
##                                                      ##
##   Autor: George Ababei                               ##
##   Universidad: Universitat de les Illes Balears      ##
##                                                      ##
##======================================================##

import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

plt.style.use('_mpl-gallery')

#Función para reemplazar las comas que separan miles y millones para poder tratarlos como float
def coma_traviesa(x):
   resultado = [float(i.replace(",", "")) for i in x]
   return resultado

#Recogemos los nombres y el número de columnas
datos_str = np.genfromtxt("data/datos_B.csv", delimiter=";", dtype=str)
nom_col=datos_str[0]
numero_col=nom_col.size
print(nom_col)

#Miramos el tipo de datos de cada columna
formats=[]
for i in range(numero_col):
	try:
		columna = np.genfromtxt("data/datos_B.csv", delimiter=";", dtype=None, encoding=None,
		 skip_header=1, usecols=i, filling_values='0')
		formats.append(columna.dtype.str)
	except:
		formats.append("U64")

#Cargamos los datos
data = np.genfromtxt("data/datos_B.csv", delimiter=";", 
	dtype={'names': nom_col,'formats': formats},
	 skip_header=1, filling_values='0')

print(data)
print(" "*3)
codigo_postal=11358
print("---- 1. El precio medio de las casas con código postal",codigo_postal, " ----")
print(" "*3)

#Para poder manipular este tipo de dataset, hay que tener en cuenta que su formato es un array de tuplas, no es un dataset 2D
#Por tanto, para este caso usaremos los comandos de esta forma data[0][0] y no así data[0,0]
c = np.where(data["Postcode"]==codigo_postal)
precios = coma_traviesa(data[c]["price"])
media_precios= np.mean(precios)
print("El precio medio de las casas con código postal %s es: " %codigo_postal, media_precios , "$")



print(" "*3)
print("---- 2. Serie ordenada de los precios de las viviendas situadas en la calle AMSTERDAM AVENUE ----")
print(" "*3)
print("Ver figura")

location = np.where(data['str_name']=='AMSTERDAM AVENUE')
precios = coma_traviesa(data[location]["price"])
#Usaremos el crfn para identificar cada casa
precio_casa = list(zip(precios, data[location]["crfn"].astype(str)))
precio_casa.sort()
precio, crfn = zip(*precio_casa)

# plot
x = crfn
y = precio
plt.plot(x, y, marker='o', linestyle='--')
plt.xticks(rotation=90)
plt.xlabel("Crfn de las viviendas")
plt.title("Serie ordenada de los precios de las viviendas situadas en la calle AMSTERDAM AVENUE")

plt.show()

print(" "*3)
print("---- 3. ¿Qué empresa ha comprado más viviendas durante el primer cuartil del año 2020? ----")
print(" "*3)

compras_21 = np.where(data['yearqtr']=='2020Q1')
unique, counts = np.unique(data[compras_21]["grantee"], return_counts=True)
num_viviendas = list(zip(counts, unique))
num_viviendas.sort(reverse=True)
print("La empresa que más viviendas ha comprado durante el primer cuartil del año 2020 es",num_viviendas[0][1],"con un total de", num_viviendas[0][0], "viviendas" )


print(" "*3)
print("---- 4. ¿Que día y en que calle se vendió la vivienda más cara? ----")
print(" "*3)

precios = coma_traviesa(data['price'])
vivienda_cara = list(zip(precios, data["str_name"], data["deed_date"]))
vivienda_cara.sort(reverse=True)
print("La vivienda más cara a la venta de Nueva York se compró el dia",vivienda_cara[0][2],"en la calle",vivienda_cara[0][1],"por un total de",vivienda_cara[0][0],"$")
