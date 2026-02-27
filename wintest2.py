import tkinter as tk
from tkinter import ttk, messagebox
import json


# Importar tu lógica de dibujo (asegúrate de que los archivos .py estén en la misma carpeta)
# from logica_femm import dibujar_transformador  <-- Esto lo crearemos en el paso 2

class TransformadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseñador FEMM - Transformadores Dinámicos")
        self.root.geometry("900x700")

        # --- Contenedor Principal (Pestañas) ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, fill='both', expand=True)

        # Crear frames
        self.tab_nucleo = ttk.Frame(self.notebook)
        self.tab_devanados = ttk.Frame(self.notebook)
        self.tab_aislamientos = ttk.Frame(self.notebook)  # <--- AQUÍ ESTÁ LA CLAVE

        self.notebook.add(self.tab_nucleo, text='1. Núcleo')
        self.notebook.add(self.tab_devanados, text='2. Devanados')
        self.notebook.add(self.tab_aislamientos, text='3. Aislamientos (Dinámico)')

        self.setup_nucleo()
        self.setup_devanados()
        self.setup_aislamientos_dinamicos()

        # Botón Acción
        btn_frame = ttk.Frame(root)
        btn_frame.pack(side='bottom', pady=10)
        ttk.Button(btn_frame, text="GENERAR EN FEMM", command=self.ejecutar_femm).pack(side='left', padx=10)
        ttk.Button(btn_frame, text="Guardar Config (JSON)", command=self.guardar_json).pack(side='left', padx=10)

    # ---------------- SECCIÓN NÚCLEO (Estática) ----------------
    def setup_nucleo(self):
        frame = ttk.LabelFrame(self.tab_nucleo, text="Geometría del Núcleo")
        frame.pack(padx=20, pady=20, fill="x")

        self.vars_nucleo = {}
        campos = [
            ("Diámetro Núcleo (mm):", "305"),
            ("Ancho Ventana (mm):", "390"),
            ("Alto Ventana (mm):", "790"),
            ("Cabezal Superior (mm):", "140"),
            ("Cabezal Inferior (mm):", "50")
        ]

        for idx, (lbl, default) in enumerate(campos):
            ttk.Label(frame, text=lbl).grid(row=idx, column=0, padx=5, pady=5, sticky='e')
            var = tk.StringVar(value=default)
            ttk.Entry(frame, textvariable=var).grid(row=idx, column=1, padx=5, pady=5)
            # Guardamos la referencia usando la etiqueta como clave simple
            key = lbl.split()[0].lower()  # "Diámetro" -> "diámetro"
            self.vars_nucleo[key] = var

    # ---------------- SECCIÓN DEVANADOS (Semi-Estática) ----------------
    def setup_devanados(self):
        # Aquí podrías hacerlo dinámico también, pero por ahora usaremos tu esquema LV/HV
        frame_lv = ttk.LabelFrame(self.tab_devanados, text="Devanado Baja Tensión (LV / Serie)")
        frame_lv.pack(padx=10, pady=5, fill="x")

        self.vars_lv = self.crear_campos_devanado(frame_lv, "50000", "600", "47", "345", "10.886")

        frame_hv = ttk.LabelFrame(self.tab_devanados, text="Devanado Alta Tensión (HV / Común)")
        frame_hv.pack(padx=10, pady=5, fill="x")

        self.vars_hv = self.crear_campos_devanado(frame_hv, "80000", "600", "83", "499", "13.336")

    def crear_campos_devanado(self, parent, v, h, rad, di, cond):
        vars_dict = {}
        datos = [("Voltaje", v), ("Altura Axial", h), ("Radial", rad), ("Diam. Int", di), ("Axial Cond", cond)]
        for i, (lbl, val) in enumerate(datos):
            ttk.Label(parent, text=lbl).grid(row=0, column=i * 2, padx=2)
            var = tk.StringVar(value=val)
            ttk.Entry(parent, textvariable=var, width=10).grid(row=0, column=i * 2 + 1, padx=5)
            vars_dict[lbl] = var
        return vars_dict

    # ---------------- SECCIÓN AISLAMIENTOS (DINÁMICA) ----------------
    def setup_aislamientos_dinamicos(self):
        """ Esta es la parte que resuelve tu problema de configuraciones variables """
        panel_izq = ttk.Frame(self.tab_aislamientos)
        panel_izq.pack(side='left', fill='y', padx=10, pady=10)

        panel_der = ttk.LabelFrame(self.tab_aislamientos, text="Lista de Cilindros/Barreras")
        panel_der.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        # -- Formulario para agregar nuevo cilindro --
        ttk.Label(panel_izq, text="Nuevo Cilindro", font=('bold')).pack(pady=5)

        self.var_iso_di = tk.StringVar()
        self.var_iso_h = tk.StringVar()
        self.var_iso_rad = tk.StringVar()
        self.var_iso_mat = tk.StringVar(value="TIV")

        ttk.Label(panel_izq, text="Diámetro Interno:").pack()
        ttk.Entry(panel_izq, textvariable=self.var_iso_di).pack()

        ttk.Label(panel_izq, text="Altura Axial:").pack()
        ttk.Entry(panel_izq, textvariable=self.var_iso_h).pack()

        ttk.Label(panel_izq, text="Espesor Radial:").pack()
        ttk.Entry(panel_izq, textvariable=self.var_iso_rad).pack()

        ttk.Button(panel_izq, text="--> Agregar a Lista", command=self.agregar_cilindro).pack(pady=15)
        ttk.Button(panel_izq, text="Borrar Seleccionado", command=self.borrar_cilindro).pack(pady=5)

        # -- Tabla (Treeview) para ver lo agregado --
        columns = ('diam', 'altura', 'espesor')
        self.tree = ttk.Treeview(panel_der, columns=columns, show='headings')
        self.tree.heading('diam', text='Diam. Int (mm)')
        self.tree.heading('altura', text='Altura (mm)')
        self.tree.heading('espesor', text='Espesor (mm)')
        self.tree.pack(fill='both', expand=True)

    def agregar_cilindro(self):
        # Validación simple
        try:
            d = float(self.var_iso_di.get())
            h = float(self.var_iso_h.get())
            r = float(self.var_iso_rad.get())
            self.tree.insert('', 'end', values=(d, h, r))
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

    def borrar_cilindro(self):
        selected = self.tree.selection()
        for item in selected:
            self.tree.delete(item)

    # ---------------- LÓGICA DE SALIDA ----------------
    def ejecutar_femm(self):
        # 1. Recopilar Datos Estáticos
        datos_proyecto = {
            "nucleo": {k: float(v.get()) for k, v in self.vars_nucleo.items()},
            "lv": {k: float(v.get()) for k, v in self.vars_lv.items()},
            "hv": {k: float(v.get()) for k, v in self.vars_hv.items()},
            "aislamientos": []
        }

        # 2. Recopilar Datos Dinámicos de la Tabla
        for child in self.tree.get_children():
            valores = self.tree.item(child)['values']
            datos_proyecto["aislamientos"].append({
                "diametro": float(valores[0]),
                "altura": float(valores[1]),
                "espesor": float(valores[2])
            })

        print("Enviando datos a FEMM:", datos_proyecto)

        # AQUÍ LLAMARÍAS A TU SCRIPT LÓGICO:
        # logica_femm.dibujar_transformador(datos_proyecto)
        messagebox.showinfo("FEMM", "Datos enviados (Revisar consola)")

    def guardar_json(self):
        # Útil para guardar configuraciones complejas y no reescribirlas
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TransformadorGUI(root)
    root.mainloop()