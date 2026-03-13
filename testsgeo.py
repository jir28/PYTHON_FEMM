import femm

femm.openfemm()
femm.newdocument(1)  # electrostatics
femm.ei_probdef("millimeters", "axi", 1e-8, 0, -30)


#config 1 capa - 1 sector anillo
Radial=60
Dimint=100

AltAxi=1000
h=8+5 #(tacon+cabecera)

def drawsectoranillo(Dimint,AltAxi,Radial,h):
    # Línea vertical izquierda

    xi=Dimint/2+Radial-15

    yi=AltAxi+h

    femm.ei_drawline(xi, yi, xi, yi+3)
    femm.ei_drawline(xi, yi+3, xi-Radial-15-4.7-3, yi+3)
    femm.ei_drawline( xi-Radial-15-4.7-3, yi+3, xi-Radial-15-4.7-3, yi-110)
    femm.ei_drawline(xi - Radial - 15 - 4.7 - 3, yi - 110, xi - Radial - 15 - 4.7 , yi - 110)
    femm.ei_drawline(xi - Radial - 15 - 4.7 , yi - 110 , xi - Radial - 15 - 4.7 , yi )
    femm.ei_drawline(xi - Radial - 15 - 4.7 , yi  , xi  , yi )

    # Redondear esquinas
    femm.ei_createradius(xi - Radial - 15 - 4.7, yi, 10)
    femm.ei_createradius(xi - Radial - 15 - 4.7-3, yi+3, 13)
    return h

# Llamada a la función
h=drawsectoranillo(Dimint,AltAxi,Radial,h)


    # Ajustar vista
femm.ei_zoomnatural()

input("Sectores dibujados. Presiona Enter para salir...")
