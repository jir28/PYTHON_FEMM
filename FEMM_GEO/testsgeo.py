import femm
from  DevanadosGeo import drawdevanado
from  CoreGeo import drawcore
from  windingmaterials import materials

femm.openfemm()
femm.newdocument(1)  # electrostatics
femm.ei_probdef("millimeters", "axi", 1e-8, 0, -30)
materials()



def drawsectoranillo_sup(Dimint,AltAxi,AltVentanaNucleo,Radial,h,dy):
    # Línea vertical izquierda

    xi=Dimint/2+Radial-5

    yi=(AltVentanaNucleo + AltAxi) / 2 + dy+h

    femm.ei_drawline(xi, yi, xi, yi+3)
    femm.ei_drawline(xi, yi+3, xi-Radial-4.7-3, yi+3)
    femm.ei_drawline( xi-Radial-4.7-3, yi+3, xi-Radial-4.7-3, yi-110)
    femm.ei_drawline(xi - Radial  - 4.7 - 3, yi - 110, xi - Radial  - 4.7 , yi - 110)
    femm.ei_drawline(xi - Radial  - 4.7 , yi - 110 , xi - Radial  - 4.7 , yi )
    femm.ei_drawline(xi - Radial  - 4.7 , yi  , xi  , yi )

    # Redondear esquinas
    femm.ei_createradius(xi - Radial  - 4.7, yi, 10)
    femm.ei_createradius(xi - Radial  - 4.7-3, yi+3, 13)
    return h



def drawsectoranillo_inf(Dimint,AltAxi,AltVentanaNucleo,Radial,h,dy):
    # Línea vertical izquierda

    xi=Dimint/2+Radial-5

    yi=(AltVentanaNucleo-AltAxi)/2-h+dy

    femm.ei_drawline(xi, yi, xi, yi-3)
    femm.ei_drawline( xi, yi - 3, xi- Radial  - 4.7 , yi-3)
    femm.ei_drawline( xi - Radial - 4.7, yi - 3, xi- Radial - 4.7 , yi+110)
    femm.ei_drawline(xi - Radial - 4.7, yi + 110 , xi - Radial - 4.7+3, yi+110)
    femm.ei_drawline( xi - Radial - 4.7+3, yi+110,xi - Radial - 4.7+3, yi )
    femm.ei_drawline( xi - Radial - 4.7+3, yi, xi , yi )
    # Redondear esquinas
    femm.ei_createradius(xi - Radial - 4.7 + 3, yi, 10)
    femm.ei_createradius(  xi- Radial  - 4.7 , yi-3, 13)


    return h


def drawsectorcapa_sup(Dimint,AltAxi,AltVentanaNucleo,Radial,h2,dy):
    # Línea vertical izquierda

    xi=Dimint/2

    yi=(AltVentanaNucleo + AltAxi)/2+h2+dy

    femm.ei_drawline(xi, yi, xi, yi+3)
    femm.ei_drawline(xi, yi+3, xi+Radial+4.7+3, yi+3)
    femm.ei_drawline(xi+Radial+4.7+3, yi+3,xi+Radial+4.7+3, yi-110)
    femm.ei_drawline(xi+Radial+4.7+3, yi-110, xi+Radial+4.7, yi-110)
    femm.ei_drawline( xi+Radial+4.7, yi-110, xi+Radial+4.7, yi)
    femm.ei_drawline( xi + Radial + 4.7, yi, xi, yi)

    # Redondear esquinas
    femm.ei_createradius(xi+Radial+4.7, yi, 10)
    femm.ei_createradius(xi+Radial+4.7+3, yi, 13)
    return h2

