import PIL
import numpy as np
from ArcosAngulares import ArcosAngulares
from PresilhaEsquerda import PresilhaEsquerda
from PresilhaDireita import PresilhaDireita
from Versticilos import Versticilos
from PIL import Image

class Pessoa():
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
    
    def getArcoAngular(self):
        meuArcoAngular = ArcosAngulares(self.fonte,self.nome)
        arco1 = meuArcoAngular.getAngular1(self.fonte,self.nome)
        arco2 = meuArcoAngular.getAngular2(self.fonte,self.nome)
        arcos = [sum(arco1),sum(arco2)]
        return arcos

        
    def getVerticios(self):
        meuVersticio = Versticilos(self.fonte,self.nome)
        verticilio1 = meuVersticio.getVerticilo1(self.fonte,self.nome)
        verticilio2 = meuVersticio.getVerticilo2(self.fonte,self.nome)
        verticilio3 = meuVersticio.getVerticilo3(self.fonte,self.nome)
        verticilios = [sum(verticilio1),sum(verticilio2),sum(verticilio3)]
        return verticilios

    def getPresilhaDireita(self):
        minhaPresilha = PresilhaDireita(self.fonte,self.nome)
        presilha1 = minhaPresilha.getPresilha1(self.fonte,self.nome)
        presilha2 = minhaPresilha.getPresilha2(self.fonte,self.nome)
        presilhas = [sum(presilha1),sum(presilha2)]
        return presilhas
    
    def getPresilhaEsquerda(self):
        minhaPresilha = PresilhaEsquerda(self.fonte,self.nome)
        presilha1 = minhaPresilha.getPresilha1()
        presilha2 = minhaPresilha.getPresilha2()
        presilhas = [sum(presilha1),sum(presilha2)]
        return presilhas

#geraldo = Pessoa("Impressao_digital.jpg","Geraldo")
#print(geraldo.getVerticios())
