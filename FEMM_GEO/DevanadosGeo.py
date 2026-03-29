import femm
import math

from  AislamientosGeo  import drawanilloangular
from  AislamientosGeo  import drawminiangulo
from  windingmaterials import asignmaterials,nomesh
from  Boundaries import defboundary

from globals_array import agregar_altura, agregar_cabecerassup, agregar_cabecerasInf, agregar_taconb_d, agregar_radiales,agregar_dimint


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



def drawdevbase(boundary_name,voltage,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy):
 agregar_altura(AltAxi)
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
    y1 = (AltVentanaNucleo + AltAxi) / 2 + dy-kraft/2

    x2 = (DiamInt / 2 + Radial)-kraft/2
    y2 = AltVentanaNucleo / 2 + dy

    x3 = (DiamInt / 2 + Radial / 2)
    y3 = (AltVentanaNucleo - AltAxi) / 2 + dy+kraft/2

    x4 = DiamInt / 2+kraft/2
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
    femm.ei_createradius(DiamInt / 2 , (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2  + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy, 0.5)

    # no mallar devanado
    nomesh((DiamInt / 2 + Radial / 2), AltVentanaNucleo / 2)



#-------------------------------------------------------------------------------------------------------------------------------------

def drawdevanado(boundary_name,voltage,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,
                 NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy):
    # crear lista solo la primera vez
    agregar_cabecerassup(cabsup)
    agregar_cabecerasInf(cabinf)
    agregar_radiales(Radial)
    agregar_dimint(DiamInt)

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

    tbd=calctaconB_D(DiamInt,Radial,NumTiras,AnchoEspaciador,EsptiraInt,EsptiraExt)
    agregar_taconb_d(tbd)
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------

def calctaconB_D(DiamInt,Radial,NumTiras,AnchoEspaciador,EsptiraInt,EsptiraExt):
    pi = math.pi
    Num = ((DiamInt - EsptiraInt) * pi - NumTiras * 19) * EsptiraInt + (
            (DiamInt + 2 * Radial + EsptiraExt) * pi - NumTiras * 19) * EsptiraExt
    Den = (DiamInt + 2 * Radial + EsptiraExt) * pi - NumTiras * (AnchoEspaciador + 10)

    B=round(Num / Den)

    print(B)
    return B



#-------------------------------------------------------------------------------------------------------------------------------------
                                                        #REGULATION GAP CENTRAL- FUNCTIONS
#-------------------------------------------------------------------------------------------------------------------------------------


def drawdevbase_regsup(boundary_name, voltage,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy,separacion):
    if kraft == 0:

        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + dy)

        # Definiendo boundaries
        x1 = (DiamInt / 2 + Radial / 2)
        y1 = (AltVentanaNucleo + AltAxi) / 2 + dy

        x2 = (DiamInt / 2 + Radial)
        y2 = AltVentanaNucleo / 2 + separacion/2 + (AltAxi-separacion)/4+ dy

        x3 = (DiamInt / 2 + Radial / 2)
        y3 = AltVentanaNucleo / 2 + separacion/2 + dy

        x4 = DiamInt / 2
        y4 = AltVentanaNucleo / 2 + separacion/2 + (AltAxi-separacion)/4+ dy

        segment_points = [
            (x1, y1),
            (x2, y2),
            (x3, y3),
            (x4, y4)
        ]

        defboundary(boundary_name, voltage, segment_points, 50)
        # no mallar devanado
        nomesh(x1, y2)


        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + dy, 0.5)
        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + separacion) / 2 + dy, 0.5)
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)
        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)
    else:

        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + dy, DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy)
        femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2 + dy,DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy)

        # Definiendo boundaries
        x1 = (DiamInt / 2 + Radial / 2)
        y1 = (AltVentanaNucleo + AltAxi) / 2 + dy-kraft / 2

        x2 = (DiamInt / 2 + Radial)-kraft / 2
        y2 = AltVentanaNucleo / 2 + separacion / 2 + (AltAxi - separacion) / 4 + dy

        x3 = (DiamInt / 2 + Radial / 2)
        y3 = AltVentanaNucleo / 2 + separacion / 2 + dy + kraft / 2

        x4 = DiamInt / 2+ kraft / 2
        y4 = AltVentanaNucleo / 2 + separacion / 2 + (AltAxi - separacion) / 4 + dy

        segment_points = [
            (x1, y1),
            (x2, y2),
            (x3, y3),
            (x4, y4)
        ]

        defboundary(boundary_name, voltage, segment_points, 50)
        # Asignar material
        asignmaterials('kraftsolid', DiamInt/2+kraft/4, AltVentanaNucleo / 2 + separacion / 2 + (AltAxi - separacion) / 4 + dy , 1, 3)
        # no mallar devanado
        nomesh(x1, y2)

        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2 + dy, 0.5)
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + kraft / 2)

        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + separacion) / 2 + kraft / 2 + dy,0.5 )
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + kraft / 2)

        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy, 0.5 )
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)

        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy, 0.5 )
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5+ kraft / 2)





