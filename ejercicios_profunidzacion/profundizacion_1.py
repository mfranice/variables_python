# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.1

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

#Ingreso de variables por teclado
print('Ingrese el primer número con el que quiere operar: ')
numero_1 = float(input())
print('Ingrese el segundo número con el que quiere operar: ')
numero_2 = float(input())

#SUMA
resultado = numero_1 + numero_2
print ('La suma entre', numero_1, 'y', numero_2, 'es:', resultado)

#RESTA
resultado = numero_1 - numero_2
print ('La resta de', numero_1, 'menos', numero_2, 'es:', resultado)

#MULTIPLICACIÓN
resultado = numero_1 * numero_2
print ('La multiplicación entre', numero_1, 'y', numero_2, 'es:', resultado)

#DIVISIÓN
resultado = numero_1 / numero_2
print ('La división de', numero_1, 'por', numero_2, 'es:', resultado)

#POTENCIA
resultado = numero_1 ** numero_2
print ('El resultado de elevar', numero_1, 'a la potencia de', numero_2, 'es:', resultado)