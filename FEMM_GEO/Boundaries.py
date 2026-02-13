

import femm


def defboundary(boundary_name, voltage, segment_points):
    """
    Asigna un boundary a varios segmentos en FEMM (electrostática)

    boundary_name: str, nombre de la boundary
    voltage: float, potencial en V
    segment_points: lista de tuplas [(x1,y1), (x2,y2), ...]
                    con un punto sobre cada segmento
    """
    # Crear boundary

    # femm.ei_setsegmentprop(boundary_name, element_size, automesh, hide,GRUPO_FRONTERA )
    femm.ei_addboundprop(boundary_name, voltage, 0, 0, 0, "1")

    # Número de grupo para seleccionar todos los segmentos juntos
    GRUPO_FRONTERA = 1

    # Recorrer todos los puntos y asignar boundary
    for (x, y) in segment_points:
        femm.ei_selectsegment(x, y)
        femm.ei_setsegmentprop(boundary_name, 0, 1, 0, GRUPO_FRONTERA, "0")
        femm.ei_clearselected()
