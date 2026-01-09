#PROYECTO:
from tkinter.constants import MOVETO

# ANÁLISIS DE AISLAMIENTO EN DEVANADOS
# DE TRANSFORMADORES DE POTENCIA CON EL METODO
# DE LOS ELEMENTOS FINITOS MEDIANTE FEMM-PYTHON

#AUTORES: JAIR Z.G-ABRAHAM G.L
# V1.0

####################################################################################
# PARTE1: CONSTRUCCIÓN DE LOS ELEMENTOS GEOMÉTRICOS EN DEVANADOS
import femm

# Inicio y conexión con FEMM
femm.openfemm()

# Creación de nuevo documento
femm.newdocument(1)

# Definición de ei_probdef(units, type, precision, depth, minangle)
# En la interfaz indicar con selección si es planar o axisimétrica la simulación

sele = 2  # Cambiar el valor según la simulación deseada

if sele == 1:
    femm.ei_probdef('millimeters', 'planar', 10 ** (-8), 10 ** 6, 30)
    print("Conf: Milímetros, Planar, 1e-8, 30")
elif sele == 2:
    femm.ei_probdef('millimeters', 'axi', 10 ** (-8), 0, 30)
    print("Conf: Milímetros, Axisimétrica, 1e-8, 30")

# --------------------------------------|COMIENZO DIBUJO|-----------------------------------------

# ====================== DATOS DE DISTANCIAS NUCLEO-DEVANADO HV ======================

# ====================== DIBUJANDO DEVANADOS Y NUCLEO ======================


# -------DEV TERCIARIO-----
DimIntTER = 827  # DIAMETRO INTERNO DEL DEVANADO TERCIARIO
RadTer = 20  # RADIAL DEVANADO TERCIARIO
AltAxiTer = 2340  # ALTURA MECANICA DEVANADO TERCIARIO
CABTER =80

# DESPLAZAMIENTO GENERAL DADO EL NUCLEO,
# (DISTANCIAS POR SI SE NECESITA MOVER EL SISTEMA)
DistDev_YUGO_SUP = 120  # DISTANCIA DEL DE DEVANADO DE ALTA TENSION AL YUGO SUPERIOR
DistDev_YUGO_INF = 20  # DISTANCIA DEL DE DEVANADO DE ALTA TENSION AL YUGO INFERIOR

movx = 0
movy = CABTER + DistDev_YUGO_INF


femm.ei_drawrectangle(DimIntTER / 2 + movx, movy, DimIntTER / 2 + RadTer + movx, AltAxiTer + movy)

# -------DEV BAJA TENSION -------
DimIntLV = 913  # DIAMETRO INTERNO DEL DEVANADO DE BAJA TENSION
RadLV = 63  # RADIAL DEVANADO DEL DEVANADO DE BAJA TENSION
AltAxiLV = 2380  # ALTURA MECANICA DEL DEVANADO DE BAJA TENSION
CABLV=80

if AltAxiLV >= AltAxiTer:
    femm.ei_drawrectangle(DimIntLV / 2 + movx, -abs(AltAxiTer - AltAxiLV) / 2 + movy, DimIntLV / 2 + RadLV + movx,
                          AltAxiLV - abs(AltAxiTer - AltAxiLV) / 2 + movy)
elif AltAxiLV <= AltAxiTer:

    femm.ei_drawrectangle(DimIntLV / 2 + movx, abs(AltAxiTer - AltAxiLV) / 2 + movy, DimIntLV / 2 + RadLV + movx,
                          AltAxiLV + abs(AltAxiTer - AltAxiLV) / 2 + movy)

# -------DEV ALTA TENSION -------
DimIntHV = 1155  # DIAMETRO INTERNO DEL DEVANADO DE ALTA TENSION
RadHV = 107  # RADIAL DEVANADO DEL DEVANADO DE ALTA TENSION
AltAxiHV = 2340  # ALTURA MECANICA DEL DEVANADO DE ALTA TENSION
CABHV = 80  # DISTANCIA DE LA CABECERA DE ALTA TENSION

if AltAxiHV >= AltAxiTer:
    femm.ei_drawrectangle(DimIntHV / 2 + movx, -abs(AltAxiTer - AltAxiHV) / 2 + movy, DimIntHV / 2 + RadHV + movx,
                          AltAxiHV - abs(AltAxiTer - AltAxiHV) / 2 + movy)
elif AltAxiHV <= AltAxiTer:
    femm.ei_drawrectangle(DimIntHV / 2 + movx, abs(AltAxiTer - AltAxiHV) / 2 + movy, DimIntHV / 2 + RadHV + movx,
                          AltAxiLV + abs(AltAxiTer - AltAxiHV) + movy)

# -------NUCLEO -------

