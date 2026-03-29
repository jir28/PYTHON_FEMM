

import femm

def defboundary(boundary_name, voltage, segment_points, GRUPO_FRONTERA):

    # Intentar borrar si ya existe (no falla si no existe)
    try:
        femm.ei_deleteboundprop(boundary_name)
    except:
        pass

    # Crear de nuevo con el voltaje actualizado
    femm.ei_addboundprop(boundary_name, voltage, 0, 0, 0, "0")

    # Asignar a segmentos
    for (x, y) in segment_points:
        femm.ei_selectsegment(x, y)
        femm.ei_setsegmentprop(boundary_name, 0, 1, 0, GRUPO_FRONTERA, "0")
        femm.ei_clearselected()
