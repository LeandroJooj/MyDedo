import PIL
import numpy as np
from PIL import Image
from Shaper import shaper
np.seterr(divide='ignore', invalid='ignore')
class PresilhaEsquerda():

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

    def getPresilha1(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        img.convert("L")
        pixels = img.crop((300,200,450,350))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)

    def getPresilha2(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        img.convert("L")
        pixels = img.crop((180,580,270,700))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)

        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)
