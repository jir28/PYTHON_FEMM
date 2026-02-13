import femm
from  windingmaterials import asignmaterials


def drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, CabSupAT, CabinfAT):
    # Dibujar el rectángulo de la ventana del núcleo
    femm.ei_drawrectangle(DiametroNucleo/2, 0, AnchVentanaNucleo, AltVentanaNucleo)

    # Calcular desplazamiento vertical del centro de la ventana
    dy = -abs(
        AltVentanaNucleo/2 - CabSupAT - (AltVentanaNucleo - CabSupAT - CabinfAT)/2
    )
    # asignar material
    asignmaterials('OilM', (AnchVentanaNucleo/2), (AltVentanaNucleo)-20, 10, 0)

    return dy