def drawdevbase_reginf(boundary_name, voltage,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy,separacion):
    if kraft == 0:

        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2 + dy)

        # Definiendo boundaries
        x1 = (DiamInt / 2 + Radial / 2)
        y1 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi-separacion)/2+ dy

        x2 = (DiamInt / 2 + Radial)
        y2 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi-separacion)/4+ dy

        x3 = (DiamInt / 2 + Radial / 2)
        y3 = (AltVentanaNucleo - AltAxi) / 2+ dy

        x4 = DiamInt / 2
        y4 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi-separacion)/4+ dy

        segment_points = [
            (x1, y1),
            (x2, y2),
            (x3, y3),
            (x4, y4)
        ]

        defboundary(boundary_name, voltage, segment_points, 50)
        # no mallar devanado
        nomesh(x1, y2)

        # --------CORNERS--------
        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - separacion) / 2 + dy, 0.5)
        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2 + dy, 0.5)
    else:

        femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2+dy,DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo - separacion) / 2 - kraft / 2+dy)
        femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - separacion) / 2+dy)

        # Definiendo boundaries
        x1 = (DiamInt / 2 + Radial / 2)
        y1 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi - separacion) / 2 + dy-kraft/2

        x2 = (DiamInt / 2 + Radial)-kraft/2
        y2 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi - separacion) / 4 + dy

        x3 = (DiamInt / 2 + Radial / 2)
        y3 = (AltVentanaNucleo - AltAxi) / 2 + dy+kraft/2

        x4 = DiamInt / 2+kraft/2
        y4 = (AltVentanaNucleo - AltAxi) / 2 + (AltAxi - separacion) / 4 + dy

        segment_points = [
            (x1, y1),
            (x2, y2),
            (x3, y3),
            (x4, y4)
        ]

        defboundary(boundary_name, voltage, segment_points, 50)
        # Asignar material
        asignmaterials('kraftsolid', DiamInt/2+kraft/4, (AltVentanaNucleo - AltAxi) / 2 + (AltAxi - separacion) / 4 + dy , 1, 3)
        # no mallar devanado
        nomesh(x1, y2)

        # --------CORNERS--------
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - separacion) / 2 - kraft / 2 +dy, 0.5 )
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - separacion) / 2+dy, 0.5 + kraft / 2 )

        # crea corner sup derech
        femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo - separacion) / 2 - kraft / 2 + dy,0.5 )
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + kraft / 2)

        # crea corner inf izq
        femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy, 0.5)
        femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)


        # crea corner inf derec
        femm.ei_createradius(DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2+dy,0.5 )
        femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2+dy, 0.5+ kraft / 2)





# ----------ANILLOS ANGULARES-REG SUP----------------
def anilloangularsup_regsup(AltVentanaNucleo,AltAxi, Radial,DiamInt,kraft,ax,dy):
    if kraft == 0:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)

        # Asignar material
        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo + AltAxi) / 2 - ax/2 + dy, 1, 3)


    else:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 +kraft/2+ 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 +kraft/2+ 1)

        # Asignar material
        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo + AltAxi) / 2 - ax/2 + dy, 1, 3)



