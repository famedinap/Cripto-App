import cv2
import numpy as np
import base64
import pyaes
import os

def aes(nivel,prueba):
    retval, buffer  = cv2.imencode('.png',prueba) 
    data = base64.b64encode(buffer)


    if nivel==1:
        key = os.urandom(16)
    elif nivel==2:
        key= os.urandom(24)
    elif nivel == 3:
        key = os.urandom(32)
    else:
        print('no voy a hacer nada')


    aes = pyaes.AESModeOfOperationCTR(key)
    d = aes.encrypt(data)
    baseencode=base64.b64encode(d)
    #print('texto en base 64: ',baseencode)
    basedecode=base64.b64decode(baseencode)
    aes = pyaes.AESModeOfOperationCTR(key)
    decripted=aes.decrypt(basedecode)

    nparr = np.frombuffer(base64.b64decode(decripted), np.uint8)
    img2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return baseencode

