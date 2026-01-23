#PROYECTO:
import femm

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



# ====================== DIBUJANDO DEVANADOS Y NUCLEO ======================

#------------Dibujando nucleo------------#
AltVentanaNucleo=2150
AnchVentanaNucleo=785
DiametroNucleo=735

femm.ei_drawrectangle(DiametroNucleo/2,0, AnchVentanaNucleo, AltVentanaNucleo)

# Agregar arcos en las esquinas internas del núcleo
    #femm.ei_drawarc(DiametroNucleo/2,0, AnchVentanaNucleo, AltVentanaNucleo,90,1)
    #femm.mi_createradius(DiametroNucleo/2,0,0.1)
#------------Dibujando dev ter------------#
AltAxi=1830
Radial=15
DiamInt=777


# --------MINI ANGULO/ANILLO ANGULAR -------
axial_cond=18.076

ax=round(axial_cond-1)
ra=Radial+2





aislamiento=2 #indica que es cordex, aislamiento =2 indica papel kraft

if aislamiento == 1:
    # --------DEV SIN AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt/2,(AltVentanaNucleo-AltAxi)/2,DiamInt/2+Radial , (AltVentanaNucleo+AltAxi)/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5)
    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 )
    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 )
    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 )

    # --------MINI ANGULO--------
    femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1)
    femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1)
    femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1, 0.5 + 1)
    femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1, 0.5  + 1)



elif aislamiento == 2:
    kraft=0.46
    # --------DEV CON AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2)
    femm.ei_drawrectangle(DiamInt/2+  kraft/2,(AltVentanaNucleo-AltAxi)/2+  kraft/2,DiamInt/2+Radial-  kraft/2 , (AltVentanaNucleo+AltAxi)/2 -  kraft/2)

    #--------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)

    # --------MINI ANGULO--------
    femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1)
    femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1)
    femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax)
    femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1, 0.5+ kraft/2+1)
    femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1, 0.5+ kraft/2+1)


#------------Dibujando dev bt------------#
AltAxi=1830
Radial=72
DiamInt=857

aislamiento=2 #indica que es cordex, aislamiento =2 indica papel kraft

if aislamiento == 1:
    # --------DEV SIN AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt/2,(AltVentanaNucleo-AltAxi)/2,DiamInt/2+Radial , (AltVentanaNucleo+AltAxi)/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5)
    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 )
    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 )
    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 )

elif aislamiento == 2:
    kraft=0.46
    #--------DEV CON AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2)
    femm.ei_drawrectangle(DiamInt/2+  kraft/2,(AltVentanaNucleo-AltAxi)/2+  kraft/2,DiamInt/2+Radial-  kraft/2 , (AltVentanaNucleo+AltAxi)/2 -  kraft/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)


#------------Dibujando dev at------------#
AltAxi=1790
Radial=111
DiamInt=1097

aislamiento=2 #indica que es cordex, aislamiento =2 indica papel kraft

if aislamiento == 1:
    # --------DEV SIN AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt/2,(AltVentanaNucleo-AltAxi)/2,DiamInt/2+Radial , (AltVentanaNucleo+AltAxi)/2)
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5)
    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 )
    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 )
    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 )

elif aislamiento == 2:
    kraft=0.46
    # --------DEV CON AISLAMIENTO--------
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2)
    femm.ei_drawrectangle(DiamInt/2+  kraft/2,(AltVentanaNucleo-AltAxi)/2+  kraft/2,DiamInt/2+Radial-  kraft/2 , (AltVentanaNucleo+AltAxi)/2 -  kraft/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo-AltAxi)/2+  kraft/2, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2+Radial, (AltVentanaNucleo + AltAxi) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt/2+Radial+  kraft/2, (AltVentanaNucleo + AltAxi) / 2+  kraft/2, 0.5)


#------------Dibujando devs reg------------#
#nota: Para el dev de regulacion se necesita un dato extra que es su distancia entre la parte sup e inf, al cual llamaeremos separacion

