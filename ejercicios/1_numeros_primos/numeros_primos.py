import math

#funcion para desviacion estandar
def desviacion(arr):
    return math.sqrt(varianza(arr))
    
#funcion para varianza
def varianza(arr):
    m = media(arr)
    return sum((x - m) ** 2 for x in arr) / len(arr)


#funcion para media de los numeros primos
def media(arr):
    return sum(arr) / len(arr)

#Funcion para obtener numeros primos
def es_primo(num):
    #Descarrta los numeros menores a 2 (0 y 1)
    if num < 2:
        return False
    for i in range(2, num -1): #comprueba los divisores
        if num % i == 0:
            return False
    return True

# Funcion para obtener los primeros 500 numeros
def n_primos(n):
    n_primos = []
    num = 2
    while len(n_primos) < n:
        if es_primo(num):
            n_primos.append(num)
        num += 1
    return n_primos

n_primos = n_primos(500)
print("Primos:", n_primos)
print("Media:", media(n_primos), "Varianza:", varianza(n_primos),"Desviacion Estandar:", desviacion(n_primos))