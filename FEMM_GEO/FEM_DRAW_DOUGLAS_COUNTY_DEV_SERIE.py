#PROYECTO: FEM WITH PYTHON FOR POWER TRANSFORMERS

#Douglas County PUD
#fert: 16087896

import femm

from  DevanadosGeo import drawdevanado
from  DevanadosGeo import drawdevbase

from  DevanadosGeo import drawdevanadoRegGap

# Inicio y conexión con FEMM
femm.openfemm()

# Creación de nuevo documento
femm.newdocument(1)  # Electrostatic problem

# Definición de ei_probdef(units, type, precision, depth, minangle)
# En la interfaz indicar con selección si es planar o axisimétrica la simulación

sele = 2  # Cambiar el valor según la simulación deseada

if sele == 1:
    femm.ei_probdef('millimeters', 'planar', 10 ** (-8), 10 ** 6, 30)
    print("Conf: Milímetros, Planar, 1e-8, 30")
elif sele == 2:
    femm.ei_probdef('millimeters', 'axi', 10 ** (-8), 0, 30)
    print("Conf: Milímetros, Axisimétrica, 1e-8, 30")

# --------------------------------------|COMIENZO DIBUJO|-----------------------------------------
#------------Dibujando nucleo------------#
AltVentanaNucleo=790
AnchVentanaNucleo=390
DiametroNucleo=305
CabSupAT=50+90
CabinfAT=50

femm.ei_drawrectangle(DiametroNucleo/2,0, AnchVentanaNucleo, AltVentanaNucleo)

#desplazamiento del centro de la ventana por cabeceras en la vertical
dy=-abs(AltVentanaNucleo/2-CabSupAT-(AltVentanaNucleo-CabSupAT-CabinfAT)/2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev serie-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=600
Radial=47
DiamInt=345
axial_cond=10.886

kraft=0.61
drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev común-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=600
Radial=83
DiamInt=499
axial_cond=13.336

kraft=0.46
drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)



input("Simulación terminada. Presiona Enter para salir...")