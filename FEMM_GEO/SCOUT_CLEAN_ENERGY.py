#PROYECTO: FEM WITH PYTHON FOR POWER TRANSFORMERS

#SCOUT CLEAN ENERGY
#fert: C18789150

import femm
import math
from  DevanadosGeo import drawdevanado
from  CoreGeo import drawcore
from FEMM_GEO.DevanadosGeo import drawdevanadoRegGap
from  windingmaterials import materials
from AislamientosGeo import drawcilindro


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
 # ------------Dibujando nucleo------------#
    AltVentanaNucleo = 2540
    AnchVentanaNucleo = 950
    DiametroNucleo = 900
    CabSupAT = 140 + 80
    CabinfAT = 80+30

    dy = drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, CabSupAT, CabinfAT)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev TER-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2000
Radial=13
DiamInt=948
axial_cond=15.8462
Boundaryvoltage=180000

kraft=0.0
drawdevanado("BoundTer",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev bt-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2250
Radial=52
DiamInt=1018
axial_cond=11.523
Boundaryvoltage=0.0

kraft=0.0
drawdevanado("BoundLV",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev Hv-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=2210
Radial=112
DiamInt=1336
axial_cond=12.986
Boundaryvoltage=0.0

kraft=1.37
drawdevanado("BoundHV",Boundaryvoltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev REG-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

AltAxi=1380
Radial=41
DiamInt=1704
axial_cond=12.836
separacion=800
Boundaryvoltage=0.0

kraft=1.22
drawdevanadoRegGap(AltVentanaNucleo,AltAxi,Radial,axial_cond, DiamInt,kraft,dy,separacion)


#------------------- CORE-TER-----------------------
   #c1
altaxicil=2250
radialCil=1
DimInt=900+(8*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

#------------------- TER-LV-----------------------
   #c1
altaxicil=2250
radialCil=3
DimInt=974+(11*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)


#------------------- LV-HV-----------------------
   #c1
altaxicil=2250
radialCil=2
DimInt=1122+(6*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

   #c2
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

   #c3
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)


   #C4
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)


  #C5
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2+1*2+11*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C6
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2+1*2+11*2+1*2+10*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C7
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2+1*2+11*2+1*2+10*2+1*2+10*2) #este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C8
altaxicil=2250
radialCil=1
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2+1*2+11*2+1*2+10*2+1*2+10*2+2*1+10*2) #este parámetro lo calcula el usuario
drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)


  #C9
altaxicil=2250
radialCil=3
DimInt=1122+(6*2+2*2+10*2+1*2++10*2+2+10*2+1*2+11*2+1*2+10*2+1*2+10*2+2*1+10*2+1*2+10*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

#------------------- HV-REG-----------------------

  #C1
altaxicil=2250
radialCil=2
DimInt=1560+(6*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C2
altaxicil=2250
radialCil=2
DimInt=1560+(6*2+2*2+8*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C3
altaxicil=2250
radialCil=2
DimInt=1560+(6*2+2*2+8*2+2*2+10*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C4
altaxicil=2250
radialCil=2
DimInt=1560+(6*2+2*2+8*2+2*2+10*2+2*2+8*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C5
altaxicil=2250
radialCil=2
DimInt=1560+(6*2+2*2+8*2+2*2+10*2+2*2+8*2+2*2+10*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)

  #C6
altaxicil=2250
radialCil=4
DimInt=1560+(6*2+2*2+8*2+2*2+10*2+2*2+8*2+2*2+10*2+2*2+8*2)#este parámetro lo calcula el usuario

drawcilindro(DimInt,AltVentanaNucleo,altaxicil, radialCil,dy)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando PROTECCIONES SUPERIOR EN INF-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#ESPESOR TACON B Y D

DimInt=948
DimExt=974
NumTiras=28
AnchoEspaciador=25
EsptiraInt=6
EsptiraExt=11


pi=math.pi
Num=((DimInt - EsptiraInt)*pi-NumTiras*19)*EsptiraInt  +  ((DimExt+EsptiraExt)*pi-NumTiras*19)*EsptiraExt
Den=(DimExt+EsptiraExt)*pi-NumTiras*(AnchoEspaciador+10)

B=(Num/Den)

print(B)

#EJECUTRANDO SOLUCION Y MUESTRA DE RESULTADOS
femm.ei_zoomnatural()
femm.ei_saveas("Scout.fee")
femm.ei_createmesh()     # Genera la malla
femm.ei_showmesh()       # Ocultar la malla
#femm.ei_analyze()        # Analizar
#femm.ei_loadsolution()   # Cargarsolucion


input("Simulación terminada. Presiona Enter para salir...")