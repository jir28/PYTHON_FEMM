#EN ESTE SCRIPT SE HARAN PRUEBAS DE LA VENTANA PRINCIPAL DEL GENERADOR DE FEMM

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel, QSpinBox,
    QDoubleSpinBox, QFrame, QScrollArea
)
from PySide6.QtCore import Qt
import sys

# bloque radial

class RadialBlock(QFrame):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(1)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.type_combo = QComboBox()
        self.type_combo.addItems(["Cilindro", "Devanado"])
        self.type_combo.currentTextChanged.connect(self.update_fields)
        self.layout.addWidget(self.type_combo)

        self.dynamic = QVBoxLayout()
        self.layout.addLayout(self.dynamic)

        self.setLayout(self.layout)
        self.update_fields("Cilindro")

    def set_data(self, data):
        if data["tipo"] == "cilindro":
            self.type_combo.setCurrentText("Cilindro")
            self.d_int.setValue(data["d_int"])
            self.e.setValue(data["espesor"])

        else:
            self.type_combo.setCurrentText("Devanado")
            self.d_int.setValue(data["d_int"])
            self.e.setValue(data["espesor"])
            self.h.setValue(data["altura"])
            self.v.setValue(data["tension"])
            self.insulation.setCurrentText(data["aislamiento"])

            if data["aislamiento"] == "Papel Kraft":
                self.ins_thk.setValue(data.get("espesor_aislamiento", 1.0))

    def toggle_insulation_thickness(self, text):
        is_kraft = (text == "Papel Kraft")
        self.lbl_ins_thk.setVisible(is_kraft)
        self.ins_thk.setVisible(is_kraft)

    def clear(self):
        while self.dynamic.count():
            item = self.dynamic.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def update_fields(self, kind):
        self.clear()

        # DIÁMETRO INTERNO
        lbl_dint = QLabel("Diámetro interno (mm)")
        self.d_int = QDoubleSpinBox()
        self.d_int.setRange(100, 5000)
        self.d_int.setValue(800)

        self.dynamic.addWidget(lbl_dint)
        self.dynamic.addWidget(self.d_int)

        if kind == "Cilindro":
            lbl = QLabel("Espesor (mm)")
            self.e = QDoubleSpinBox()
            self.e.setRange(1, 50)
            self.dynamic.addWidget(lbl)
            self.dynamic.addWidget(self.e)

        else:
            lbl1 = QLabel("Altura axial (mm)")
            self.h = QDoubleSpinBox()
            self.h.setRange(1000, 5000)

            lbl2 = QLabel("Espesor radial (mm)")
            self.e = QDoubleSpinBox()
            self.e.setRange(10, 500)

            lbl3 = QLabel("Tensión (kV)")
            self.v = QDoubleSpinBox()
            self.v.setRange(20, 10000)

            lbl4 = QLabel("Aislamiento conductor")
            self.insulation = QComboBox()
            self.insulation.addItems([
                "Papel Kraft",
                "Cordex",
            ])

            # ESPESOR AISLAMIENTO (solo para Kraft)
            self.lbl_ins_thk = QLabel("Espesor aislamiento (mm)")
            self.ins_thk = QDoubleSpinBox()
            self.ins_thk.setRange(0.1, 10.0)
            self.ins_thk.setSingleStep(0.1)
            self.ins_thk.setValue(1.07)

            # conexión clave
            self.insulation.currentTextChanged.connect(
                self.toggle_insulation_thickness
            )

            self.dynamic.addWidget(lbl1)
            self.dynamic.addWidget(self.h)
            self.dynamic.addWidget(lbl2)
            self.dynamic.addWidget(self.e)
            self.dynamic.addWidget(lbl3)
            self.dynamic.addWidget(self.v)
            self.dynamic.addWidget(lbl4)
            self.dynamic.addWidget(self.insulation)
            self.dynamic.addWidget(self.lbl_ins_thk)
            self.dynamic.addWidget(self.ins_thk)

            # estado inicial
            self.toggle_insulation_thickness(self.insulation.currentText())

    def get_data(self):
        d_int = self.d_int.value()
        esp = self.e.value()
        d_ext = d_int + 2 * esp
        if self.type_combo.currentText() == "Cilindro":
            return {
                "tipo": "cilindro",
                "d_int" : d_int,
                "d_ext" : d_ext,
                "espesor": self.e.value()
            }
        else:
            data = {
                "tipo": "devanado",
                "d_int": d_int,
                "d_ext": d_ext,
                "altura": self.h.value(),
                "espesor": self.e.value(),
                "tension": self.v.value(),
                "aislamiento": self.insulation.currentText()
            }
            if data["aislamiento"] == "Papel Kraft":
                data["espesor_aislamiento"] = self.ins_thk.value()
            return data






#ventana principal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuración Radial de Devanados")
        self.resize(1000, 650)

        main = QVBoxLayout()

        #################Nucleo
        core_box = QFrame()
        core_box.setFrameShape(QFrame.Box)
        core_layout = QHBoxLayout()

        core_layout.addWidget(QLabel("Diámetro externo ventana núcleo (mm):"))
        self.core_diameter = QDoubleSpinBox()
        self.core_diameter.setRange(100, 5000)
        self.core_diameter.setValue(800)
        core_layout.addWidget(self.core_diameter)

        core_layout.addWidget(QLabel("Altura de ventana (mm):"))
        self.window_height = QDoubleSpinBox()
        self.window_height.setRange(100, 5000)
        self.window_height.setValue(1200)
        core_layout.addWidget(self.window_height)

        core_box.setLayout(core_layout)
        main.addWidget(core_box)

        #################

        #control superior
        ctrl = QHBoxLayout()
        ctrl.addWidget(QLabel("Número de bloques radiales:"))
        self.n = QSpinBox()
        self.n.setRange(1, 30)
        self.n.valueChanged.connect(self.build)
        ctrl.addWidget(self.n)
        main.addLayout(ctrl)

        #Control horizontal
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.hlayout = QHBoxLayout()
        self.hlayout.setAlignment(Qt.AlignLeft)
        self.container.setLayout(self.hlayout)
        self.scroll.setWidget(self.container)
        main.addWidget(self.scroll)

        #botón exportar
        btn = QPushButton("Exportar configuración")
        btn.clicked.connect(self.export)
        main.addWidget(btn)

        self.setLayout(main)
        self.blocks = []
        self.n.setValue(5)

    def collect_state(self):
        return [b.get_data() for b in self.blocks]

    def build(self):
        old_data = self.collect_state()

        for b in self.blocks:
            b.deleteLater()
        self.blocks.clear()

        for i in range(self.n.value()):
            block = RadialBlock(i)
            block.setMinimumWidth(160)

            if i < len(old_data):
                block.set_data(old_data[i])

            self.blocks.append(block)
            self.hlayout.addWidget(block)

    def export(self):
        model = {
            "core": {
                "window_diameter": self.core_diameter.value(),
                "window_height": self.window_height.value()
            },
            "radial_blocks": []
        }

        for block in self.blocks:
            model["radial_blocks"].append(block.get_data())

        print("=== MODELO COMPLETO ===")
        print(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())