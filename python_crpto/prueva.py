import vigenere
import TurningGrill  
import playfair
import hill
import caesar
import cv2
import Aes

print('vigerere: ',vigenere.vigenere(1,'dfa','dsfd',4))
print('Turning Grill: ',TurningGrill.turningrill(4,[1,10,12,15],1,2,'jkdt staa aiwm ncat'))
print('playfair: ',playfair.playfair('acsh',1,'sdfja'))
print('hill: ',hill.hill(2,11,8,3,7,'dojmnnoufcna'))
print('caesar: ',caesar.caesar(1,'snaj',3))