VentanaNucleo = 1560  # DISTANCIA DEL la VENTANA DEL NUCLEO
Dimint= 785  # DIAMETRO DEL CILINDRO ININTERIOR HASTA EL DEVANADO TERCIARIO
femm.ei_drawrectangle(Dimint / 2, 0, VentanaNucleo, AltAxiHV + 2 * CABHV + DistDev_YUGO_INF + DistDev_YUGO_SUP)

# -------DEV REG SUP E INF -------
DimIntREG = 1475  # DIAMETRO INTERNO DEL DEVANADO DE REGULACION DE ALTA TENSION
RadREG = 21  # RADIAL DEVANADO DEL DEVANADO DE REGULACION DE ALTA TENSION
AltAxiREG = 1790  # ALTURA MECANICA DEL DEVANADO DE REGULACION DE ALTA TENSION
CABREG=355

DistREGSUP_REGINF = 604  # DISTANCIA ENTRE LA REGULACION SUPERIOR E INFERIOR


AltRegSup_Inf = (AltAxiREG - DistREGSUP_REGINF) / 2  # ALTURA MECANICA DEL DEVANADO SUP E INF DE REGULACION

# *regsup
femm.ei_drawrectangle(DimIntREG / 2 + movx, (AltAxiTer + DistREGSUP_REGINF) / 2 + movy, DimIntREG / 2 + RadREG + movx,
                      AltRegSup_Inf + (AltAxiTer + DistREGSUP_REGINF) / 2 + movy)
# *reginf
femm.ei_drawrectangle(DimIntREG / 2 + movx, (AltAxiTer - AltAxiREG) / 2 + movy, DimIntREG / 2 + RadREG + movx,
                      (AltAxiTer - DistREGSUP_REGINF) / 2 + movy)



# ====================== DIBUJANDO PROTECCION CABECERAS AL NUCLEO======================

dy_dev_coresup = 3
dy_dev_coreinf = 6

# nota: falta agregar longitud en x: distancia entre REG_AT fase 1 y REG_AT fase2, ese parametro se modela con 'sumdx_cil'
sumdx_cil = 0
femm.ei_drawrectangle(DimIntTER / 2, AltAxiHV + CABHV - dy_dev_coresup + movy,
                      DimIntREG / 2 + RadREG + movx + sumdx_cil, AltAxiHV + CABHV + movy)
femm.ei_drawrectangle(DimIntTER / 2, movy - CABHV, DimIntREG / 2 + RadREG + movx + sumdx_cil,
                      movy - CABHV + dy_dev_coreinf)

# ====================== DIBUJANDO CILINDROS ======================

# ---- CILINDROS ENTRE LA PIERNA DEL NÚCLEO Y TERCIARIO----
diamintcil=785
acumulado=0

#cil 1 PRINCIPAL TERCIARIO
esp=3
dist_to_cil=12
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil


#================================================================================
# ---- CILINDROS ENTRE TERCIARIO Y BAJA TENSION----
#nota: - Si son cilindros entre devanados se debe acumular la distancia
diamintcil =867
acumulado=0 #Cada que se inicia un nuevo devanado se reinicia el acumulado

#cil 2
esp =2
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 3
esp =3
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil


#================================================================================
# ---- CILINDROS ENTRE BAJA Y ALTA TENSION----
#nota: - Si son cilindros entre devanados se debe acumular la distancia
diamintcil =1039
acumulado=0 #Cada que se inicia un nuevo devanado se reinicia el acumulado

#cil 4
esp =2
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 5
esp =1
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 6
esp =1
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 7
esp =1
dist_to_cil =7
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil


#cil 8
esp =1
dist_to_cil =8
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil


#cil 9
esp =1
dist_to_cil =8
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#================================================================================
# ---- CILINDROS ENTRE ALTA Y REGULACION DE ALTA TENSION----
#nota: - Si son cilindros entre devanados se debe acumular la distancia
diamintcil =1369
acumulado=0 #Cada que se inicia un nuevo devanado se reinicia el acumulado

#cil 10
esp =2
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 11
esp =2
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 12
esp =2
dist_to_cil =6
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 13
esp =2
dist_to_cil =7
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil

#cil 14
esp =4
dist_to_cil =8
Alt_cil1=AltAxiTer+CABHV

x1cil=(diamintcil / 2)+dist_to_cil+movx
x2cil=diamintcil/2+ esp+movx+dist_to_cil
y1cil=movy - CABHV
y2cil=Alt_cil1

femm.ei_drawrectangle(x1cil+acumulado,y1cil ,x2cil+acumulado,y2cil )

#actualizando el acumulado
acumulado=acumulado+esp+dist_to_cil



input("Simulación terminada. Presiona Enter para salir...")
