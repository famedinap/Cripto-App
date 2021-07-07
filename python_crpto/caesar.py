def quitarespacios(texto):    
    for i in texto:
        if i == ' ':
            texto.remove(i)
    return texto

def encriptar(msg,k):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    mensaje=quitarespacios(list(msg))
    encriptado=['']
    while mensaje:               
        p1=mensaje.pop(0)                   
        a=posicion(p1,caracteres)
        if a+k>=26:
            b=(a+k)-len(caracteres)
            encriptado.append(caracteres[b]) 
        else:
            encriptado.append(caracteres[a+k])      
    return encriptado

def posicion(p1,matriz):
    a=0
    for i in range(len(matriz)):           
        if matriz[i]==p1:
            a=i                    
    return a

def desencriptar(msg,k):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    mensaje=quitarespacios(list(msg))
    encriptado=['']
    while mensaje:               
        p1=mensaje.pop(0)                   
        a=posicion(p1,caracteres)
        if a-k<0:
            b=(a-k)
            encriptado.append(caracteres[26+b]) 
        else:
            encriptado.append(caracteres[a-k])       
    return encriptado

def caesar(con,mensaje,k):
    resultado=''
    if con==1:
        encripted=encriptar(mensaje,k)
        pi=""
        for i in encripted:
            pi+=i
        resultado=pi
    elif con==2:
        decripted=desencriptar(mensaje,k)
        pi=""
        for i in decripted:
            pi+=i
        resultado=pi
    else:
        print("no voy a hacer nada, no escogio una opcion valida")
    
    return resultado