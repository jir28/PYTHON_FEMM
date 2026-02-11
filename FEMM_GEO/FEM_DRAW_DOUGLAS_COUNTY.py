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
AltVentanaNucleo=1800
AnchVentanaNucleo=740
DiametroNucleo=610
CabSupAT=110+150
CabinfAT=160

femm.ei_drawrectangle(DiametroNucleo/2,0, AnchVentanaNucleo, AltVentanaNucleo)

#desplazamiento del centro de la ventana por cabeceras en la vertical
dy=-abs(AltVentanaNucleo/2-CabSupAT-(AltVentanaNucleo-CabSupAT-CabinfAT)/2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev BT1-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=950
Radial=12
DiamInt=644
axial_cond=17.07

kraft=1.07
drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev BT2-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1420
Radial=60
DiamInt=716
axial_cond=8.191

kraft=0.0
drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev AT1-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1380
Radial=127
DiamInt=992
axial_cond=9.74

kraft=1.22
drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)



input("Simulación terminada. Presiona Enter para salir...")