import PIL
import numpy as np
from PIL import Image

class ArcosAngulares():
    def __init__(self, fonte,nome):
        self.fonte = fonte
        self.nome = nome
            
    def getAngular1(fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((260,450,340,550))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        return sum(pixels)

    def getAngular2(fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((260,250,340,350))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        return sum(pixels)

    def getNome(self):
        return self.nome

    def setNome(self,NovoNome):
        self.nome = NovoNome
    
    def getFonte(self):
        return self.fonte
    
    def setFonte(self, NovaFonte):
        self.fonte = NovaFonte
    
