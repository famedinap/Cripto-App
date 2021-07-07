from flask import Flask, request, jsonify
from flask.json import jsonify
from flask.wrappers import Request
from flask_cors import CORS, cross_origin
import hill
import cv2
import Aes
import Des
import vigenere
import TurningGrill  
import playfair
import hill
import caesar
import corrector

prueba=cv2.imread('yosoyironman.png')

app = Flask(__name__)
CORS(app)
cors = CORS(app,resourses={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/aes')
def aesf():
    return Aes.aes(3,prueba)[0]

@app.route('/caesar',methods=['POST'])
def caesarf(): 
    if request.method == 'POST':
        encriptod = int(request.form['encript'] )       
        mensaje = request.form['mensaje']
        k = int(request.form['k'])
        return caesar.caesar(encriptod,corrector.corregir(mensaje),k),{"Access-Control-Allow-Origin":"*"}

@app.route('/des')
def desvigeneref():
    return Des.des2(prueba)

@app.route('/hill',methods=['POST'])
def hillf():
    if request.method == 'POST':
        encriptod = request.form['encript'] 
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        d = int(request.form['d'])
        mensaje = request.form['mensaje']
        encriptod=int(encriptod)
        return hill.hill(encriptod,a,b,c,d,corrector.corregir(mensaje))

@app.route('/playfair',methods=['POST'])
def playfairf():
    if request.method == 'POST':
        clave = request.form['clave']
        encriptod = request.form['encript']      
        mensaje = request.form['mensaje']
        encriptod=int(encriptod)
        return playfair.playfair(corrector.corregir(clave),encriptod,corrector.corregir(mensaje))

@app.route('/turningGrill', methods=['POST'])
def turninggrillf():
    if request.method == 'POST':
        tamaño = request.form['tamaño']
        hoyos = request.form['hoyos']
        direccion = request.form['direccion']
        encriptod = request.form['encript']
        mensaje = request.form['mensaje']  
        hoyos= list(hoyos)
        def esta(n):
            numeros=['1','2','3','4','5','6','7','8','9','0']
            for i in numeros:
                if i==n:
                    return True
            return False
        aux=''
        lista=[]
        for i in hoyos:
            if i!='[':
                if esta(i):
                    aux=aux+i
                else:
                    lista.append(aux)
                    aux=''
        lista1=[]
        for i in lista:
            lista1.append(int(i))
        print(lista)
        print(hoyos,type(mensaje))
          
        return TurningGrill.turningrill(int(tamaño[0]),lista1,int(direccion[0]),int(encriptod[0]),corrector.corregir(mensaje))  

@app.route('/vigenere', methods=['POST'])
def vigenerek():
    if request.method == 'POST':
        encriptod = request.form['encript'],
        clave = request.form['clave'],
        mensaje = request.form['mensaje'],
        valork = request.form['valork']
        encriptod1=int(encriptod[0])
        valork1=int(valork[0])        
        responsed =vigenere.vigenere(encriptod1,corrector.corregir(clave[0]),corrector.corregir(mensaje[0]),valork1)
        return responsed

if __name__ =='__main__':
    app.run(port=5000,debug =True)