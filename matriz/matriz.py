def verificar_solucion(matriz):
    # Verifica las filas
    for i in range(9):
        if sum(matriz[i]) != 45:  
            return False, f"Fila {i + 1} es incorrecta"
    
    # Verifica las columnas
    for j in range(9):
        columna = [matriz[i][j] for i in range(9)]
        if sum(columna) != 45:
            return False, f"Columna {j + 1} es incorrecta"
    
    return True, "La solución es correcta"

# Ejemplo de uso
matriz_solucion = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


es_correcta, mensaje = verificar_solucion(matriz_solucion)
print(mensaje)
