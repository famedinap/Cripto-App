from sympy import Matrix, pprint

global caracteres
caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def inversamodular(a,b,c,d):
    A = Matrix([
        [a,b],
        [c,d]
    ])
    ainv = A.inv_mod(26)
    return ainv

def matriz(a,b,c,d):
    A = Matrix([
        [a,b],
        [c,d]
    ])   
    return A

def quitarespacios(texto):    
    for i in texto:
        if i == ' ':
            texto.remove(i)
    return texto

def posicion(p1):
    a=0
    for i in range(len(caracteres)):            
            if caracteres[i]==p1:
                a=i                    
    return a

def mensaje(msg):
    mensaje=quitarespacios(list(msg))
    if len(mensaje)%2==1:
        mensaje.append('x')
    return mensaje

def encriptar(matrize,mensaj):
    mensajee=mensaje(mensaj)
    encriptado=[' ']
    while mensajee:
        vector=[posicion(mensajee.pop(0)),posicion(mensajee.pop(0))]
        x=((vector[0]*matrize[0,0])+(vector[1]*matrize[1,0]))%26
        y=((vector[0]*matrize[0,1])+(vector[1]*matrize[1,1]))%26        
        encriptado.append(caracteres[x])
        encriptado.append(caracteres[y])   
    return encriptado

def hill(con,a,b,c,d,mensaje):
    resultado=''
    if con==1:
        matrize=matriz(a,b,c,d)
        encripted=encriptar(matrize,mensaje)
        pi=""
        for i in encripted:
            pi+=i
        resultado=pi
    elif con==2:
        matrizinversa=inversamodular(a,b,c,d)
        decripted=encriptar(matrizinversa,mensaje)
        pi=""
        for i in decripted:
            pi+=i
        resultado=pi
    else:
        print("no voy a hacer nada, no escogio una opcion valida")
    return resultado