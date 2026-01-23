import femm

# Inicia FEMM
femm.openfemm()
femm.newdocument(1)  # electro problem

# ------------ Parámetros ------------ #
x = 10  # Coordenada x de la esquina
y = 20  # Coordenada y de la esquina
r = 5   # Radio del arco

# ------------ Crear esquina y convertirla en arco ------------ #
# Dibuja un rectángulo para ejemplo
#femm.mi_drawrectangle(0, 0, 20, 30)

# Convierte la esquina en un arco
#femm.mi_createradius(x, y, r)


a=2150
b=785
c=735

femm.ei_drawrectangle(c/2,0, a, b)
#femm.mi_createradius(c/2, 0, 1)


input("Simulación terminada. Presiona Enter para salir...")