def anilloangularinf_regsup(AltVentanaNucleo,separacion, Radial,DiamInt,kraft,ax,dy):
    if kraft == 0:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + separacion) / 2 + 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy,DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy,DiamInt / 2 + Radial, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 +kraft/2+ 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 +kraft/2+ 1)

        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo + separacion) / 2  + ax/2 + dy, 1, 3)


    else:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + separacion) / 2 + 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy,DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + ax + 1 + dy, DiamInt / 2 + Radial,(AltVentanaNucleo + separacion) / 2 + ax + 1 + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + 1+kraft/2)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + separacion) / 2 + dy, 0.5 + 1+kraft/2)

        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo + separacion) / 2  + ax/2 + dy, 1, 3)


# -----------------ANILLOS ANGULARES-REG INF--------------------

def anilloangularsup_reginf(AltVentanaNucleo,separacion, Radial,DiamInt,kraft,ax,dy):
    if kraft == 0:
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - separacion) / 2 - 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy,DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy,DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1)

        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo - separacion) / 2 - 1 - ax/2 + dy, 1, 3)

    else:
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - separacion) / 2 - 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 - 1 - ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy,DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy,DiamInt / 2 + Radial, (AltVentanaNucleo - separacion) / 2 - ax - 1 + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1+kraft/2)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - separacion) / 2 + dy, 0.5 + 1+kraft/2)
        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo - separacion) / 2 - 1 - ax/2 + dy, 1, 3)


def anilloangularinf_reginf(AltVentanaNucleo,AltAxi, Radial,DiamInt,kraft,ax,dy):
    if kraft == 0:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax/2+dy, 1, 3)

    else:

        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1+kraft/2)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1+kraft/2)

        asignmaterials('Weidmann', DiamInt / 2 - 0.5, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax/2+dy, 1, 3)
# -----------------ANILLOS EQ-------------------------

def drawanillo_eqsup(boundary_name,voltage,AltAxi, AltVentanaNucleo, Dimint, radiosint, Radial, offset, h1, hanillo_eq, dy):

     h = offset + h1
     x1 = Dimint / 2 + 2
     y1 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + dy
     x2 = Dimint / 2 + Radial
     y2 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + hanillo_eq + dy

     femm.ei_drawrectangle(x1, y1, x2, y2)


     #definiendo boundaries
     # Definiendo boundaries
     px1 = Dimint / 2 + 2
     py1 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + dy  + hanillo_eq/2

     px2 = (Dimint / 2 + Radial/2)
     py2 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + hanillo_eq + dy

     px3 = (Dimint / 2 + Radial )
     py3 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + dy  + hanillo_eq/2

     px4 = (Dimint / 2 + Radial/2)
     py4 = (AltVentanaNucleo + AltAxi) / 2 + h + 2 + dy

     segment_points = [
         (px1, py1),
         (px2, py2),
         (px3, py3),
         (px4, py4)
     ]

     defboundary(boundary_name,voltage, segment_points, 50)



     femm.ei_createradius(x1, y1, radiosint[0])
     femm.ei_createradius(x2, y1, radiosint[1])
     femm.ei_createradius(x1, y2, radiosint[2])
     femm.ei_createradius(x2, y2, radiosint[2])

     x1 = Dimint / 2
     y1 = (AltVentanaNucleo + AltAxi) / 2 + dy + h
     x2 = Dimint / 2 + Radial + 2
     y2 = (AltVentanaNucleo + AltAxi) / 2 + 2 + hanillo_eq + 2 + dy + h

     femm.ei_drawrectangle(x1, y1, x2, y2)

     femm.ei_createradius(x1, y1, radiosint[0] + 2)
     femm.ei_createradius(x2, y1, radiosint[1] + 2)
     femm.ei_createradius(x1, y2, radiosint[2] + 2)
     femm.ei_createradius(x2, y2, radiosint[2] + 2)

     # Asignar nomesh en el centro
     nomesh(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2)
     # Asignar material
     asignmaterials('Kraftloose', x1 + 1, y1 + (y2 - y1) / 2, 1, 3)

     l = h + 4 + hanillo_eq
     return l

