import PIL
import numpy as np
from PIL import Image
from Shaper import shaper
np.seterr(divide='ignore', invalid='ignore')

class ArcosAngulares():
    def __init__(self, fonte,nome):
        self.fonte = fonte
        self.nome = nome
            
    def getAngular1(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        img.convert("L")
        pixels = img.crop((260,450,340,550))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        pixels = pixels.astype("float32")
        return sum(pixels)

    def getAngular2(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        img.convert("L")
        pixels = img.crop((260,250,340,350))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        pixels = pixels.astype("float32")
        
        return sum(pixels)

    def getNome(self):
        return self.nome

    def setNome(self,NovoNome):
        self.nome = NovoNome
    
    def getFonte(self):
        return self.fonte
    
    def setFonte(self, NovaFonte):
        self.fonte = NovaFonte
    
