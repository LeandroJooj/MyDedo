import PIL
import numpy as np
import math
from PIL import Image
from Shaper import shaper
np.seterr(divide='ignore', invalid='ignore')

class Versticilos():
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

    def getVerticilo1(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        img.convert("L")
        #print(img.mode)        
        pixels = img.crop((200,200,340,340))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        #print(pixels.shape)
        pixels = pixels.astype("float32")        
        pixels = np.around(pixels)
        return sum(pixels)

    def getVerticilo2(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((400,500,500,650))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        pixels = pixels.astype("float32")
        pixels = np.around(pixels)
        return sum(pixels)

    def getVerticilo3(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((150,500,250,650))
        pixels = np.asarray(pixels)
        tam = pixels.size
        y = shaper(tam)
        x =round(tam/y)
        pixels.reshape(x,y)
        pixels = pixels.astype("float32")
        pixels = np.around(pixels)
        return sum(pixels)
