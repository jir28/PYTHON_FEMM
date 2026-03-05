import femm
import math
from  DevanadosGeo import drawdevanado
from  CoreGeo import drawcore
from FEMM_GEO.DevanadosGeo import drawdevanadoRegGap
from  windingmaterials import materials
from AislamientosGeo import drawcilindro
femm.openfemm()
femm.newdocument(1)
materials()
# Creación de nuevo documento


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

 # ------------Dibujando nucleo------------#
    AltVentanaNucleo = 2140
    AnchVentanaNucleo = 545
    DiametroNucleo = 640
    CabSupAT = 130 + 120
    CabinfAT = 120+20

    dy = drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, CabSupAT, CabinfAT)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev TER-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1760
Radial=31
DiamInt=682
axial_cond=13.039
Boundaryvoltage=80000

kraft=0.0
drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev BT-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1770
Radial=58
DiamInt=974
axial_cond=16.486
Boundaryvoltage=0.0

kraft=1.07
drawdevanado("BoundBT",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev AT2 -REG-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1770
Radial=23
DiamInt=1190
axial_cond=12.436
Boundaryvoltage=0.0

kraft=1.22
drawdevanado("BoundREG",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev AT1-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1750
Radial=87
DiamInt=1376
axial_cond=10.702
Boundaryvoltage=0.0

kraft=2.29
drawdevanado("BoundAT",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)




#EJECUTRANDO SOLUCION Y MUESTRA DE RESULTADOS
femm.ei_zoomnatural()
femm.ei_saveas("Nochistongo.fee")
femm.ei_createmesh()     # Genera la malla
femm.ei_showmesh()       # Ocultar la malla
input("Simulación terminada. Presiona Enter para salir...")