def drawanillo_eqinf(boundary_name,voltage,AltAxi, AltVentanaNucleo, Dimint, radiosint, Radial, offset, h1, hanillo_eq, dy):
     h = offset + h1
     # Primer rectángulo inferior
     x1 = Dimint / 2 + 2
     y1 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 + dy
     x2 = Dimint / 2 + Radial
     y2 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 - hanillo_eq + dy

     femm.ei_drawrectangle(x1, y1, x2, y2)

     #definiendo boundaries
     # Definiendo boundaries
     px1 = Dimint / 2 + Radial/2
     py1 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 + dy

     px2 = (Dimint / 2 + Radial)
     py2 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 - hanillo_eq/2 + dy

     px3 = (Dimint / 2 + Radial/2 )
     py3 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 - hanillo_eq + dy

     px4 = (Dimint / 2 + 2)
     py4 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 - hanillo_eq/2 + dy

     segment_points = [
         (px1, py1),
         (px2, py2),
         (px3, py3),
         (px4, py4)
     ]

     defboundary(boundary_name,voltage, segment_points, 50)


     femm.ei_createradius(x1, y1, radiosint[0])
     femm.ei_createradius(x2, y1, radiosint[1])
     femm.ei_createradius(x1, y2, radiosint[2])
     femm.ei_createradius(x2, y2, radiosint[2])

     # Segundo rectángulo inferior (con margen extra)
     x1 = Dimint / 2
     y1 = (AltVentanaNucleo - AltAxi) / 2 - h + dy
     x2 = Dimint / 2 + Radial + 2
     y2 = (AltVentanaNucleo - AltAxi) / 2 - h - 2 - hanillo_eq - 2 + dy

     femm.ei_drawrectangle(x1, y1, x2, y2)
     femm.ei_createradius(x1, y1, radiosint[0] + 2)
     femm.ei_createradius(x2, y1, radiosint[1] + 2)
     femm.ei_createradius(x1, y2, radiosint[2] + 2)
     femm.ei_createradius(x2, y2, radiosint[2] + 2)


     # Asignar nomesh en el centro
     nomesh(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2)
     # Asignar material
     asignmaterials('Kraftloose', x1 + 1, y1 + (y2 - y1) / 2, 1, 3)

     l = h + 4 + hanillo_eq
     return l


def drawanillo_eqsup_reginf(boundary_name,voltage,AltVentanaNucleo,AltAxi, Dimint, radiosint, Radial, offset, h1, hanillo_eq,separacion, dy):

     h = offset + h1

     x1 = Dimint / 2 + 2
     y1 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2+ h + 2 + dy
     x2 = Dimint / 2 + Radial
     y2 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + h + 2 + hanillo_eq + dy

     femm.ei_drawrectangle(x1, y1, x2, y2)

     #definiendo boundaries
     # Definiendo boundaries
     px1 = Dimint / 2 + Radial/2
     py1 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2+ h + 2 + dy

     px2 = (Dimint / 2 + Radial)
     py2 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + h + 2 + hanillo_eq/2 + dy

     px3 = (Dimint / 2 + Radial/2 )
     py3 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + h + 2 + hanillo_eq + dy

     px4 = (Dimint / 2 + 2)
     py4 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + h + 2 + hanillo_eq/2 + dy

     segment_points = [
         (px1, py1),
         (px2, py2),
         (px3, py3),
         (px4, py4)
     ]

     defboundary(boundary_name,voltage, segment_points, 50)


     femm.ei_createradius(x1, y1, radiosint[0])
     femm.ei_createradius(x2, y1, radiosint[1])
     femm.ei_createradius(x1, y2, radiosint[2])
     femm.ei_createradius(x2, y2, radiosint[2])

     x1 = Dimint / 2
     y1 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + dy + h
     x2 = Dimint / 2 + Radial + 2
     y2 = (AltVentanaNucleo - AltAxi) / 2 +(AltAxi-separacion)/2 + 2 + hanillo_eq + 2 + dy + h

     femm.ei_drawrectangle(x1, y1, x2, y2)
     femm.ei_createradius(x1, y1, radiosint[0] + 2)
     femm.ei_createradius(x2, y1, radiosint[1] + 2)
     femm.ei_createradius(x1, y2, radiosint[2] + 2)
     femm.ei_createradius(x2, y2, radiosint[2] + 2)

     # Asignar nomesh en el centro
     nomesh(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2)
     # Asignar material
     asignmaterials('Kraftloose', x1 + 1, y1 + (y2 - y1) / 2, 1, 3)

     l = h + 4 + hanillo_eq
     return l



