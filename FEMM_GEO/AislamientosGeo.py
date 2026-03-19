import math

import femm


from  windingmaterials import asignmaterials
from globals_array import obtener_taconb_d
#-----------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def drawminiangulo(AltVentanaNucleo,AltAxi, Radial, DiamInt, axial_cond,kraft,dy):
    l_recomp = Radial - 19 * 2 - 4
    ax = round(axial_cond - 1)

    if kraft==0:

        # --------MINI ANGULOS SUPERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        # corners
        # crea corner sup izq

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)

        # --------MINI ANGULOS INFERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 + dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)

        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)

        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1)

        #asignar material
        #-compensador superior
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy + 0.5, 1,3)
        #-compensador inferior
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo - AltAxi) / 2 + dy - 0.5, 1,3)
        # -miniangulos inf
        asignmaterials('Weidmann',(DiamInt/2-0.5), (AltVentanaNucleo - AltAxi) / 2 + dy + ax/2, 1,3)
        asignmaterials('Weidmann',(DiamInt/2+Radial+0.5), (AltVentanaNucleo - AltAxi) / 2 + dy+ ax/2 , 1,3)
        # -miniangulos sup
        asignmaterials('Weidmann', (DiamInt / 2 - 0.5), (AltVentanaNucleo + AltAxi) / 2 + dy - ax / 2, 1, 3)
        asignmaterials('Weidmann', (DiamInt / 2 + Radial + 0.5), (AltVentanaNucleo + AltAxi) / 2 + dy - ax / 2, 1, 3)

    else:
        l_recomp = Radial - 19 * 2 - 4

        # --------MINI ANGULOS SUPERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2+ dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy, 0.5 + 1 + kraft / 2)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy, 0.5 + 1 + kraft / 2)

        # --------MINI ANGULOS INFERIORES-------

        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2+ dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)

        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy, 0.5 + 1 + kraft / 2)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)

        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy, 0.5 + 1 + kraft / 2)


        # Asignar material
        # asignar material
        # -compensador superior
        asignmaterials('Weidmann', (DiamInt / 2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy + 0.5, 1, 3)
        # -compensador inferior
        asignmaterials('Weidmann', (DiamInt / 2 + Radial / 2), (AltVentanaNucleo - AltAxi) / 2 + dy - 0.5, 1, 3)
        # -miniangulos inf
        asignmaterials('Weidmann', (DiamInt / 2 - 0.5), (AltVentanaNucleo - AltAxi) / 2 + dy + ax / 2, 1, 3)
        asignmaterials('Weidmann', (DiamInt / 2 + Radial + 0.5), (AltVentanaNucleo - AltAxi) / 2 + dy + ax / 2, 1, 3)
        # -miniangulos sup
        asignmaterials('Weidmann', (DiamInt / 2 - 0.5), (AltVentanaNucleo + AltAxi) / 2 + dy - ax / 2, 1, 3)
        asignmaterials('Weidmann', (DiamInt / 2 + Radial + 0.5), (AltVentanaNucleo + AltAxi) / 2 + dy - ax / 2, 1, 3)
        asignmaterials('kraftsolid', (DiamInt / 2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy - kraft/4, kraft/2,2)


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def drawanilloangular(AltVentanaNucleo,AltAxi, Radial, DiamInt, axial_cond,kraft,dy):
    ax = round(axial_cond - 1)
    if kraft== 0:
        #--------ANILLO ANGULAR SUPERIOR-----------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5  + 1)
        # --------ANILLO ANGULAR INFERIOR-----------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 -1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        # Asignar material
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy + 0.5, 1,3)
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo - AltAxi) / 2 + dy - 0.5, 1,3)

    else:

        # --------ANILLO ANGULAR SUPERIOR--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5+ kraft/2+1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5+ kraft/2+1)

        # --------ANILLO ANGULAR INFERIOR--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5+ kraft/2+1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5+ kraft/2+1)

        # Asignar material
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy + 0.5, 1,3)
        asignmaterials('Weidmann',(DiamInt/2 + Radial / 2), (AltVentanaNucleo - AltAxi) / 2 + dy - 0.5, 1,3)
        asignmaterials('kraftsolid', (DiamInt / 2 + Radial / 2), (AltVentanaNucleo + AltAxi) / 2 + dy - kraft/4, kraft/2,2)

