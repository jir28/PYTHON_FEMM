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

    def clear(self):
        while self.dynamic.count():
            item = self.dynamic.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def update_fields(self, kind):
        self.clear()

        if kind == "Cilindro":
            lbl = QLabel("Espesor (mm)")
            self.e = QDoubleSpinBox()
            self.e.setRange(0.5, 50)
            self.dynamic.addWidget(lbl)
            self.dynamic.addWidget(self.e)

        else:
            lbl1 = QLabel("Altura axial (mm)")
            self.h = QDoubleSpinBox()
            self.h.setRange(10, 5000)

            lbl2 = QLabel("Espesor radial (mm)")
            self.e = QDoubleSpinBox()
            self.e.setRange(5, 500)

            lbl3 = QLabel("Tensión (kV)")
            self.v = QDoubleSpinBox()
            self.v.setRange(0.1, 10000)

            lbl4 = QLabel("Aislamiento conductor")
            self.insulation = QComboBox()
            self.insulation.addItems([
                "Papel Kraft",
                "Cordex",
            ])


            self.dynamic.addWidget(lbl1)
            self.dynamic.addWidget(self.h)
            self.dynamic.addWidget(lbl2)
            self.dynamic.addWidget(self.e)
            self.dynamic.addWidget(lbl3)
            self.dynamic.addWidget(self.v)
            self.dynamic.addWidget(lbl4)
            self.dynamic.addWidget(self.insulation)

    def get_data(self):
        if self.type_combo.currentText() == "Cilindro":
            return {
                "tipo": "cilindro",
                "espesor": self.e.value()
            }
        else:
            return {
                "tipo": "devanado",
                "altura": self.h.value(),
                "espesor": self.e.value(),
                "tension": self.v.value()
            }


#ventana principal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuración Radial de Devanados")
        self.resize(1000, 350)

        main = QVBoxLayout()

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

    def build(self):
        for b in self.blocks:
            b.deleteLater()
        self.blocks.clear()

        for i in range(self.n.value()):
            block = RadialBlock(i)
            block.setMinimumWidth(140)
            self.blocks.append(block)
            self.hlayout.addWidget(block)

    def export(self):
        data = [b.get_data() for b in self.blocks]
        print("=== PERFIL RADIAL ===")
        for i, d in enumerate(data, 1):
            print(f"Bloque {i}: {d}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())