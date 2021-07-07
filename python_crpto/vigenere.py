def crearmatriz():
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    matriz = [[0 for x in range(26)]for y in range(26)]
    cont=0
    for i in range(26):
        for j in range(26):
            if j+cont<26:
                matriz[i][j]=caracteres[j+cont]
            else:
                matriz[i][j]=caracteres[j+cont-26]
        cont=cont+1
    return matriz

def quitarespacios(texto):    
    for i in texto:
        if i == ' ':
            texto.remove(i)
    return texto

def posicion(p1,matriz):
    a=0
    for i in range(len(matriz)):           
        if matriz[i]==p1:
            a=i                    
    return a

def encriptar(matriz,clave,msg):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    mensaje=quitarespacios(list(msg))
    encriptado=[' ']
    while mensaje:
        aux1=mensaje.pop(0)
        aux2=clave.pop(0)
        pos1=posicion(aux1,caracteres)
        pos2=posicion(aux2,caracteres)
        clave.append(aux2)
        encriptado.append(matriz[pos1][pos2])
    return encriptado

def buscar(pos,car,matriz):
    encontrado:int=0    
    for i in range(26):
        if matriz[pos][i]==car:
            encontrado=i            
    return encontrado

def desencriptar(matriz,clave,msg):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    mensaje=quitarespacios(list(msg))
    desencriptado=[' ']
    while mensaje:
        aux1=mensaje.pop(0)
        aux2=clave.pop(0)
        pos1=posicion(aux2,caracteres) 
        pos2=buscar(pos1,aux1,matriz)       
        clave.append(aux2)
        desencriptado.append(matriz[pos2][0])
    return desencriptado


def imprimir(mensaje,k):
    pi=''
    mensaje=quitarespacios(mensaje)
    while mensaje:
        for i in range(k):
            if mensaje:
                pi+=mensaje.pop(0)
            else:
                break
        pi+=" "
    return pi

def vigenere(con,clave,mensaje,valork):
    
    matriz=crearmatriz()
    clave=list(clave)

    resultado=''

    if con==1:
        encripted=encriptar(matriz,clave,mensaje)
        resultado=imprimir(encripted,valork)
    elif con==2:
        decripted=desencriptar(matriz,clave,mensaje)
        resultado=imprimir(decripted,valork)
    else:
        print("no voy a hacer nada, no escogio una opcion valida")
    
    return resultado