# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

recorte_1 = palabra_1 [:3]
print('El recorte de la primera palabra ingresada es: ', recorte_1)
recorte_2 = palabra_2 [:2]
print('El recorte de la segunda palabra ingresada es: ', recorte_2)
print('La palabra que se forma con los recortes de las ingresadas es la siguiente: ', recorte_1 + recorte_2)