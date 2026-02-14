import femm
from  windingmaterials import asignmaterials
from  Boundaries import defboundary

def drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, CabSupAT, CabinfAT):
    # Dibujar el rectángulo de la ventana del núcleo
    femm.ei_drawrectangle(DiametroNucleo/2, 0, AnchVentanaNucleo, AltVentanaNucleo)


    # Calcular desplazamiento vertical del centro de la ventana
    dy = -abs(
        AltVentanaNucleo/2 - CabSupAT - (AltVentanaNucleo - CabSupAT - CabinfAT)/2
    )

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
    asignmaterials('OilM', (AnchVentanaNucleo/2), (AltVentanaNucleo)-20, 10, 0)

    return dy