def drawanillo_eqinf_regsup(boundary_name,voltage,AltVentanaNucleo,AltAxi, Dimint, radiosint, Radial, offset, h1, hanillo_eq,separacion, dy):
    h = offset + h1
    # Primer rectángulo inferior
    x1 = Dimint / 2 + 2
    y1 =  AltVentanaNucleo/2 + separacion/2 - h - 2 + dy
    x2 = Dimint / 2 + Radial
    y2 = AltVentanaNucleo/2 + separacion/2  - h - 2 - hanillo_eq + dy

    femm.ei_drawrectangle(x1, y1, x2, y2)

    # Definiendo boundaries
    px1 = Dimint / 2 + Radial / 2
    py1 =  AltVentanaNucleo/2 + separacion/2 - h - 2 + dy

    px2 = (Dimint / 2 + Radial)
    py2 = AltVentanaNucleo/2 + separacion/2  - h - 2 - hanillo_eq/2 + dy

    px3 = (Dimint / 2 + Radial / 2)
    py3 = AltVentanaNucleo/2 + separacion/2  - h - 2 - hanillo_eq + dy

    px4 = (Dimint / 2 + 2)
    py4 = AltVentanaNucleo/2 + separacion/2  - h - 2 - hanillo_eq/2 + dy

    segment_points = [
        (px1, py1),
        (px2, py2),
        (px3, py3),
        (px4, py4)
    ]

    defboundary(boundary_name, voltage, segment_points, 50)

    femm.ei_createradius(x1, y1, radiosint[0])
    femm.ei_createradius(x2, y1, radiosint[1])
    femm.ei_createradius(x1, y2, radiosint[2])
    femm.ei_createradius(x2, y2, radiosint[2])

    # Segundo rectángulo inferior (con margen extra)
    x1 = Dimint / 2
    y1 = AltVentanaNucleo/2 + separacion/2  - h + dy
    x2 = Dimint / 2 + Radial + 2
    y2 = AltVentanaNucleo/2 + separacion/2  - h - 2 - hanillo_eq - 2 + dy

    femm.ei_drawrectangle(x1, y1, x2, y2)
    femm.ei_createradius(x1, y1, radiosint[0] + 2)
    femm.ei_createradius(x2, y1, radiosint[1] + 2)
    femm.ei_createradius(x1, y2, radiosint[2] + 2)
    femm.ei_createradius(x2, y2, radiosint[2] + 2)


    # Asignar nomesh en el centro
    nomesh(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2)
    # Asignar material
    asignmaterials('Kraftloose', x1 + 1, y1 + (y2 - y1) / 2, 1, 3)

    l = h + 4 + hanillo_eq
    return l
 #--------------------------PUNTA CENTRAL-----------------------------

def draw_punta_central(boundary_name,voltagereg,L,A,esp,DimInt,AltVentanaNucleo, Radial,dy):

    #Encintando

    x1=DimInt/2+Radial+5
    y1=AltVentanaNucleo/2+dy-A/2
    x2=DimInt/2+Radial+5+L
    y2=AltVentanaNucleo/2+dy+A/2


    femm.ei_drawrectangle(x1, y1, x2, y2)


 #------------------------------------------------------------------------------------------------------------------------------------------------

def drawdev_fullreg(boundary_name,voltagereg,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,dy,separacion):
    agregar_altura(AltAxi)
    agregar_cabecerassup(cabsup)
    agregar_cabecerasInf(cabinf)
    agregar_radiales(Radial)
    agregar_dimint(DiamInt)

    ax = round(axial_cond - 1)

    drawdevbase_regsup(boundary_name, voltagereg,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy,separacion)
    anilloangularsup_regsup(AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, ax, dy)
    anilloangularinf_regsup(AltVentanaNucleo, separacion, Radial, DiamInt, kraft, ax, dy)

    drawdevbase_reginf(boundary_name, voltagereg,AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy,separacion)
    anilloangularsup_reginf(AltVentanaNucleo, separacion, Radial, DiamInt, kraft, ax, dy)
    anilloangularinf_reginf(AltVentanaNucleo,AltAxi, Radial,DiamInt,kraft,ax,dy)



