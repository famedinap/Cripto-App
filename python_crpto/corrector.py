def corregir(texto):
    text=texto.lower()
    newtext=''
    for i in text:
        if esta(i):
            newtext=newtext+i

    return newtext

def esta(n):
    caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    for i in caracteres:
        if i==n:
            return True
    return False

print(corregir('pErrO se7tenta{ h64pta'))