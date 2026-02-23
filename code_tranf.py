###############################################
# Transformer Loading Script (Python version) #
# BY Abraham GL                               #
# 17/03/2024                                  #
###############################################

import femm
import numpy as np

# Datos preliminares del transformador y carga
n1 = 472           # espiras primario
n2 = 91            # espiras secundario
v1 = 156.25         # voltaje RMS aplicado al primario
Z2 = 1e6           # impedancia de carga
ix = 0.05          # corriente de vacío estimada

# Abrir FEMM e inicializar problema
femm.openfemm()

try:
    femm.opendocument("TRANSF_FEMM.fem")
except:
    femm.opendocument("TRANSF_FEMM.fem")

femm.mi_saveas("solu.fem")

# Construir impedancia aproximada del transformador
femm.mi_setcurrent("Primary", ix)
femm.mi_setcurrent("Secondary", 0)
femm.mi_analyze()
femm.mi_loadsolution()

# Matriz de impedancias del transformador (compleja)
Zt = np.zeros((2,2), dtype=complex)

r = femm.mo_getcircuitproperties("Primary")
Zt[0,0] = r[1]/ix
r = femm.mo_getcircuitproperties("Secondary")
Zt[0,1] = r[1]/ix
Zt[1,0] = Zt[0,1]
Zt[1,1] = Zt[0,0]*(n2/n1)**2

# Matriz de impedancia de carga y vector de voltajes
Zl = np.array([[0,0],[0,Z2]], dtype=complex)
v = np.sqrt(2)*np.array([v1,0], dtype=complex)

# Estimación inicial de corrientes
ic = np.linalg.solve(Zt+Zl, v)

# Iteración para convergencia
for k in range(100):
    femm.mi_setcurrent("Primary", ic[0])
    femm.mi_setcurrent("Secondary", ic[1])
    femm.mi_analyze()
    femm.mi_loadsolution()

    vt = np.zeros(2, dtype=complex)
    r = femm.mo_getcircuitproperties("Primary")
    vt[0] = r[1]
    r = femm.mo_getcircuitproperties("Secondary")
    vt[1] = r[1]

    u = v - vt - Zl @ ic
    ic = ic + np.linalg.solve(Zt+Zl, u)

    print(f"{k}  {abs(np.sqrt(u.T @ u))}")
    if np.sqrt(u.T @ u) < 0.1:
        break

print("\nLoad currents (complex values):")
print(ic)

# Magnitudes RMS
v_1 = abs(vt[0])/np.sqrt(2)
v_2 = abs(vt[1])/np.sqrt(2)

i_1 = abs(ic[0])/np.sqrt(2)
i_2 = abs(ic[1])/np.sqrt(2)

print("\nVoltajes RMS:")
print("v1 =", v_1)
print("v2 =", v_2)

print("\nCorrientes RMS:")
print("i1 =", i_1)
print("i2 =", i_2)

# Mostrar ángulos de fase
print("\nÁngulos de fase (grados):")
print("angle(v1) =", np.angle(vt[0], deg=True))
print("angle(v2) =", np.angle(vt[1], deg=True))
print("angle(i1) =", np.angle(ic[0], deg=True))
print("angle(i2) =", np.angle(ic[1], deg=True))

# Potencia y resistencia equivalente
dat = femm.mo_getcircuitproperties("Secondary")

femm.mo_selectblock(0.0245,0)
femm.mo_selectblock(-0.0245,0)
P = femm.mo_blockintegral(4)  # watts
R = P/(i_2**2)

print("\nEquivalent resistance R =", R)
input("Simulación terminada. Presiona Enter para salir...")