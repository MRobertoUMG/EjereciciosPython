
class matrizDispersa:
    def __init__(self):
        self.matrix = []
       

    def cargar_csv_a_matriz(self,archivo):        
        for linea in archivo:
            self.matrix.append(linea)
            
    def mostrar_matriz(self):
        for linea in self.matrix:
        #for ele in linea:
            #print(ele)
            print(linea)

nMatriz = matrizDispersa()           

nombre_archivo = input("Introduce el nombre del archivo: ")
with open(nombre_archivo, "r") as archivo:
   
        #matrix.append([linea])
        nMatriz.cargar_csv_a_matriz(archivo)

nMatriz.mostrar_matriz()