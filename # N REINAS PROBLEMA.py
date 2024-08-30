# N REINAS PROBLEMA
import copy
tablero = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(8)]
         


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
    soluciones=[]
    if numero_reinas == 0:
        return [copy.deepcopy(matriz)]
    
    for i in range(len(matriz)):
        
        nuevaMatriz=copy.deepcopy(matriz)
        nuevoArreglo=[len(matriz)-numero_reinas,i]
        
        if confirmar(nuevaMatriz,nuevoArreglo):
            nuevaMatriz[len(matriz)-numero_reinas][i]=1
            
            matrizSolucion=N_reinas(nuevaMatriz, numero_reinas - 1)
            if matrizSolucion:
                soluciones.extend(matrizSolucion)
            
            
    return soluciones


soluciones = N_reinas(tablero,len(tablero))

if soluciones:
    print("Se encontró una o mas soluciónes:")
    print(soluciones)
    print(len(soluciones))
else:
    print("No se encontró ninguna solución.")