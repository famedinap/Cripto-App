import cv2
import numpy as np
import base64
from pyDes import *


def des2(prueba):
    retval, buffer  = cv2.imencode('.png',prueba) 
    data = base64.b64encode(buffer)


    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    baseencode=base64.b64encode(d)
    #print('texto en base 64: ',baseencode)
    basedecode=base64.b64decode(baseencode)
    decripted=k.decrypt(d)

    nparr = np.frombuffer(base64.b64decode(decripted), np.uint8)
    img2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return baseencode