def drawsectorcapa_inf(Dimint,AltAxi,AltVentanaNucleo,Radial,h2,dy):
    # Línea vertical derecha

    xi = Dimint/2
    yi = (AltVentanaNucleo - AltAxi)/2 - h2 + dy

    femm.ei_drawline(xi, yi, xi, yi-3)
    femm.ei_drawline(xi, yi-3, xi+Radial+4.7+3, yi-3)
    femm.ei_drawline(xi+Radial+4.7+3, yi-3, xi+Radial+4.7+3, yi+110)
    femm.ei_drawline(xi+Radial+4.7+3, yi+110, xi+Radial+4.7, yi+110)
    femm.ei_drawline(xi+Radial+4.7, yi+110, xi+Radial+4.7, yi)
    femm.ei_drawline(xi+Radial+4.7, yi, xi, yi)

    # Redondear esquinas
    femm.ei_createradius(xi+Radial+4.7, yi, 10)
    femm.ei_createradius(xi+Radial+4.7+3, yi-3, 13)

    return h2

def drawanillo_eqsup(AltAxi,Dimint,radiosint,h,hanillo_eq,dy):

    x1=Dimint/2+2
    y1=AltAxi+h+2+dy
    x2=Dimint/2+Radial
    y2=AltAxi+h+2+hanillo_eq+dy


    femm.ei_drawrectangle(x1, y1, x2,y2)
    femm.ei_createradius(x1, y1, radiosint[0])
    femm.ei_createradius(x2, y1, radiosint[1])
    femm.ei_createradius(x1, y2, radiosint[2])
    femm.ei_createradius(x2, y2, radiosint[2])


    x1=Dimint/2
    y1=AltAxi+h+dy
    x2=Dimint/2+Radial+2
    y2=AltAxi+h+2+hanillo_eq+2+dy


    femm.ei_drawrectangle(x1, y1, x2,y2)
    femm.ei_createradius(x1, y1, radiosint[0]+2)
    femm.ei_createradius(x2, y1, radiosint[1]+2)
    femm.ei_createradius(x1, y2, radiosint[2]+2)
    femm.ei_createradius(x2, y2, radiosint[2]+2)

    l=h+4+hanillo_eq
    return l


def drawanillo_eqinf(AltAxi, AltVentanaNucleo, Dimint, radiosint,h,hanillo_eq, dy):
    # Primer rectángulo inferior
    x1 = Dimint/2 + 2
    y1 = (AltVentanaNucleo - AltAxi)/2 - h - 2 - dy
    x2 = Dimint/2 + Radial
    y2 = (AltVentanaNucleo - AltAxi)/2 - h - 2 - hanillo_eq - dy

    femm.ei_drawrectangle(x1, y1, x2, y2)
    femm.ei_createradius(x1, y1, radiosint[0])
    femm.ei_createradius(x2, y1, radiosint[1])
    femm.ei_createradius(x1, y2, radiosint[2])
    femm.ei_createradius(x2, y2, radiosint[2])

    # Segundo rectángulo inferior (con margen extra)
    x1 = Dimint/2
    y1 = (AltVentanaNucleo - AltAxi)/2 - h - dy
    x2 = Dimint/2 + Radial + 2
    y2 = (AltVentanaNucleo - AltAxi)/2 - h - 2 - hanillo_eq - 2 - dy

    femm.ei_drawrectangle(x1, y1, x2, y2)
    femm.ei_createradius(x1, y1, radiosint[0] + 2)
    femm.ei_createradius(x2, y1, radiosint[1] + 2)
    femm.ei_createradius(x1, y2, radiosint[2] + 2)
    femm.ei_createradius(x2, y2, radiosint[2] + 2)

    l = h + 4 + hanillo_eq
    return l

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



#config 1 capa - 1 sector anillo
Radial=58
Dimint=974

AltAxi=1770
h=8+5 #(tacon+cabecera)

# Llamada a la función
h=drawsectoranillo_sup(Dimint,AltAxi,AltVentanaNucleo,Radial,h,dy)
h=drawsectoranillo_inf(Dimint,AltAxi,AltVentanaNucleo,Radial,h,dy)

h1=h+10
drawsectorcapa_inf(Dimint,AltAxi,AltVentanaNucleo,Radial,h1,dy)
drawsectorcapa_sup(Dimint,AltAxi,AltVentanaNucleo,Radial,h1,dy)


femm.ei_zoomnatural()


input("Sectores dibujados. Presiona Enter para salir...")
