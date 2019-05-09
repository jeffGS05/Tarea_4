hoja_calculo = [['carlos', 'juan', 'luis'],
 [5.454, 0.554, 0.954],
 [6.57, 9.57, 7.57],
 [3.64, 4.64, 1.64],]
# Parte 1
# Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
#
# Promedio
#
# La suma
#
# La multiplicación

import math
nombre,cvalor,jvalor,lvalor=hoja_calculo
calculo_dic = {'suma':lambda a,b,c: a+b, 'resta':lambda a,b,c: a-b,'promedio': lambda a: max(), 'multi': lambda a,b,c: a*b*c, 'Impuesto': lambda a: a*1.2,}

# Parte 2
# Obtenga utilizando el diccionario de funciones:

#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.

print("El promedio de la cantidad miles de colones en débito es : " + str(calculo_dic['suma'](cvalor[0],jvalor[0],lvalor[0])))
El promedio de la cantidad miles de colones en débito es : 12.024000000000001
# 2. La suma de todas las deudas

print("La suma de todas las deudas es de : " + str(calculo_dic['suma'](cvalor[2],jvalor[2],lvalor[2])))
#La suma de todas las deudas es de : 8.524000000000001
# 3. la multiplicación de todos los crédito entre si

print("3. La multiplicación de todos los crédito entre si es de : " + str(calculo_dic['multi'](cvalor[1],jvalor[1],lvalor[1])))
La multiplicación de todos los crédito entre si es de : 24.600259200000004

# Parte 3
# Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2)
# a toda la fila de créditos usando el diccionario de funciones.

hoja_calculo[1][1] = calculo_dic['Impuesto'](hoja_calculo[1][1])
hoja_calculo[2][1] = calculo_dic['Impuesto'](hoja_calculo[2][1])
hoja_calculo[3][1] = calculo_dic['Impuesto'](hoja_calculo[3][1])

print("Se le aplico un impuesto del 20% a las lineas de credito de los usuarios " , nombre[0],hoja_calculo[1][1], ':',nombre[1], hoja_calculo[2][1], ':',nombre[2], hoja_calculo[3][1])
Se le aplico un impuesto del 20% a las lineas de credito de los usuarios  'carlos', 0.6648000000000001 juan 11.484 luis 5.568











