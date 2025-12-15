# PROYECTO:

# ANÁLISIS DE AISLAMIENTO EN DEVANADOS
# DE TRANSFORMADORES DE POTENCIA CON EL METODO
# DE LOS ELEMENTOS FINITOS MEDIANTE FEMM-PYTHON

# AUTORES: JAIR Z.G-ABRAHAM G.L
# V1.0

####################################################################################
# PARTE1: CONSTRUCCIÓN DE LOS ELEMENTOS GEOMÉTRICOS EN DEVANADOS
print("hi abraham")
import femm
from win32con import ABSOLUTE

# Inicio y conexión con FEMM
femm.openfemm()

# Creación de nuevo documento
femm.newdocument(1)

# Definición de ei_probdef(units, type, precision, depth, minangle)
# En la interfaz indicar con selección si es planar o axisimétrica la simulación
x=1

sele = 2  # Cambiar el valor según la simulación deseada

if sele == 1:
    femm.ei_probdef('millimeters', 'planar', 10 ** (-8), 10 ** 6, 30)
    print("Conf: Milímetros, Planar, 1e-8, 30")
elif sele == 2:
    femm.ei_probdef('millimeters', 'axi', 10 ** (-8), 0, 30)
    print("Conf: Milímetros, Axisimétrica, 1e-8, 30")

# --------------------------------------|COMIENZO DIBUJO|-----------------------------------------


# ====================== DATOS DE DISTANCIAS NUCLEO-DEVANADO HV ======================

CABHV = 80  # DISTANCIA DE LA CABECERA DE ALTA TENSION
DistDevHV_YUGO_SUP = 120  # DISTANCIA DEL DE DEVANADO DE ALTA TENSION AL YUGO SUPERIOR
DistDevHV_YUGO_INF = 20  # DISTANCIA DEL DE DEVANADO DE ALTA TENSION AL YUGO INFERIOR
VentanaNucleo = 1560  # DISTANCIA DEL la VENTANA DEL NUCLEO
DimCilTer = 785  # DIAMETRO DEL CILINDRO ININTERIOR HASTA EL DEVANADO TERCIARIO

# ====================== DIBUJANDO DEVANADOS Y NUCLEO ======================
# DESPLAZAMIENTO GENERAL DADO EL NUCLEO,
# (DISTANCIAS POR SI SE NECESITA MOVER EL SISTEMA)
movx = 0
movy = CABHV + DistDevHV_YUGO_INF

# DEV TERCIARIO
DimIntTER = 827  # DIAMETRO INTERNO DEL DEVANADO TERCIARIO
RadTer = 20  # RADIO DEVANADO TERCIARIO
AltAxiTer = 2340  # ALTURA MECANICA DEVANADO TERCIARIO
femm.ei_drawrectangle(DimIntTER / 2 + movx, movy, DimIntTER / 2 + RadTer + movx, AltAxiTer + movy)

# DEV BAJA TENSION
DimIntLV = 913  # DIAMETRO INTERNO DEL DEVANADO DE BAJA TENSION
RadLV = 63  # RADIO DEVANADO DEL DEVANADO DE BAJA TENSION
AltAxiLV = 2380  # ALTURA MECANICA DEL DEVANADO DE BAJA TENSION

if AltAxiLV >= AltAxiTer:
    femm.ei_drawrectangle(DimIntLV / 2 + movx, -abs(AltAxiTer - AltAxiLV) / 2 + movy, DimIntLV / 2 + RadLV + movx,
                          AltAxiLV - abs(AltAxiTer - AltAxiLV) / 2 + movy)
elif AltAxiLV <= AltAxiTer:

    femm.ei_drawrectangle(DimIntLV / 2 + movx, abs(AltAxiTer - AltAxiLV) / 2 + movy, DimIntLV / 2 + RadLV + movx,
                          AltAxiLV + abs(AltAxiTer - AltAxiLV) / 2 + movy)

# DEV ALTA TENSION
DimIntHV = 1155  # DIAMETRO INTERNO DEL DEVANADO DE ALTA TENSION
RadHV = 107  # RADIO DEVANADO DEL DEVANADO DE ALTA TENSION
AltAxiHV = 2340  # ALTURA MECANICA DEL DEVANADO DE ALTA TENSION

if AltAxiHV >= AltAxiTer:
    femm.ei_drawrectangle(DimIntHV / 2 + movx, -abs(AltAxiTer - AltAxiHV) / 2 + movy, DimIntHV / 2 + RadHV + movx,
                          AltAxiHV - abs(AltAxiTer - AltAxiHV) / 2 + movy)
