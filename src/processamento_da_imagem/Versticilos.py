import PIL
import numpy as np
from PIL import Image

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
        pixels = img.crop((200,200,340,340))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        # pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)

    def getVerticilo2(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((400,500,500,650))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(pixels, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)

    def getVerticilo3(self,fonte,nome):
        img = Image.open("imagens/"+fonte)
        pixels = img.crop((150,500,250,650))
        pixels = np.asarray(pixels)
        pixels = pixels.astype("float32")
        pixels /= pixels.max()
        #pyplot.imshow(img, cmap="binary")
        pixels = np.around(pixels)
        return sum(pixels)
