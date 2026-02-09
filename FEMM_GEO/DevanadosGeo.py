import femm
from  AislamientosGeo import drawanilloangular
from  AislamientosGeo import drawminiangulo


def drawdevbase(AltVentanaNucleo,AltAxi, Radial, DiamInt,kraft,dy):
#Devanado base sin miniangulos, anillo angular, etc.

 if kraft == 0:
     femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, DiamInt / 2 + Radial,
                           (AltVentanaNucleo + AltAxi) / 2 + dy)
     # --------CORNERS--------
     # crea corner inf izq
     femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
     # crea corner sup izq
     femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)
     # crea corner inf derec
     femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5)
     # crea corner sup derech
     femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5)

 else:
    femm.ei_drawrectangle(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, DiamInt / 2 + Radial,
                          (AltVentanaNucleo + AltAxi) / 2 + dy)
    femm.ei_drawrectangle(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy,
                          DiamInt / 2 + Radial - kraft / 2, (AltVentanaNucleo + AltAxi) / 2 - kraft / 2 + dy)

    # --------CORNERS--------
    # crea corner inf izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # crea corner sup izq
    femm.ei_createradius(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # crea corner inf derec
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo - AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo - AltAxi) / 2 + kraft / 2 + dy, 0.5)

    # crea corner sup derech
    femm.ei_createradius(DiamInt / 2 + Radial, (AltVentanaNucleo + AltAxi) / 2 + dy, 0.5 + kraft / 2)
    femm.ei_createradius(DiamInt / 2 + Radial + kraft / 2, (AltVentanaNucleo + AltAxi) / 2 + kraft / 2 + dy, 0.5)



def drawdevanado(AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,dy):
    # Devanado con miniangulos, anillo angular, etc.

    ax = round(axial_cond - 1)
    if kraft==0:
        # --------DEV SIN AISLAMIENTO DE PAPEL--------
        drawdevbase(AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, dy)
        if (Radial + 2 * ax) < 78:
        # --------DEV CON ANILLO ANGULAR--------
            drawanilloangular(AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, dy)
        elif (Radial + 2 * ax) > 78:
        # --------DEV CON ANILLO MINIANGULO-------
            drawminiangulo(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)

    else:
        # --------DEV CON AISLAMIENTO DE PAPEL--------
        drawdevbase(AltVentanaNucleo, AltAxi, Radial, DiamInt, kraft, dy)
        if (Radial + 2 * ax) < 78:
        # --------DEV CON ANILLO ANGULAR--------
            drawanilloangular(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)
        elif (Radial + 2 * ax) > 78:
        # --------DEV CON ANILLO MINIANGULO-------
            drawminiangulo(AltVentanaNucleo, AltAxi, Radial, DiamInt, axial_cond, kraft, dy)



