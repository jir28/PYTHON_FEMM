import femm

femm.openfemm()
femm.newdocument(1)  # electrostatics
femm.ei_probdef("millimeters", "axi", 1e-8, 0, -30)




def drawsectoranillo_sup(Dimint,AltAxi,Radial,h,dy):
    # Línea vertical izquierda

    xi=Dimint/2+Radial-5

    yi=AltAxi+h+dy

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


def drawsectorcapa_sup(Dimint,AltAxi,Radial,h2,dy):
    # Línea vertical izquierda

    xi=Dimint/2

    yi=AltAxi+h2+dy

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



dy=10
AltVentanaNucleo=2000


#config 1 capa - 1 sector anillo
Radial=60
Dimint=100

AltAxi=1000
h=8+5 #(tacon+cabecera)

# Llamada a la función
h=drawsectoranillo_sup(Dimint,AltAxi,Radial,h,dy)
drawsectoranillo_inf(Dimint,AltAxi,AltVentanaNucleo,Radial,h,dy)



#config 1 capa - 1 sector capa
Radial=60
Dimint=100

AltAxi=1000
h2=60 #(tacon+cabecera)

# Llamada a la función
h2=drawsectorcapa_sup(Dimint,AltAxi,Radial,h2,dy)

h2 = drawsectorcapa_inf(Dimint, AltAxi, AltVentanaNucleo, Radial, h2, dy)

    # Ajustar vista
femm.ei_zoomnatural()

input("Sectores dibujados. Presiona Enter para salir...")
