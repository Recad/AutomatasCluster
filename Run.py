#! /usr/bin/env python3
import sys
from poblacion import *
import matplotlib
matplotlib.use('Agg')
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import threading

#Clase encargada de iniciar la apliación
class formulario():
	def __init__(self, parent=None):
		self.my_arraysp1 = []
		self.my_arraysp2 = []
		self.my_arraysp3 = []
        

		self.IndiceP1=float(sys.argv[1])
		self.IndiceP2=float(sys.argv[2])
		self.IndiceP3=float(sys.argv[3])

    #Valida los datos de entrada
	def ValidarDatos(self):
		self.IndiceP1 = float(sys.argv[1])
		self.IndiceP2 = float(sys.argv[2])
		self.IndiceP3 = float(sys.argv[3])

		self.IndicePropa1 = float(sys.argv[4])
		self.IndicePropa2 = float(sys.argv[5])
		self.IndicePropa3 = float(sys.argv[6])

		self.IndiceViaje1 = float(sys.argv[7])
		self.IndiceViaje2 = float(sys.argv[8])
		self.IndiceViaje3 = float(sys.argv[9])

		self.Vistas = int(sys.argv[10])
		self.iteraciones = int(sys.argv[11])

		self.muertes = int(sys.argv[12])



		if ( (self.IndiceP1 > 0.0 and self.IndiceP2>0.0 and self.IndiceP3>0.0) and (self.IndicePropa1 > 0.0 and self.IndicePropa2>0.0 and self.IndicePropa3>0.0) and (self.IndiceViaje1 > 0.0 and self.IndiceViaje1>0.0 and self.IndiceViaje1>0.0)):

			if (self.Vistas >= (self.iteraciones)) or (self.muertes > self.iteraciones):
				return False

			else:
				return True
		else:
			return False

    #TRanforma un indice dado por el usuario en una probabilidd del sistema
	def DefProbabilidades(self, percentil):

		return math.floor((1/percentil)*100)

    #lanza la app
	def lanzar(self):

		if self.ValidarDatos():

			self.poblaci = Poblacion(True, "pobla1")
			self.poblaci2 = Poblacion(False, "pobla2")
			self.poblaci3 = Poblacion(False, "pobla3")
			self.poblaci.poblar(self.DefProbabilidades(self.IndiceP1))
			self.poblaci2.poblar(self.DefProbabilidades(self.IndiceP2))
			self.poblaci3.poblar(self.DefProbabilidades(self.IndiceP3))
			self.poblaci.infectarIndividuo()
            
			self.iterar()

			#self.ImprimirMat(self.poblaci.name, self.my_arraysp1)
			#self.ImprimirMat(self.poblaci2.name, self.my_arraysp2)
			#self.ImprimirMat(self.poblaci3.name, self.my_arraysp3)


			self.LimpiarMats()
		else:
			
			print("Error in inputs")
           

    #realiza las acciones de las iteraciones
	def iterar(self):
		for i in range(0, self.iteraciones):
            #Inicio de las iteraciones de movimiento
			self.poblaci.realizarIteracionMovimiento()
			self.poblaci2.realizarIteracionMovimiento()
			self.poblaci3.realizarIteracionMovimiento()
            #-----------------------------------------------------------------------------------------------------------



            #Inicio de la propagación
			self.poblaci.PropagacionVirus(self.DefProbabilidades(self.IndicePropa1))
			self.poblaci2.PropagacionVirus(self.DefProbabilidades(self.IndicePropa2))
			self.poblaci3.PropagacionVirus(self.DefProbabilidades(self.IndicePropa3))
            #-----------------------------------------------------------------------------------------------------------

            # Liminacion de muertos de las poblaciones
			if (self.muertes > 0):
				self.poblaci.eliminarMuertos(self.muertes)
				self.poblaci2.eliminarMuertos(self.muertes)
				self.poblaci3.eliminarMuertos(self.muertes)
            # -----------------------------------------------------------------------------------------------------------


            #Inicio de los posibles viajes entre poblaciones
            #Poblacion origen entregando viajeros
			self.poblaci2.recibirIndividuo(self.poblaci.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje1)))
			self.poblaci3.recibirIndividuo(self.poblaci.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje1)))
            #Poblacion 2 entregando viajeros
            #self.poblaci.recibirIndividuo(self.poblaci2.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje2)))
			self.poblaci3.recibirIndividuo(self.poblaci2.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje2)))
            #Poablación 3 entregando individuos
			self.poblaci2.recibirIndividuo(self.poblaci3.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje3)))
            #self.poblaci.recibirIndividuo(self.poblaci3.EntregarIndividuo(self.DefProbabilidades(self.IndiceViaje3)))

			if i % self.Vistas == 0:

				self.ImprimirMat(self.poblaci.name, self.poblaci.PrintMatNice(),i)
				self.ImprimirMat(self.poblaci2.name, self.poblaci2.PrintMatNice(),i)
				self.ImprimirMat(self.poblaci3.name, self.poblaci3.PrintMatNice(),i)
				#self.my_arraysp1.append(self.poblaci.PrintMatNice())
				#self.my_arraysp2.append(self.poblaci2.PrintMatNice())
				#self.my_arraysp3.append(self.poblaci3.PrintMatNice())

    #Limpia las matrices
	def LimpiarMats(self):
		self.my_arraysp1 = []
		self.my_arraysp2 = []
		self.my_arraysp3 = []

    #IMprime las matrices
	def ImprimirMat(self,name,array,indice):


		cmap = ListedColormap(['White', 'Blue', 'Red'])
	
		
		#f,axarr = plt.subplots()

		#f.subplots_adjust(hspace=0.4, wspace=0.4)
			

		#axarr.set_title("T :" + str(indice))
		#fig = axarr.get()

		plt.imsave('Resultado-' + name + "vista:" + str(indice)+ '.png',array, cmap=cmap,  vmin=0, vmax=2)

		#manager = plt.get_current_fig_manager()
		#manager.resize(*manager.window.maxsize())


		#plt.savefig('Resultado ' + name + '.png')
		#manager.canvas.set_window_title(name)
		#plt.show()





if __name__ == '__main__':
   

    myapp = formulario()
    myapp.lanzar()


