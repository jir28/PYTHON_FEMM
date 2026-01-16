import numpy as np
from scipy.interpolate import interp1d

# =============================
# Parámetros
# =============================
L_OBJ = 10.0        # mm
N_PUNTOS = None     # conservar número original

archivo_in = "1.txt"
archivo_out = "1000.txt"

# =============================
# Leer archivo
# =============================
header = []
data_lines = []

with open(archivo_in, "r") as f:
    for line in f:
        if line.strip().startswith("%"):
            header.append(line.rstrip("\n"))
        elif line.strip() == "":
            header.append(line.rstrip("\n"))
        else:
            data_lines.append(line.rstrip("\n"))

# =============================
# Parsear datos
# =============================
s = []
V = []

for l in data_lines:
    parts = l.split()
    s.append(float(parts[0]))
    V.append(float(parts[1]))

s = np.array(s)
V = np.array(V)

if N_PUNTOS is None:
    N_PUNTOS = len(s)


interp = interp1d(
    s, V,
    kind="linear",
    bounds_error=False,
    fill_value="extrapolate"
)

s_new = np.linspace(0.0, L_OBJ, N_PUNTOS)
V_new = interp(s_new)

with open(archivo_out, "w") as f:
    for h in header:
        f.write(h + "\n")

    for si, Vi in zip(s_new, V_new):
        f.write(f"{si:13.8e} {Vi:13.8e}\n")

