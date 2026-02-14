import femm
import math

from  AislamientosGeo  import drawanilloangular
from  AislamientosGeo  import drawminiangulo
from  windingmaterials import nomesh
from  Boundaries import defboundary
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def drawdevbase(boundary_name,voltage,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy):
#Devanado base sin miniangulos, anillo angular, etc.

 if kraft == 0:
     femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, DiamInt / 2 + Radial,
                           (AltVentanaNucleo + AltAxi) / 2 + dy)

     #no mallar devanado
     nomesh((DiamInt / 2 + Radial/2),AltVentanaNucleo/2)

     # Definiendo boundaries
     x1=(DiamInt / 2 + Radial/2)
     y1=(AltVentanaNucleo + AltAxi) / 2+dy

     x2=(DiamInt / 2 + Radial)
     y2=AltVentanaNucleo/2+dy

     x3=(DiamInt / 2 + Radial/2)
     y3=(AltVentanaNucleo - AltAxi)/2+dy

     x4=DiamInt / 2
     y4=AltVentanaNucleo/2+dy

     segment_points = [
         (x1, y1),
         (x2, y2),
         (x3, y3),
         (x4, y4)
     ]

     defboundary(boundary_name, voltage, segment_points,50)

     # -------- CREANDO LOS CORNERS CON LAS BOUNDARIES ASIGNADAS--------
     # crea corner inf izq
     femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
     # crea corner sup izq
     femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)

     # crea corner inf derec
     femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
     # crea corner sup derech
     femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)


 else:
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + dy)

    femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy,DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy)

    # no mallar devanado
    nomesh((DiamInt / 2 + Radial / 2), AltVentanaNucleo / 2)

    # Definiendo boundaries
    x1 = (DiamInt / 2 + Radial / 2)
    y1 = (AltVentanaNucleo + AltAxi) / 2 + dy-0.5

    x2 = (DiamInt / 2 + Radial)-0.5
    y2 = AltVentanaNucleo / 2 + dy

    x3 = (DiamInt / 2 + Radial / 2)
    y3 = (AltVentanaNucleo - AltAxi) / 2 + dy+0.5

    x4 = DiamInt / 2+0.5
    y4 = AltVentanaNucleo / 2 + dy

    segment_points = [
        (x1, y1),
        (x2, y2),
        (x3, y3),
        (x4, y4)
    ]

    defboundary(boundary_name, voltage, segment_points,50)

    # -------- CREANDO LOS CORNERS CON LAS BOUNDARIES ASIGNADAS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # crea corner sup izq
    #femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    #femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2 + dy, 0.5)
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 - kraft / 2 + dy, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # no mallar devanado
    nomesh((DiamInt / 2 + Radial / 2), AltVentanaNucleo / 2)


#-------------------------------------------------------------------------------------------------------------------------------------

def drawdevanado(boundary_name,voltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy):
    # Devanado con miniangulos, anillo angular, etc.

    ax = round(axial_cond - 1)
    if kraft==0:
        # --------DEV SIN AISLAMIENTO DE PAPEL--------
        drawdevbase(boundary_name,voltage,AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, dy)
        if (Radial + 2 * ax) < 78:
        # --------DEV CON ANILLO ANGULAR--------
            drawanilloangular(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)
        elif (Radial + 2 * ax) > 78:
        # --------DEV CON ANILLO MINIANGULO-------
            drawminiangulo(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)

    else:
        # --------DEV CON AISLAMIENTO DE PAPEL--------
        drawdevbase(boundary_name,voltage,AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, dy)
        if (Radial + 2 * ax) < 78:
        # --------DEV CON ANILLO ANGULAR--------
            drawanilloangular(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)
        elif (Radial + 2 * ax) > 78:
        # --------DEV CON ANILLO MINIANGULO-------
            drawminiangulo(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

def drawdevanadoRegGap(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy,separacion):
    ax = round(axial_cond - 1)

    if kraft == 0:
        # --------DEV SIN AISLAMIENTO DE PAPEL--------
        # --------DEV SIN AISLAMIENTO--------

        # ================dev sup================
        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2+dy, DiamInt / 2 + Radial,
                              (AltVentanaNucleo + AltAxi) / 2+dy)

        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + separacion) / 2+dy, 0.5)
        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + separacion+dy) / 2, 0.5)
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2+dy, 0.5)
        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2+dy, 0.5)

        # ==============dev inf==================
        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2+dy, DiamInt / 2 + Radial,
                              (AltVentanaNucleo - separacion) / 2+dy)
        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2+dy, 0.5)
        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2+dy, 0.5)
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - separacion) / 2+dy, 0.5)
        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2+dy, 0.5)

        # --------ANILLO ANGULAR SUP- REG SUP--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5 + 1)
        # --------ANILLO ANGULAR INF- REG SUP--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + 1 + ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + separacion) / 2 + 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + 1 + ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + separacion) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 - 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + separacion) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1+dy,
                         DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1+dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo + separacion) / 2 + ax + 1+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2+dy, 0.5 + 1)

        # --------ANILLO ANGULAR SUP- REG INF--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        # --------ANILLO ANGULAR INF- REG INF--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - separacion) / 2 - 1 - ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - separacion) / 2 - 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 - 1 - ax+dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - separacion) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + 1+dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - separacion) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1+dy,
                         DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1+dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo - separacion) / 2 - ax - 1+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2+dy, 0.5 + 1)


    else:
        # --------DEV CON AISLAMIENTO DE PAPEL--------
        # --------DEV CON AISLAMIENTO--------
        # ================dev sup================
        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2+dy, DiamInt / 2 + Radial,
                              (AltVentanaNucleo + AltAxi) / 2+dy)
        femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2+dy,
                              DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2+dy)

        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + separacion) / 2+dy, 0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2+dy, 0.5)

        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2+dy,
                             0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + separacion) / 2+dy, 0.5)

        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2+dy, 0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2+dy, 0.5)

        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2+dy,
                             0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2+dy, 0.5)

        # ==============dev inf==================
        femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2+dy,
                              DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo - separacion) / 2 - kraft / 2+dy)
        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2+dy, DiamInt / 2 + Radial,
                              (AltVentanaNucleo - separacion) / 2+dy)

        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2+dy, 0.5)
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2+dy, 0.5 + kraft / 2)

        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2+dy,
                             0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2+dy, 0.5)

        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - separacion) / 2 + kraft / 2+dy, 0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - separacion) / 2+dy, 0.5)

        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo - separacion) / 2 + kraft / 2+dy,
                             0.5 + kraft / 2)
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2+dy, 0.5)

        # --------ANILLO ANGULAR SUP- REG SUP--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)
        # --------ANILLO ANGULAR INF- REG SUP--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy,
                         DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + 1)

        # --------ANILLO ANGULAR SUP- REG INF--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1)
        # --------ANILLO ANGULAR INF- REG INF--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,
                         (AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,
                         (AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy,
                         DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy, DiamInt / 2 + Radial,
                         (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1)
