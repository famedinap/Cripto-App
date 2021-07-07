def gmatriz(cl:list):
    caracteres =['a','b','c','d','e','f','g','h','ij','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cl=convertij(cl)       
    cont=0
    for i in cl:
        if cl.count(i)>1:
            while cl.count(i)!=0:
                cl.remove(i)
            cl.insert(cont,i)
        cont=cont+1
    cont=0
    for i in cl:
        caracteres.remove(i)
        caracteres.insert(cont,i)
        cont=cont+1
    matr=contruirmatriz(caracteres)    
    return matr

def convertij(cl):
    for i in range(len(cl)+1) :
        if cl[i-1]=='i':
            cl[i-1]='ij'
    for i in range(len(cl)+1) :
        if cl[i-1]=='j':
            cl[i-1]='ij'  
    return cl

def contruirmatriz(caracteres):
    matr=[['a',0,0,0,0],[0,0,0,0,0],['3',0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]    
    cont=1
    for i in range(len(caracteres)):
        if cont<=5:            
            matr[0][cont-1]=caracteres[i]
        elif cont>5 and cont<=10:                       
            matr[1][cont-6]=caracteres[i]       
        elif cont>10 and cont<=15:            
            matr[2][cont-11]=caracteres[i]
        elif cont>15 and cont<=20:
            matr[3][cont-16]=caracteres[i]
        elif cont>20 and cont<=25:
            matr[4][cont-21]=caracteres[i]
        cont=cont+1
    return matr
        

def quitarespacios(texto):    
    for i in texto:
        if i == ' ':
            texto.remove(i)
    return texto

def encriptar(matriz,msg):
    mensaje=quitarespacios(list(msg))
    mensaje=convertij(mensaje)
    encriptado=['']
    while mensaje:
        p1=''
        p2=''
        if len(mensaje)>2:
            p1=mensaje.pop(0)
            p2=mensaje.pop(0)
        else:
            p1=mensaje.pop(0)
            p2='x' 
               
        ab=posicion(p1,matriz)
        a=ab[0]
        b=ab[1]
        cd=posicion(p2,matriz)
        c=cd[0]
        d=cd[1]        
        encriptado=cript(a,b,c,d,matriz,encriptado)
    return encriptado    
        
        
def posicion(p1,matriz):
    a,b=0,0
    for i in range(5):
            for j in range(5):
                if matriz[i][j]==p1:
                    a=i
                    b=j
    return a,b

def cript(a,b,c,d,matriz,encriptado):    
    if a==c:            
            if b==4:
                encriptado.append(matriz[a][0])
                encriptado.append(matriz[c][d+1])            
            elif d==4:
                encriptado.append(matriz[a][b+1])
                encriptado.append(matriz[c][0])
            else:
                encriptado.append(matriz[a][b+1])
                encriptado.append(matriz[c][d+1])
    elif b==d:
        if a==4:
            encriptado.append(matriz[0][b])
            encriptado.append(matriz[c+1][d])
        elif c==4:
            encriptado.append(matriz[a+1][b])
            encriptado.append(matriz[0][d])
        else:
            encriptado.append(matriz[a+1][b])
            encriptado.append(matriz[c+1][d])
    else:
        encriptado.append(matriz[a][d])
        encriptado.append(matriz[c][b])
    return encriptado


def desencriptar(matriz,msg):
    msg=list(msg)
    for i in range(len(msg)+1) :
        if msg[i-1]=='i':
            msg[i-1]=' '
    mensaje=quitarespacios(msg)    
    mensaje=convertij(mensaje)
    desencriptado=['']
    while mensaje:        
        p1=mensaje.pop(0)
        p2=mensaje.pop(0)               
        ab=posicion(p1,matriz)
        a=ab[0]
        b=ab[1]
        cd=posicion(p2,matriz)
        c=cd[0]
        d=cd[1]        
        desencriptado=decript(a,b,c,d,matriz,desencriptado)
    return desencriptado 

def decript(a,b,c,d,matriz,desencriptado):    
    if a==c:            
            if b==0:
                desencriptado.append(matriz[a][4])
                desencriptado.append(matriz[c][d-1])            
            elif d==0:
                desencriptado.append(matriz[a][b-1])
                desencriptado.append(matriz[c][4])
            else:
                desencriptado.append(matriz[a][b-1])
                desencriptado.append(matriz[c][d-1])
    elif b==d:
        if a==0:
            desencriptado.append(matriz[4][b])
            desencriptado.append(matriz[c-1][d])
        elif c==0:
            desencriptado.append(matriz[a-1][b])
            desencriptado.append(matriz[4][d])
        else:
            desencriptado.append(matriz[a-1][b])
            desencriptado.append(matriz[c-1][d])
    else:
        desencriptado.append(matriz[a][d])
        desencriptado.append(matriz[c][b])
    return desencriptado

def  playfair(clave,con,mensaje):

    g=quitarespacios(list(clave))
    matriz=gmatriz(g)
    resultado=''
    if con==1:
        encripted=encriptar(matriz,mensaje)
        pi=""
        for i in encripted:
            pi+=i
        resultado=pi
    elif con==2:
        decripted=desencriptar(matriz,mensaje)
        pi=""
        for i in decripted:
            pi+=i
        resultado=pi
    else:
        print("no voy a hacer nada, no escogio una opcion valida")
    
    return resultado