import numpy as np
from graphviz import Digraph
import matplotlib.pyplot as plt

class matrizDispersa:
    def __init__(self):
        self.mat = []
       

    def cargar_csv_a_matriz(self,archivo):        
        for linea in archivo:
            self.mat.append(linea)
            
    def mostrar_matriz(self):
        for linea in self.mat:
            #for ele in linea:
                #print(linea[ele])
            print(linea)

    def insertar_matriz(self):
        n_row = int(input("Ingrese el numero de filas que desea insertar en la matriz: "))
        n_col = int(input("Ingrese el numero de columnas que desea insertar en la matriz: "))
        for i in range(n_row):
            insert_matriz_manual = []
            print(f"---- Ingrese los datos de la FILA  {i+1} ----")
            for j in range(n_col):
                edad = int(input("Edad de las personas que presentan la insuficiencia: "))
                insert_matriz_manual.append(edad)
        self.mat.append(insert_matriz_manual)

    #numero = input("Número de personas por insuficiencia cardíaca()")
    
    def generar_grafica(self, matrix):
           # Crear un gráfico dirigido
        dot = Digraph()

        # Obtener dimensiones de la matriz
        rows, cols = matrix.shape

        # Crear nodos para cada celda de la matriz
        for i in range(rows):
            for j in range(cols):
                # Agregar nodos con etiquetas de fila y columna
                dot.node(f'{i}_{j}', label=str(matrix[i][j]))

                # Agregar nodos adicionales para unir las celdas
                if i < rows - 1:
                    dot.node(f'{i+1}_{j}', label='', style='invisible')
                    dot.edge(f'{i}_{j}', f'{i+1}_{j}', style='invisible')
                if j < cols - 1:
                    dot.node(f'{i}_{j+1}', label='', style='invisible')
                    dot.edge(f'{i}_{j}', f'{i}_{j+1}', style='invisible')

        # Dibujar el gráfico
        dot.attr(rankdir='LR')
        dot.attr(splines='line')
        dot.attr(dpi='300')
        dot.attr(label=f'Matrix\n{matrix}', fontsize='12')
        dot.attr(fontsize='10')
        dot.format = 'png'
        dot.render('matrix_graph', cleanup=True)

        # Mostrar la imagen generada
        img = plt.imread('matrix_graph.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    

nMatriz = matrizDispersa()           

'''nombre_archivo = input("Introduce el nombre del archivo: ")
with open(nombre_archivo, "r") as archivo:
   
        #matrix.append([linea])
        nMatriz.cargar_csv_a_matriz(archivo)'''


#------------------------------------------------------------------------------#

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

#nMatriz.generar_grafica(nMatriz.mat)
nMatriz.insertar_matriz()
nMatriz.mostrar_matriz()

