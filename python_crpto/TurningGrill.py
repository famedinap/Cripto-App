def genmatriz(tamano):
    matriz = [[0 for x in range(tamano)]for y in range(tamano)]
    for i in range(tamano):
        for j in range(tamano):            
            matriz[i][j]=i+j+1+(i*(tamano-1))
    return matriz

def posicion(p1,matriz,tamano):
    a,b=0,0
    for i in range(tamano):
            for j in range(tamano):
                if matriz[i][j]==p1:
                    a=i
                    b=j
    return a,b

def quitarespacios(texto):    
    for i in texto:
        if i == ' ':
            texto.remove(i)
    return texto

def rotar(matriz):        
    rotada=[]  
    for i in range(len(matriz[0])):
        rotada.append([])
        for j in range(len(matriz)):
            rotada[i].append(matriz[len(matriz)-1-j][i])        
    return rotada

def asignar(tamano,grilla,encriptado,mensaje):
    for k in range(tamano):
        for l in range(tamano):
            if grilla[k][l]==0 and mensaje:
                encriptado[k][l]=mensaje.pop(0)    
    return encriptado,mensaje

def imp(grilla):
    for j in range(len(grilla)):
	    print(grilla[j])

def encriptar(tamano,grilla,direccion,msg):
    mensaje=quitarespacios(list(msg))
    encriptado=[[0 for x in range(tamano)]for y in range(tamano)]
    for i in range(4):
        aux=asignar(tamano,grilla,encriptado,mensaje)
        encriptado=aux[0]
        mensaje=aux[1]
        grilla=rotar(grilla)
        if direccion==2:
            grilla=rotar(grilla)
            grilla=rotar(grilla)
    return encriptado 

def encolar(tamano,grilla,desencriptado,matriz):
    for k in range(tamano):
        for l in range(tamano):
            if grilla[k][l]==0:
                desencriptado+=matriz[k][l]
    return desencriptado

def desencriptar(tamano,grilla,direccion,msg):
    
    mensaje=quitarespacios(list(msg))
    matriz=[[0 for x in range(tamano)]for y in range(tamano)]
    desencriptado=[' ']
    for i in range(tamano):
        for j in range(tamano):
            matriz[i][j]=mensaje.pop(0)
    for i in range(4):
        desencriptado = encolar(tamano,grilla,desencriptado,matriz)
        grilla=rotar(grilla)
        if direccion==2:
            grilla=rotar(grilla)
            grilla=rotar(grilla)
    return desencriptado

def imprimir(encriptado,k):
    mensaje=[" "] 
    pi=""   
    for i in range(k):
        for j in range(k):            
            mensaje+=encriptado[i][j]
    mensaje=quitarespacios(mensaje)
    while mensaje:
        for i in range(k):
            if mensaje:
                pi+=mensaje.pop(0)
            else:
                break
        pi+=" "        
    return pi
    
def imprimir1(mensaje,k):
    pi=""
    mensaje=quitarespacios(mensaje)
    while mensaje:
        for i in range(k):
            if mensaje:
                pi+=mensaje.pop(0)
            else:
                break
        pi+=" "
    return pi

def turningrill(tamaño,hoyos,direccion,con,mensaje):

    grilla=genmatriz(tamaño)
    
    for i in hoyos:
        pos=posicion(i,grilla,tamaño)
        grilla[pos[0]][pos[1]]=0
    resultado=''
    if con==1:
        encripted=encriptar(tamaño,grilla,direccion,mensaje)
        resultado=imprimir(encripted,tamaño)
    elif con==2:    
        decripted=desencriptar(tamaño,grilla,direccion,mensaje)
        resultado=imprimir1(decripted,5)        
    else:
        print("no voy a hacer nada, no escogio una opcion valida")
    
    return resultado