elif AltAxiHV <= AltAxiTer:
    femm.ei_drawrectangle(DimIntHV / 2 + movx, abs(AltAxiTer - AltAxiHV) / 2 + movy, DimIntHV / 2 + RadHV + movx,
                          AltAxiLV + abs(AltAxiTer - AltAxiHV) + movy)

# NUCLEO
femm.ei_drawrectangle(DimCilTer / 2, 0, VentanaNucleo, AltAxiHV + 2 * CABHV + DistDevHV_YUGO_INF + DistDevHV_YUGO_SUP)

# DEV REG SUP E INF
DimIntREG = 1475  # DIAMETRO INTERNO DEL DEVANADO DE REGULACION DE ALTA TENSION
RadREG = 21  # RADIO DEVANADO DEL DEVANADO DE REGULACION DE ALTA TENSION
AltAxiREG = 1790  # ALTURA MECANICA DEL DEVANADO DE REGULACION DE ALTA TENSION
DistREGSUP_REGINF = 604  # DISTANCIA ENTRE LA REGULACION SUPERIOR E INFERIOR
AltRegSup_Inf = (AltAxiREG - DistREGSUP_REGINF) / 2  # ALTURA MECANICA DEL DEVANADO SUP E INF DE REGULACION

# -regsup
femm.ei_drawrectangle(DimIntREG / 2 + movx, (AltAxiTer + DistREGSUP_REGINF) / 2 + movy, DimIntREG / 2 + RadREG + movx,
                      AltRegSup_Inf + (AltAxiTer + DistREGSUP_REGINF) / 2 + movy)
# -reginf
femm.ei_drawrectangle(DimIntREG / 2 + movx, (AltAxiTer - AltAxiREG) / 2 + movy, DimIntREG / 2 + RadREG + movx,
                      (AltAxiTer - DistREGSUP_REGINF) / 2 + movy)

# ====================== DIBUJANDO CILINDROS ======================

# Cilindros pierma-terciario

cil_leg_ter = []
esp_tiras_leg_ter = []
cantidad_cil_leg_ter = int(input("¿Cuántos cilindros hay entre core y terciario? "))
cantidad_tir_leg_ter = int(input("¿Cuántos tiras hay entre core y terciario? "))

for i in range(cantidad_cil_leg_ter):
    try:
        n = float(input(f"Ingrese el espesor del cilindro {i + 1}: "))
        cil_leg_ter.append(n)
    except ValueError:
        print("Error: No ingresó un número válido. Intente de nuevo.")
        break

# print(f"Los números ingresados son: {cil_leg_ter}")

# for i in range(cantidad_cil_leg_ter):
#    x1 =DimCilTer +    # Coordenada X inicial
# y1 = 0                       # Coordenada Y inicial
# x2 = x1 + ancho              # Coordenada X final
# y2 = y1 + alto               # Coordenada Y final

# Dibujar el rectángulo en FEMM
# femm.mi_drawrectangle(x1, y1, x2, y2)
# print(f"Rectángulo #{i + 1} dibujado: ({x1}, {y1}) a ({x2}, {y2})")


for i in range(cantidad_tir_leg_ter):
    try:
        n = float(input(f"Ingrese el espesor de la tira {i + 1}: "))
        esp_tiras_leg_ter.append(n)
    except ValueError:
        print("Error: No ingresó un número válido. Intente de nuevo.")
        break

# print(f"Los números ingresados son: {esp_tiras_leg_ter}")


# ====================== DIBUJANDO PROTECCION CABECERAS AL NUCLEO======================

dy_dev_coresup = 3
dy_dev_coreinf = 6

# nota: falta agregar longitud en x dado los cilindros y distancia entre REG_AT fase 1 y REG_AT fase2, ese parametro se modela con 'sumdx_cil'
sumdx_cil = 0
femm.ei_drawrectangle(DimIntTER / 2, AltAxiHV + CABHV - dy_dev_coresup + movy,
                      DimIntREG / 2 + RadREG + movx + sumdx_cil, AltAxiHV + CABHV + movy)
femm.ei_drawrectangle(DimIntTER / 2, movy - CABHV, DimIntREG / 2 + RadREG + movx + sumdx_cil,
                      movy - CABHV + dy_dev_coreinf)

input("Simulación terminada. Presiona Enter para salir...")
