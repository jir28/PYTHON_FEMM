import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Importamos la lógica que creamos en el Paso 1
import logica_femm


class TransformadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador FEMM - Transformadores de Potencia")
        self.root.geometry("600x700")

        # --- Contenedor Principal con Pestañas ---
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=True)

        # Crear frames para cada pestaña
        self.frame_gral = ttk.Frame(notebook)
        self.frame_nucleo = ttk.Frame(notebook)
        self.frame_serie = ttk.Frame(notebook)
        self.frame_comun = ttk.Frame(notebook)
        self.frame_cilindros = ttk.Frame(notebook)

        notebook.add(self.frame_gral, text='General')
        notebook.add(self.frame_nucleo, text='Núcleo')
        notebook.add(self.frame_serie, text='Dev. Serie')
        notebook.add(self.frame_comun, text='Dev. Común')
        notebook.add(self.frame_cilindros, text='Aislamientos')

        # Inicializar componentes
        self.crear_pestana_general()
        self.crear_pestana_nucleo()
        self.crear_pestana_serie()
        self.crear_pestana_comun()
        self.crear_boton_ejecutar()

    def crear_pestana_general(self):
        ttk.Label(self.frame_gral, text="Configuración Global", font=('Arial', 12, 'bold')).pack(pady=10)

        # Tipo de simulación
        ttk.Label(self.frame_gral, text="Tipo de Simulación:").pack()
        self.combo_tipo = ttk.Combobox(self.frame_gral, values=["Axisimétrica", "Planar"])
        self.combo_tipo.current(0)  # Default Axisimétrica
        self.combo_tipo.pack()

    def crear_pestana_nucleo(self):
        # Usamos una grid para organizar bonito
        frame = ttk.LabelFrame(self.frame_nucleo, text="Dimensiones del Núcleo (mm)")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.ent_nuc_alt = self.crear_input(frame, "Altura Ventana:", "790", 0)
        self.ent_nuc_anch = self.crear_input(frame, "Ancho Ventana:", "390", 1)
        self.ent_nuc_diam = self.crear_input(frame, "Diámetro Núcleo:", "305", 2)
        self.ent_nuc_cabsup = self.crear_input(frame, "Cabezal Superior:", "140", 3)  # 50+90
        self.ent_nuc_cabinf = self.crear_input(frame, "Cabezal Inferior:", "50", 4)

    def crear_pestana_serie(self):
        frame = ttk.LabelFrame(self.frame_serie, text="Parámetros Devanado Serie")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.var_serie_activo = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Incluir este devanado", variable=self.var_serie_activo).grid(row=0, column=0,
                                                                                                 columnspan=2)

        self.ent_ser_volt = self.crear_input(frame, "Voltaje (V):", "50000", 1)
        self.ent_ser_altaxi = self.crear_input(frame, "Altura Axial:", "600", 2)
        self.ent_ser_radial = self.crear_input(frame, "Espesor Radial:", "47", 3)
        self.ent_ser_diamint = self.crear_input(frame, "Diámetro Interno:", "345", 4)
        self.ent_ser_cond = self.crear_input(frame, "Axial Conductor:", "10.886", 5)
        self.ent_ser_kraft = self.crear_input(frame, "Aislamiento Papel:", "0.0", 6)

    def crear_pestana_comun(self):
        frame = ttk.LabelFrame(self.frame_comun, text="Parámetros Devanado Común")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.var_comun_activo = tk.BooleanVar(value=True)
        tk.Checkbutton(frame, text="Incluir este devanado", variable=self.var_comun_activo).grid(row=0, column=0,
                                                                                                 columnspan=2)

        self.ent_com_volt = self.crear_input(frame, "Voltaje (V):", "80000", 1)
        self.ent_com_altaxi = self.crear_input(frame, "Altura Axial:", "600", 2)
        self.ent_com_radial = self.crear_input(frame, "Espesor Radial:", "83", 3)
        self.ent_com_diamint = self.crear_input(frame, "Diámetro Interno:", "499", 4)
        self.ent_com_cond = self.crear_input(frame, "Axial Conductor:", "13.336", 5)
        self.ent_com_kraft = self.crear_input(frame, "Aislamiento Papel:", "0.0", 6)

    def crear_input(self, parent, label_text, default_val, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="e")
        entry = ttk.Entry(parent)
        entry.insert(0, default_val)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def crear_boton_ejecutar(self):
        btn = ttk.Button(self.root, text="GENERAR GEOMETRÍA EN FEMM", command=self.recopilar_y_ejecutar)
        btn.pack(side="bottom", fill="x", padx=20, pady=20)

    def recopilar_y_ejecutar(self):
        try:
            # Recopilación de datos (Diccionario gigante)
            datos = {
                'tipo_simulacion': 'axi' if self.combo_tipo.get() == "Axisimétrica" else 'Planar',

                # NUCLEO
                'nucleo_alto': float(self.ent_nuc_alt.get()),
                'nucleo_ancho': float(self.ent_nuc_anch.get()),
                'nucleo_diametro': float(self.ent_nuc_diam.get()),
                'nucleo_cab_sup': float(self.ent_nuc_cabsup.get()),
                'nucleo_cab_inf': float(self.ent_nuc_cabinf.get()),

                # SERIE
                'serie_activo': self.var_serie_activo.get(),
                'serie_voltage': float(self.ent_ser_volt.get()),
                'serie_alt_axi': float(self.ent_ser_altaxi.get()),
                'serie_radial': float(self.ent_ser_radial.get()),
                'serie_diam_int': float(self.ent_ser_diamint.get()),
                'serie_axial_cond': float(self.ent_ser_cond.get()),
                'serie_kraft': float(self.ent_ser_kraft.get()),

                # COMUN
                'comun_activo': self.var_comun_activo.get(),
                'comun_voltage': float(self.ent_com_volt.get()),
                'comun_alt_axi': float(self.ent_com_altaxi.get()),
                'comun_radial': float(self.ent_com_radial.get()),
                'comun_diam_int': float(self.ent_com_diamint.get()),
                'comun_axial_cond': float(self.ent_com_cond.get()),
                'comun_kraft': float(self.ent_com_kraft.get()),

                # CILINDROS (Hardcodeado ejemplo simple, idealmente sería una lista dinámica)
                'cilindros': [
                    {'dim_int': 305 + 18, 'alt_axi': 655, 'radial': 3},  # C1 ejemplo
                    # Aquí puedes agregar lógica para leer inputs de la pestaña cilindros
                ]
            }

            # Llamar a la lógica FEMM
            logica_femm.ejecutar_simulacion(datos)
            messagebox.showinfo("Éxito", "Simulación enviada a FEMM")

        except ValueError:
            messagebox.showerror("Error", "Por favor revisa que todos los campos sean numéricos.")
        except Exception as e:
            messagebox.showerror("Error Crítico", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = TransformadorApp(root)
    root.mainloop()