#-------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------
def drawcilindro(DimInt , AltVentanaNucleo, radialCil, dy, desy1,desy2,AlturasAxiDev):
        AltmaxAxiDev = max(AlturasAxiDev)
        #pos_max = AlturasAxiDev.index(AltmaxAxiDev)
        altaxicil = AltmaxAxiDev

        DistToCil = DimInt / 2
        x1=DistToCil
        y1=(AltVentanaNucleo - altaxicil) / 2 + dy+desy1
        x2=DistToCil + radialCil
        y2=(AltVentanaNucleo + altaxicil) / 2 + dy+desy2

        femm.ei_drawrectangle(x1, y1, x2,y2)
        # Asignar material
        asignmaterials('TIV', DistToCil+radialCil/2, altaxicil/2+ dy , 2, 3)

   # Definir el arreglo fuera de la función
acumulados = []

def drawpackcil(DimInt_inicial,AltVentanaNucleo, radiales,ductos,dy,CabecerasDevinf,CabecerasDevsup,AlturasAxiDev,alturascil_recortesup,alturascil_recorteinf):
        AltmaxAxiDev = max(AlturasAxiDev)
        pos_max = AlturasAxiDev.index(AltmaxAxiDev)
        taconbd=max(obtener_taconb_d())

        DimInt_actual = DimInt_inicial
        n_cil = len(radiales)
        if not acumulados:
            # La lista está vacía, indica que no se tiene ningun cilindro previo, por lo que es el que está pegado al core
            print("acumulados está vacío, inicializando...")

            desy1 = -CabecerasDevinf[1]
            desy2 = CabecerasDevsup[pos_max] - taconbd - round(0.01 * AltVentanaNucleo) - 3


        else:
            # La lista NO está vacía
            desy1 = -CabecerasDevinf[1] + taconbd + 3
            desy2 = CabecerasDevsup[pos_max] - taconbd - round(0.01 * AltVentanaNucleo) - 3

            print("acumulados ya tiene datos, seguimos acumulando...")
            # Por ejemplo, podrías tomar el último valor como punto de partida

        for i in range(n_cil):
            # Sumar ducto antes del cilindro
            if n_cil == 1:
                DimInt_actual += 2 * ductos[0]
            else:
                DimInt_actual += 2 * ductos[i]

            # Guardar diámetro después del ducto
            acumulados.append(DimInt_actual)
            radialCil = radiales[i]

            #Codigo para recorte de alturas sup e inf en caso de necesitarse
            # Supongamos que alturascil_recortesup[i] y alturascil_recorteinf[i]
            # pueden ser 0 (sin recorte) o un valor distinto (con recorte)

            sup = alturascil_recortesup[i]
            inf = alturascil_recorteinf[i]

            match (sup == 0, inf == 0):
                case (True, True):
                    # Sin recortes
                    drawcilindro(DimInt_actual, AltVentanaNucleo, radialCil, dy, desy1, desy2, AlturasAxiDev)

                case (False, True):
                    # Solo recorte superior
                    desy2 =  desy2-sup
                    drawcilindro(DimInt_actual, AltVentanaNucleo, radialCil, dy, desy1, desy2, AlturasAxiDev)

                case (True, False):
                    # Solo recorte inferior
                    desy1 =  desy1+inf
                    drawcilindro(DimInt_actual, AltVentanaNucleo, radialCil, dy, desy1, desy2, AlturasAxiDev)

                case (False, False):
                    # Ambos recortes
                    desy2 = desy2-sup
                    desy1 = desy1+inf
                    drawcilindro(DimInt_actual, AltVentanaNucleo, radialCil, dy, desy1, desy2, AlturasAxiDev)

            # Preparar diámetro para el siguiente cilindro
            DimInt_actual += 2 * radialCil

            # Guardar diámetro después del cilindro
            acumulados.append(DimInt_actual)

            # Ver todos los acumulados
            # print(acumulados)

