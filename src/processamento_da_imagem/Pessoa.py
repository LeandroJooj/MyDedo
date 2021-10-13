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
        while(not(isinstance(arcos,np.float64))):
            arcos = sum(arcos)
        return arcos

        
    def getVerticios(self):
        meuVersticio = Versticilos(self.fonte,self.nome)
        verticilio1 = meuVersticio.getVerticilo1(self.fonte,self.nome)
        verticilio2 = meuVersticio.getVerticilo2(self.fonte,self.nome)
        verticilio3 = meuVersticio.getVerticilo3(self.fonte,self.nome)
        verticilios = sum([sum(verticilio1),sum(verticilio2),sum(verticilio3)])
        while not(isinstance(verticilios,np.float64)):
            verticilios = sum(verticilios)
        return verticilios

    def getPresilhaDireita(self):
        minhaPresilha = PresilhaDireita(self.fonte,self.nome)
        presilha1 = minhaPresilha.getPresilha1(self.fonte,self.nome)
        presilha2 = minhaPresilha.getPresilha2(self.fonte,self.nome)
        presilhas = [sum(presilha1),sum(presilha2)]
        while(not(isinstance(presilhas,np.float64))):
            presilhas = sum(presilhas)
        return presilhas
    
    def getPresilhaEsquerda(self):
        minhaPresilha = PresilhaEsquerda(self.fonte,self.nome)
        presilha1 = minhaPresilha.getPresilha1(self.fonte,self.nome)
        presilha2 = minhaPresilha.getPresilha2(self.fonte,self.nome)
        presilhas = [sum(presilha1),sum(presilha2)]
        while(not(isinstance(presilhas,np.float64))):
            presilhas = sum(presilhas)
        return presilhas



geraldo = Pessoa("digital9.jpg","Geraldo")
print("Geraldo: ",geraldo.getArcoAngular())
print("Geraldo: ",geraldo.getVerticios())
print("Geraldo: ",geraldo.getPresilhaDireita())
print("Geraldo: ",geraldo.getPresilhaEsquerda())

print("--------------------------------")
kevin = Pessoa("digital13.jpg","Kevin")
print("Kevin: ",kevin.getArcoAngular())
print("Kevin: ",kevin.getVerticios())
print("Kevin: ",kevin.getPresilhaDireita())
print("Kevin: ",kevin.getPresilhaEsquerda())


print("--------------------------------")
carlos = Pessoa("digital14.jpg","Carlos")
print("Carlos: ",carlos.getArcoAngular())
print("Carlos: ",carlos.getVerticios())
print("Carlos: ",carlos.getPresilhaDireita())
print("Carlos: ",carlos.getPresilhaEsquerda())


print("--------------------------------")
mark = Pessoa("digital15.jpg","Mark")
print("Mark: ",mark.getArcoAngular())
print("Mark: ",mark.getVerticios())
print("Mark: ",mark.getPresilhaDireita())
print("Mark: ",mark.getPresilhaEsquerda())

print("--------------------------------")
indiana = Pessoa("digital16.jpg","Indiana")
print("Indiana: ",indiana.getArcoAngular())
print("Indiana: ",indiana.getVerticios())
print("Indiana: ",indiana.getPresilhaDireita())
print("Indiana: ",indiana.getPresilhaEsquerda())


print("--------------------------------")
george = Pessoa("Impressao_digital.jpg","George")
print("George: ",george.getArcoAngular())
print("George: ",george.getVerticios())
print("George: ",george.getPresilhaDireita())
print("George: ",george.getPresilhaEsquerda())



