import PIL
import numpy as np
from PIL import Image

class PresilhaDireita():
    def __init__(self, fonte,nome):
        self.fonte = fonte
        self.nome = nome
        
    def getNome(self):
        return self.nome

    def setNome(self,NovoNome):
        self.nome = NovoNome
    
    def getFonte(self):
        return self.fonte
    
    def setFonte(self, NovaFonte):
        self.fonte = NovaFonte
                
    def getPresilha1(fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((300,480,450,580))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)

    def getPresilha2(fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((150,200,250,300))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)
