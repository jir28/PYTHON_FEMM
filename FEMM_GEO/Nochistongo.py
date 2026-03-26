#PROYECTO: FEM WITH PYTHON FOR POWER TRANSFORMERS

import femm
from  DevanadosGeo import drawdevanado
from  CoreGeo import drawcore
from CoreGeo import draw_arandela_sup_inf
from  windingmaterials import materials
from AislamientosGeo import drawpackcil
from globals_array import  obtener_alturas,obtener_cabecerassup, obtener_cabecerasinf,obtener_radiales,obtener_dimint

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
    AltVentanaNucleo = 2140
    AnchVentanaNucleo = 545
    DiametroNucleo = 640
    CabSupAT=120 + 130
    CabInfAT=120+30

#Para dibujar el nucleo se necesita tener toras las cabeceras y alturas en arreglos
dy=drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo,  CabSupAT, CabInfAT)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev TER-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1760
Radial=31
DiamInt=682
axial_cond=13.039
Boundaryvoltage=80000
cabsup=115
cabinf=115

kraft=0.0

NumTiras = 28
AnchoEspaciador = 30
EsptiraInt = 6
EsptiraExt = 6



drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi,
             Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev LV-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1770
Radial=58
DiamInt=974
axial_cond=16.486
Boundaryvoltage=0.0
cabsup=110
cabinf=110

kraft=1.07

NumTiras = 28
AnchoEspaciador = 30
EsptiraInt = 8
EsptiraExt = 6



drawdevanado("BoundLV",Boundaryvoltage,AltVentanaNucleo,AltAxi,
             Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev REG AT-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1770
Radial=23
DiamInt=1190
axial_cond=12.436
Boundaryvoltage=0.0
cabsup=110
cabinf=110

kraft=1.22

NumTiras = 28
AnchoEspaciador = 40
EsptiraInt = 8
EsptiraExt = 6



drawdevanado("BoundREGAT",Boundaryvoltage,AltVentanaNucleo,AltAxi,
             Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev REG AT-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1750
Radial=87
DiamInt=1376
axial_cond=10.702
Boundaryvoltage=0.0
cabsup=130+120
cabinf=120+20

kraft=2.29

NumTiras = 56
AnchoEspaciador = 19
EsptiraInt = 8
EsptiraExt = 8



drawdevanado("BoundAT",Boundaryvoltage,AltVentanaNucleo,AltAxi,
             Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy)

#-----------------------------------------------------------------Dibujando CILINDROS-----------------------------------------------------------------------------------#

#print("Alturas dev:", obtener_alturas())
#print("cab sup dev:", obtener_cabecerassup())
#print("cab inf dev:", obtener_cabecerasinf())
print("radialesdev:", obtener_radiales())
print("diamdev:", obtener_dimint())

#Una vez dibujados todos los devanados se mandan a llamar las cabeceras inferior y superior, asi como alturas axiales del devanado, esto permite dibujar el núcleo y cilindros

CabecerasDevinf=obtener_cabecerasinf()
CabecerasDevSup=obtener_cabecerassup()
AlturasAxiDev=obtener_alturas()
Radialesdev=obtener_radiales()
DiamIntdev=obtener_dimint()
#------------------- CORE-TER-----------------------

DimInt_inicial = 640


# Espacios entre cilindros (ductos)
ductos = [12, 6]
#alturas
alturascil_recortesup=[0,0]
alturascil_recorteinf=[0,0]
# Espesores de cada cilindro
radiales = [3]

drawpackcil(DimInt_inicial,AltVentanaNucleo, radiales,ductos,dy,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev,alturascil_recortesup,alturascil_recorteinf)



#------------------- CORE-TER-----------------------

DimInt_inicial = 744


# Espacios entre cilindros (ductos)
ductos = [6, 8,8,8,8,10,10,10,8,8,9,8]
#alturas
alturascil_recortesup=[0,0,0,0,0,0,0,0,0,0,0]
alturascil_recorteinf=[0,0,0,0,0,0,0,0,0,0,0]
# Espesores de cada cilindro
radiales = [2,1,1,1,1,1,1,1,1,1,3]

drawpackcil(DimInt_inicial,AltVentanaNucleo, radiales,ductos,dy,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev,alturascil_recortesup,alturascil_recorteinf)


#------------------- LV - REGAT-----------------------

DimInt_inicial = 1090


# Espacios entre cilindros (ductos)
ductos = [6, 8,10,10,8]
#alturas
alturascil_recortesup=[0,0,0,0]
alturascil_recorteinf=[0,0,0,0]
# Espesores de cada cilindro
radiales = [2,1,1,4]

drawpackcil(DimInt_inicial,AltVentanaNucleo, radiales,ductos,dy,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev,alturascil_recortesup,alturascil_recorteinf)

#------------------- REGAT -AT-----------------------

DimInt_inicial = 1236


# Espacios entre cilindros (ductos)
ductos = [6,8,9,10,10,10,8]
#alturas
alturascil_recortesup=[0,0,0,0,0,10]
alturascil_recorteinf=[0,0,0,0,0,5]
# Espesores de cada cilindro
radiales = [2,1,1,1,1,3]

drawpackcil(DimInt_inicial,AltVentanaNucleo, radiales,ductos,dy,CabecerasDevinf,CabecerasDevSup,AlturasAxiDev,alturascil_recortesup,alturascil_recorteinf)


#-----------------------------------------------------------------Dibujando proteccion arandela sup - inf-----------------------------------------------------------------------------------#

draw_arandela_sup_inf(AltVentanaNucleo,AlturasAxiDev,Radialesdev,DiamIntdev,CabecerasDevSup,CabecerasDevinf,3,3,dy)



#EJECUTRANDO SOLUCION Y MUESTRA DE RESULTADOS
femm.ei_zoomnatural()
femm.ei_saveas("Nochistongo.fee")
#femm.ei_createmesh()     # Genera la malla
#femm.ei_showmesh()       # Ocultar la malla

input("Sectores dibujados. Presiona Enter para salir...")
