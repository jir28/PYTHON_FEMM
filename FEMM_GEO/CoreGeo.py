import femm
from  windingmaterials import asignmaterials
from  Boundaries import defboundary

def drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo, AlturasAxiDev, CabecerasDevSup, CabecerasDevinf):



    for i in range(len(AlturasAxiDev)):
        if (AlturasAxiDev[i] + CabecerasDevSup[i] + CabecerasDevinf[i]) == AltVentanaNucleo:
            CabSup = CabecerasDevSup[i]
            Cabinf = CabecerasDevinf[i]
            print("CabSupAT:", CabSup)
            print("CabinfAT:", Cabinf)

            break  # terminamos el bucle al encontrar la primera coincidencia
    else:
        # Si no se encontró ningún valor que cumpla la condición
        print("ERROR: revisar longitudes de cabecera o axiales de bobina, el núcleo no se dimensionó correctamente")
        # Valores propuesto provisionales mientras el usuario corrije
        CabSup = 5000
        Cabinf = 5000




    # Calcular desplazamiento vertical del centro de la ventana
    dy = +abs(
        AltVentanaNucleo/2 - CabSup - (AltVentanaNucleo - CabSup - Cabinf)/2
    )
    # Dibujar el rectángulo de la ventana del núcleo
    femm.ei_drawrectangle(DiametroNucleo / 2, dy, AnchVentanaNucleo * 1.5, AltVentanaNucleo+dy)


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