separacion=660

AltAxi=1290
Radial=27
DiamInt=1411


if aislamiento == 1:
    # --------DEV SIN AISLAMIENTO--------
    #sup
    femm.ei_drawrectangle(DiamInt/2,(AltVentanaNucleo-AltAxi)/2,DiamInt/2+Radial , (AltVentanaNucleo-separacion)/2)
    #inf
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2, DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2)
elif aislamiento == 2:
    kraft=1.220
    # --------DEV CON AISLAMIENTO--------
    #================dev sup================
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2)
    femm.ei_drawrectangle(DiamInt / 2 +kraft/2, (AltVentanaNucleo + separacion) / 2+kraft/2, DiamInt / 2 + Radial-kraft/2,(AltVentanaNucleo + AltAxi) / 2-kraft/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo + separacion) / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2, 0.5+ kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial , (AltVentanaNucleo + separacion) / 2 , 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo + AltAxi) / 2, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2+ Radial , (AltVentanaNucleo + AltAxi) / 2, 0.5)

    # ==============dev inf==================
    femm.ei_drawrectangle(DiamInt / 2 +kraft/2, (AltVentanaNucleo - AltAxi) / 2+kraft/2, DiamInt / 2 + Radial-kraft/2, (AltVentanaNucleo - separacion) / 2-kraft/2)
    femm.ei_drawrectangle(DiamInt/2,(AltVentanaNucleo-AltAxi)/2,DiamInt/2+Radial , (AltVentanaNucleo-separacion)/2)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2, 0.5)
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo - AltAxi) / 2, 0.5 + kraft / 2)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2, 0.5+ kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial , (AltVentanaNucleo - AltAxi) / 2 , 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo-separacion)/2 + kraft / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo-separacion)/2, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo-separacion)/2 + kraft / 2, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo-separacion)/2, 0.5)

# ====================== DIBUJANDO CILINDROS ======================

#------------- Cilindros entre Pierna y Terciario
    #c1
altaxicil=1860
radialCil=3
DimInt=735 #este parámetro lo calcula el usuario

DistToCil=DimInt/2+12

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

#------------- Cilindros entre Terciario y Baja T
    #c2
altaxicil=1830
radialCil=2
DimInt=807 + (6*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c3
altaxicil=1830
radialCil=3
DimInt=807 + (6*2 + 2*2 + 8*2)  #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)


#------------- Cilindros entre Baja T y Alta T
    #c4
altaxicil=1830
radialCil=2
DimInt=1001 + (6*2)  #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c5
altaxicil=1830
radialCil=1
DimInt=1001 + (6*2+ 2*2 + 8*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c6
altaxicil=1830
radialCil=1
DimInt=1001 + (6*2+ 2*2 + 8*2 + 1*2 +9*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c7
altaxicil=1830
radialCil=3
DimInt=1001 + (6*2+ 2*2 + 8*2 + 1*2 +9*2 +1*2 +10*2)  #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

#------------- Cilindros entre Alta T y Reg
    #c8
altaxicil=1830
radialCil=2
DimInt=1319 + (6*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c9
altaxicil=1830
radialCil=2
DimInt=1319 + (6*2+ 2*2 +6*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c10
altaxicil=1830
radialCil=2
DimInt=1319 + (6*2 + 2*2 + 6*2 + 2*2 + 8*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

    #c11
altaxicil=1830
radialCil=4
DimInt=1319 + (6*2 + 2*2 + 6*2 + 2*2 + 8*2 + 2*2 +8*2) #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)

#------------- Cilindros entre RegF1 y RegF2
    #c12
altaxicil=1830
radialCil=2
DimInt=1465 + 6*2  #este parámetro lo calcula el usuario

DistToCil=DimInt/2

femm.ei_drawrectangle(DistToCil,(AltVentanaNucleo-altaxicil)/2,DistToCil+radialCil , (AltVentanaNucleo+altaxicil)/2)









input("Simulación terminada. Presiona Enter para salir...")




