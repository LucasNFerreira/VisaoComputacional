# estou a importar as bibliotecas matplotlib e numpy.
from matplotlib import pyplot as plt
import numpy as np 

# defino os meus dados e criterios iniciais.
tolerance=10
start_altimetry=100
x=np.array([0,10,20,30,40,50,60,70,80,90])
y=np.array([4,5,6,5,6,7,8,9,8,7])
x2=np.array([0,0,10,20,30,40,50,60,70,80,90,90])
y2=np.array([0,4,5,6,5,6,7,8,9,8,7,0])

# Esta e a classe que vai plotar uma nova linha cada vez que eu fizer um click no grafico.
class LineBuilder:
    def __init__(self, line):
        self.line = line
        # Aqui esta a ser criado o primeiro ponto da lista que eventualmente vai ser plotada.
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        # Aqui estamos a ligar a acao de carregar num botao do rato com um evento que vamos definir a seguir.
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        if event.inaxes!=self.line.axes: return
        # Aqui actualizamos a lista com um segundo ponto (dois pontos temos uma recta!!!).
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        # Aqui estou a redefinir a escala do meu grafico para poder continuar a desenhar as linhas
        # ao longo de todo o meu perfil de terreno.
        plt.xlim([event.xdata -tolerance,event.xdata+tolerance])
        # e desenho os novos dados.
        self.line.figure.canvas.draw()

# Criacao do canvas para ver a figura e atribuicao de um titulo.
fig = plt.figure()
