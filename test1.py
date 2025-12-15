# transformer_winding_femm.py
# Requisitos: tener instalado FEMM y un wrapper Python para FEMM (p.ej. "femm" de python-femm / pyFEMM).
# No ejecutes esto a ciegas: ajusta rutas, unidades y parámetros.

import math
import femm   # nombre típico del wrapper; si usas pyfemm u otro, adapta import
def setup_problem():
    femm.openfemm()
    femm.newdocument(0)
    femm.mi_probdef(0, "millimeters", "planar", 1e-8, 1000)


def ensure_materials(materials):
    # materials: dict nombre -> dict de propiedades (permitir usar mi_addmaterial si no existe)
    for name, props in materials.items():
        try:
            femm.mi_getmaterial(name)
        except Exception:
            # props puede tener campos: mu_x, mu_y, Hc, sigma, J, etc.
            # Para simplicidad agregamos un material lineal con permeabilidad relativa.
            mu_r = props.get("mu_r", 1.0)
            sigma = props.get("sigma", 0.0)
            femm.mi_addmaterial(name, mu_r, mu_r, 0, 0, sigma, 0, 0, 0, 0, 0, 0, 0)

def draw_rectangle(xc, yc, width, height, group=0, nodeprop=None):
    # dibuja rectángulo centrado en (xc, yc)
    hw = width/2.0
    hh = height/2.0
    pts = [
        (xc - hw, yc - hh),
        (xc + hw, yc - hh),
        (xc + hw, yc + hh),
        (xc - hw, yc + hh),
    ]
    # Añadir nodos
    for (x,y) in pts:
        femm.mi_addnode(x, y)
    # Añadir segmentos
    for i in range(len(pts)):
        x1,y1 = pts[i]
        x2,y2 = pts[(i+1)%len(pts)]
        femm.mi_addsegment(x1, y1, x2, y2)
    # Añadir bloque (label) en centro y retornar coordenadas centro
    femm.mi_addblocklabel(xc, yc)
    return (xc, yc)

def add_block_properties_at(xc, yc, material_name, mesh_size=5, turns=0, circuit_name=None, mag_dir=0):
    # selecciona el label y define las propiedades del bloque
    femm.mi_selectlabel(xc, yc)
    # mi_setblockprop(name, automesh, meshsize, incircuit, magdir, group, turns)
    incircuit = circuit_name if circuit_name is not None else "<None>"
    femm.mi_setblockprop(material_name, False, mesh_size, incircuit, mag_dir, 0, turns)
    femm.mi_clearselected()

def add_circuit(name, current):
    # tipo 0 = series circuit / DC? (FEMM usa "addcircprop(name, current, circuittype)")
    femm.mi_addcircprop(name, current, 0)

def save_and_mesh(filename):
    femm.mi_saveas(filename)   # guarda por primera vez
    femm.mi_createmesh()       # ahora sí existe archivo


def create_winding_example():
    setup_problem()

    # --- Definir materiales
    materials = {
        "Air": {"mu_r":1.0},
        "Copper": {"mu_r":1.0, "sigma":5.96e7},
        "Insulation": {"mu_r":1.0, "sigma":0.0},
        "Iron": {"mu_r":5000}
    }
    ensure_materials(materials)

    # Parámetros del devanado (ejemplo)
    # coordenadas centrales de la primera espira
    x_center = 0.0
    y_center = 0.0
    turn_width = 6.0   # ancho de conductor por vuelta (mm)
    turn_height = 10.0 # alto de conductor (mm)
    n_turns = 10
    spacing = 0.5      # separación entre vueltas (mm)
    insulation_thickness = 0.8  # capa de aislamiento externa (mm)

    # circuito
    circuit_name = "Winding1"
    current_A = 10.0
    add_circuit(circuit_name, current_A)

    # Dibujar las vueltas como rectángulos anidados (simple aproximación)
    # Lo ideal es generar perfil de cada espira según tu geometría real (apilado axial o toroidal)
    x = x_center
    y = y_center
    # empezamos en el interior y vamos hacia afuera
    for i in range(n_turns):
        w = turn_width + 2*i*(turn_width + spacing)  # ejemplo de separación lateral, adapta según tu packing
        h = turn_height
        xc = x + i * (turn_width + spacing)  # desplazar cada vuelta en X para demostración
        yc = y
        cx, cy = draw_rectangle(xc, yc, w, h)
        # colocamos label y propiedades (cobre)
        add_block_properties_at(cx, cy, "Copper", mesh_size=2.0, turns=1, circuit_name=circuit_name)

    # Añadir capa de aislamiento alrededor (simple envolvente)
    outer_w = (n_turns)*(turn_width+spacing) + 2*insulation_thickness
    outer_h = turn_height + 2*insulation_thickness
    cx,cy = draw_rectangle(x_center + (n_turns-1)*(turn_width+spacing)/2.0, y_center, outer_w, outer_h)
    add_block_properties_at(cx, cy, "Insulation", mesh_size=3.0, turns=0, circuit_name=None)

    # Guardar y mallar
    save_and_mesh("transformer_winding_example.fem")

if __name__ == "__main__":
    create_winding_example()
