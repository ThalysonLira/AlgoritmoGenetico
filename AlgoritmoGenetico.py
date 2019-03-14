# -*- coding: utf-8 -*-
"""
AlgoritmoGenetico
"""
import numpy as np

class AlgoritmoGenetico:
    def __init__(self, POP_TAM, GENE_TAM, CARGA_MAX = 3.1):
        print("Algoritmo Genetico")
        self.POP_TAM = POP_TAM
        self.GENE_TAM = GENE_TAM
        self.POP = []
        self.POP_AUX = []
        self.APTIDAO = []
    
    def populacao_inicial(self):
        print("Criando populacao inicial!")
        
        for i in range(self.POP_TAM):
            self.POP.append(np.random.randint(0, 2, self.GENE_TAM))
            
    def cruzamento_simples(self, pai1, pai2):
        print("Cruzamento com 1 ponto de corte.")
        
        desc1 = np.zeros(self.GENE_TAM, int)
        desc2 = np.zeros(self.GENE_TAM, int)
        
        for i in range(self.GENE_TAM):
            if i < self.GENE_TAM / 2:
                desc1[i] = self.POP[pai1][i]
                desc2[i] = self.POP[pai2][i]
            else:
                desc1[i] = self.POP[pai2][i]
                desc2[i] = self.POP[pai1][i]
                
        self.POP_AUX.append(desc1)
        self.POP_AUX.append(desc2)
        
    def cruzamento_uniforme(self, pai1, pai2):
        print("Cruzamento com 1 ponto de corte.")
        
        desc1 = np.zeros(self.GENE_TAM, int)
        desc2 = np.zeros(self.GENE_TAM, int)
        
        for i in range(self.GENE_TAM):
            if np.random.randint(0, 2) == 0:
                desc1[i] = self.POP[pai1][i]
                desc2[i] = self.POP[pai2][i]
            else:
                desc1[i] = self.POP[pai2][i]
                desc2[i] = self.POP[pai1][i]
                
        self.POP_AUX.append(desc1)
        self.POP_AUX.append(desc2)
        
    def avaliacao(self):
        livros = []
        livros.append(0.6)
        livros.append(1.6)
        livros.append(0.8)
        livros.append(0.7)
        livros.append(1.2)
        livros.append(0.3)
        livros.append(0.1)
        livros.append(1.4)
        livros.append(1.3)
        livros.append(0.5)
        
        self.APTIDAO = []
        
        for i in range(self.POP_TAM):
            peso = 0.0
            for g in range(self.GENE_TAM):
                peso += (self.POP[i][g] * livros[g])
             
            if peso <= self.CARGA_MAX:
                self.APTIDAO.append(peso)
            else:
                self.APTIDAO.append(0.0)
                
    def substituicao(self):
        self.POP = self.POP_AUX.copy()        
        self.POP_AUX = []
                
                
                