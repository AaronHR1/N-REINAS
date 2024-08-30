# N REINAS PROBLEMA
import copy
tablero = [[0, 0, 0, 0] for _ in range(4)]
         


def confirmar(matriz,valor_insertado):
    print(valor_insertado[0],valor_insertado[1])
    
    fila=valor_insertado[0]
    columna=valor_insertado[1]
    
    for i in range(len(matriz)):
        if i!=columna and matriz[fila][i]==1:
            return False
    
    for j in range(len(matriz)):
        if j!=fila and matriz[j][columna]==1:
            return False
    
    
    fila_temp=valor_insertado[0] -1 
    columna_temp=valor_insertado[1] -1
    
    
    #arriba izq
    while columna_temp>=0 and fila_temp>=0:
        if matriz[fila_temp][columna_temp] ==1:
            return False
        columna_temp-=1
        fila_temp-=1
        
    fila_temp=valor_insertado[0] +1
    columna_temp=valor_insertado[1] -1
    
    #abajo izq
    while columna_temp>=0 and fila_temp<len(matriz):
        if matriz[fila_temp][columna_temp] ==1:
            return False
        columna_temp-=1
        fila_temp+=1   
        
    fila_temp=valor_insertado[0] -1 
    columna_temp=valor_insertado[1] +1
    
    #arriba derecha
    while columna_temp<len(matriz) and fila_temp>=0:
        if matriz[fila_temp][columna_temp] ==1:
            return False
        columna_temp+=1
        fila_temp-=1
    
    fila_temp=valor_insertado[0] +1 
    columna_temp=valor_insertado[1] +1
    
    #abajo derecha
    while columna_temp<len(matriz) and fila_temp<len(matriz):
        if matriz[fila_temp][columna_temp] ==1:
            return False
        columna_temp+=1
        fila_temp+=1
    
    
    return True
    

def N_reinas(matriz,numero_reinas):
    if numero_reinas == 0:
        return matriz
    
    for i in range(len(matriz)):
        
        nuevaMatriz=copy.deepcopy(matriz)
        nuevoArreglo=[len(matriz)-numero_reinas,i]
        
        if confirmar(nuevaMatriz,nuevoArreglo):
            nuevaMatriz[len(matriz)-numero_reinas][i]=1
            resultado = N_reinas(nuevaMatriz, numero_reinas - 1)
            if resultado:
                return resultado
        
        
        N_reinas(nuevaMatriz,numero_reinas-1)
    


solucion = N_reinas(tablero,len(tablero))

if solucion:
    print("Se encontró una solución:")
    for fila in solucion:
        print(fila)
else:
    print("No se encontró ninguna solución.")