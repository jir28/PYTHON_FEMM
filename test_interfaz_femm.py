# Interfaz PySide6 estilo "layout radial" para transformadores
# Inspirada en hojas de cálculo eléctricas reales (cilindros + devanados en secuencia)
# Objetivo: representar visualmente espesores radiales y tipos de elemento

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel, QSpinBox,
    QDoubleSpinBox, QFrame, QScrollArea
)
from PySide6.QtCore import Qt
import sys

# -----------------------------
# Bloque radial (una columna)
# -----------------------------
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
            self.v.setRange(0.1, 1000)

            self.dynamic.addWidget(lbl1)
            self.dynamic.addWidget(self.h)
            self.dynamic.addWidget(lbl2)
            self.dynamic.addWidget(self.e)
            self.dynamic.addWidget(lbl3)
            self.dynamic.addWidget(self.v)

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

# -----------------------------
# Ventana principal
# -----------------------------
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuración Radial de Devanados")
        self.resize(1100, 450)

        main = QVBoxLayout()

        # -----------------------------
        # Datos globales del núcleo
        # -----------------------------
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

        # -----------------------------
        # Control de bloques radiales
        # -----------------------------
        ctrl = QHBoxLayout()
        ctrl.addWidget(QLabel("Número de bloques radiales:"))
        self.n = QSpinBox()
        self.n.setRange(1, 30)
        self.n.valueChanged.connect(self.build)
        ctrl.addWidget(self.n)
        main.addLayout(ctrl)

        # Área horizontal desplazable
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.hlayout = QHBoxLayout()
        self.hlayout.setAlignment(Qt.AlignLeft)
        self.container.setLayout(self.hlayout)
        self.scroll.setWidget(self.container)
        main.addWidget(self.scroll)

        # Botón exportar
        btn = QPushButton("Exportar configuración")
        btn.clicked.connect(self.export)
        main.addWidget(btn)

        self.setLayout(main)

        self.blocks = []
        self.n.setValue(5)
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

# -----------------------------
# Main
# -----------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
