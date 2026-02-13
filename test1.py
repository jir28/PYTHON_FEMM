import femm

# Abrir FEMM y crear documento electrostático
femm.openfemm()
femm.newdocument(1)

# Definir material
femm.ei_addmaterial('OilM', 2.2, 0, 0)

# Dibujar un rectángulo
femm.ei_drawrectangle(0, 0, 50, 30)

# Colocar un block label en el centro del rectángulo
femm.ei_addblocklabel(25, 15)
femm.ei_selectlabel(25, 15)

# Asignar el material y tamaño de malla
femm.ei_setblockprop('OilM', 1, 1, 0)

# Guardar el archivo
input("Simulación terminada. Presiona Enter para salir...")
