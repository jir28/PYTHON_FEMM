import femm


from  windingmaterials import asignmaterials
from  Boundaries import defboundary

def drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo,  CabSupAT, CabInfAT):

    # Calcular desplazamiento vertical del centro de la ventana
    dy = -abs(
        AltVentanaNucleo/2 - CabSupAT - (AltVentanaNucleo - CabSupAT - CabInfAT)/2
    )
    # Dibujar el rectángulo de la ventana del núcleo
    femm.ei_drawrectangle(DiametroNucleo / 2, 0, AnchVentanaNucleo * 3, AltVentanaNucleo)


    # Definiendo boundaries
    x1 = DiametroNucleo / 2 + AnchVentanaNucleo / 2
    y1 = AltVentanaNucleo

    x2 = DiametroNucleo / 2 +AnchVentanaNucleo
    y2 = AltVentanaNucleo / 2

    x3 = DiametroNucleo / 2 + AnchVentanaNucleo / 2
    y3 = 0

    x4 = DiametroNucleo/2
    y4 = AltVentanaNucleo / 2

    segment_points = [
        (x1, y1),
        (x2, y2),
        (x3, y3),
        (x4, y4)
    ]
    voltage=0
    defboundary("core", voltage, segment_points,100)



    # asignar material
    asignmaterials('OilM', DiametroNucleo/2+AnchVentanaNucleo / 4, (AltVentanaNucleo)-20, 10, 0)

    return dy


def draw_arandela_sup_inf(AltVentanaNucleo,altaxidev,radialesdev,dimintdev,cabsupdev,cabinfdev,espsup,espinf,dy):
    maxpos = len(altaxidev)-1
    print("maxpos:",maxpos)
    #arandela sup
    x1=dimintdev[0]/2
    y1=cabsupdev[0]+(altaxidev[0]+AltVentanaNucleo)/2-espsup+dy
    x2=dimintdev[maxpos]/2+radialesdev[maxpos]
    y2=cabsupdev[0]+(altaxidev[0]+AltVentanaNucleo)/2+dy

    femm.ei_drawrectangle(x1, y1, x2, y2)

    #arandela inf
    x1 = dimintdev[0]/2
    y1 =  (AltVentanaNucleo-altaxidev[0])/2-cabinfdev[0]+dy
    x2 = dimintdev[maxpos]/2 +radialesdev[maxpos]
    y2 = (AltVentanaNucleo-altaxidev[0])/2-cabinfdev[0]+dy+espinf

    femm.ei_drawrectangle(x1, y1, x2, y2)

