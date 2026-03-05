#PROYECTO: FEM WITH PYTHON FOR POWER TRANSFORMERS

#SCOUT CLEAN ENERGY
#fert: C18789150

import femm
import math
from  DevanadosGeo import drawdevanado
from  CoreGeo import drawcore
from FEMM_GEO.DevanadosGeo import drawdevanadoRegGap
from  windingmaterials import materials
from AislamientosGeo import drawpackcil_barreras
from globals_array import  obtener_alturas, obtener_cabecerassup, obtener_cabecerasinf

# Inicio y conexión con FEMM
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

    #información general del dibujo para dibujar el núcleo
    #CabecerasDevSup = [185, 60, 140 + 80, 495]
    #CabecerasDevinf = [185, 60, 80+30, 495]
    #AlturasAxiDev = [2000, 2250, 2210, 1380]
    AltVentanaNucleo = 2540
    AnchVentanaNucleo = 950
    DiametroNucleo = 900



 # Determinando tacon B y D


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev TER-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2000
Radial=13
DiamInt=948
axial_cond=15.8462
Boundaryvoltage=180000
cabsup=185
cabinf=185

kraft=0.0

NumTiras = 28
AnchoEspaciador = 25
EsptiraInt = 6
EsptiraExt = 11





drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev bt-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2250
Radial=52
DiamInt=1018
axial_cond=11.523
Boundaryvoltage=0.0
cabsup=60
cabinf=60
kraft=0.0

drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev Hv-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2210
Radial=112
DiamInt=1336
axial_cond=12.986
Boundaryvoltage=0.0
cabsup=140+80
cabinf=80+30
kraft=1.37
drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev REG-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

AltAxi=1380
Radial=41
DiamInt=1704
axial_cond=12.836
separacion=800
Boundaryvoltage=0.0
cabsup=495
cabinf=495
kraft=1.22
drawdevanadoRegGap(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,0,separacion)


#-----------------------------------------------------------------Dibujando CILINDROS-----------------------------------------------------------------------------------#

#print("Alturas dev:", obtener_alturas())
#print("Alturas dev:", obtener_cabecerassup())
#print("Alturas dev:", obtener_cabecerasinf())

#Una vez dibujados todos los devanados se mandan a llamar las cabeceras inferior y superior, asi como alturas axiales del devanado, esto permite dibujar el núcleo y cilindros

CabecerasDevinf=obtener_cabecerasinf()
CabecerasDevSup=obtener_cabecerassup()
AlturasAxiDev=obtener_alturas()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#------------------- CORE-TER-----------------------
   #c1
DimInt_inicial = 900
altaxicil = 2250

# Espacios entre cilindros (ductos)
ductos = [13, 8]

# Espesores de cada cilindro
radiales = [3]

drawpackcil_barreras(DimInt_inicial,AltVentanaNucleo, radiales,ductos,0,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev)

#------------------- TER-LV-----------------------
# c1
DimInt_inicial = 974
altaxicil = 2250

# Espacios entre cilindros (ductos)
ductos = [9, 10]
# Espesores de cada cilindro
radiales = [3]
drawpackcil_barreras(DimInt_inicial,AltVentanaNucleo, radiales,ductos,0,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev)


#------------------- LV-HV-----------------------
DimInt_inicial = 1122
altaxicil = 2250

# Espacios entre cilindros (ductos)
ductos = [6, 10, 10, 10, 11,10,10,10,10,8]  # uno antes de cada cilindro

# Espesores de cada cilindro
radiales = [2, 1, 1, 1, 1, 1,1,1,3]

drawpackcil_barreras(DimInt_inicial,AltVentanaNucleo, radiales,ductos,0,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev)
#------------------- HV-REG-----------------------

DimInt_inicial = 1560
altaxicil = 2250

# Espacios entre cilindros (ductos)
ductos = [6, 8, 10, 8, 10,8,8]  # uno antes de cada cilindro

# Espesores de cada cilindro
radiales = [2, 2,2,2,2,4]

drawpackcil_barreras(DimInt_inicial,AltVentanaNucleo, radiales,ductos,0,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev)

# ------------Dibujando nucleo------------#
#Para dibujar el nucleo se necesita tener toras las cabeceras y alturas en arreglos
drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, AlturasAxiDev, CabecerasDevinf, CabecerasDevSup)



#EJECUTRANDO SOLUCION Y MUESTRA DE RESULTADOS
femm.ei_zoomnatural()
femm.ei_saveas("Scout.fee")
femm.ei_createmesh()     # Genera la malla
femm.ei_showmesh()       # Ocultar la malla
#femm.ei_analyze()        # Analizar
#femm.ei_loadsolution()   # Cargarsolucion


input("Simulación terminada. Presiona Enter para salir...")