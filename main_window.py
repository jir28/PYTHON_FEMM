
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel, QSpinBox,
    QDoubleSpinBox, QGroupBox, QScrollArea
)
from PySide6.QtCore import Qt
import sys

class ElementWidget(QGroupBox):
    def __init__(self, index):
        super().__init__(f"Elemento {index}")
        self.index = index
        self.layout = QVBoxLayout()

        #tipo de elemento
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Tipo:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Devanado", "Cilindro"])
        self.type_combo.currentTextChanged.connect(self.update_fields)
        type_layout.addWidget(self.type_combo)
        self.layout.addLayout(type_layout)

        #contenedor dinamico
        self.dynamic_layout = QVBoxLayout()
        self.layout.addLayout(self.dynamic_layout)

        self.setLayout(self.layout)
        self.update_fields("Devanado")

    def clear_dynamic(self):
        while self.dynamic_layout.count():
            item = self.dynamic_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def update_fields(self, element_type):
        self.clear_dynamic()

        if element_type == "Devanado":
            self.add_devanado_fields()
        else:
            self.add_cilindro_fields()


    #Para devanados

    def add_devanado_fields(self):
        self.dynamic_layout.addWidget(QLabel("Altura axial (mm):"))
        self.h_axial = QDoubleSpinBox()
        self.h_axial.setRange(1, 5000)
        self.dynamic_layout.addWidget(self.h_axial)

        self.dynamic_layout.addWidget(QLabel("Espesor radial (mm):"))
        self.e_radial = QDoubleSpinBox()
        self.e_radial.setRange(1, 500)
        self.dynamic_layout.addWidget(self.e_radial)

        self.dynamic_layout.addWidget(QLabel("Tensión (kV):"))
        self.voltage = QDoubleSpinBox()
        self.voltage.setRange(0.1, 10000)
        self.dynamic_layout.addWidget(self.voltage)

        self.dynamic_layout.addWidget(QLabel("Tipo de aislamiento:"))
        self.insulation = QComboBox()
        self.insulation.addItems([
            "Papel Kraft",
            "Cordex",
        ])
        self.dynamic_layout.addWidget(self.insulation)

    #Para cilindros

    def add_cilindro_fields(self):
        self.dynamic_layout.addWidget(QLabel("Altura axial (mm):"))
        self.h_cyl = QDoubleSpinBox()
        self.h_cyl.setRange(1, 5000)
        self.dynamic_layout.addWidget(self.h_cyl)

        self.dynamic_layout.addWidget(QLabel("Espesor (mm):"))
        self.e_cyl = QDoubleSpinBox()
        self.e_cyl.setRange(0.5, 20)
        self.dynamic_layout.addWidget(self.e_cyl)


    #exportar datos

    def get_data(self):
        if self.type_combo.currentText() == "Devanado":
            return {
                "tipo": "devanado",
                "h_axial": self.h_axial.value(),
                "e_radial": self.e_radial.value(),
                "tension_kV": self.voltage.value(),
                "aislamiento": self.insulation.currentText()
            }
        else:
            return {
                "tipo": "cilindro",
                "h": self.h_cyl.value(),
                "e": self.e_cyl.value()
            }


#ventana principal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estudio Devanados WEG")
        self.resize(600, 900)

        self.layout = QVBoxLayout()

        #número de elementos
        n_layout = QHBoxLayout()
        n_layout.addWidget(QLabel("Número de elementos:"))
        self.n_spin = QSpinBox()
        self.n_spin.setRange(1, 20)
        self.n_spin.valueChanged.connect(self.build_elements)
        n_layout.addWidget(self.n_spin)
        self.layout.addLayout(n_layout)

        #scroll  elementos
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container_layout = QVBoxLayout()
        self.container.setLayout(self.container_layout)
        self.scroll.setWidget(self.container)
        self.layout.addWidget(self.scroll)

        #botón exportar
        self.export_btn = QPushButton("Exportar datos")
        self.export_btn.clicked.connect(self.export_data)
        self.layout.addWidget(self.export_btn)

        self.setLayout(self.layout)

        self.elements = []
        self.n_spin.setValue(1)

    def build_elements(self):
        for el in self.elements:
            el.deleteLater()
        self.elements.clear()

        for i in range(self.n_spin.value()):
            el = ElementWidget(i + 1)
            self.elements.append(el)
            self.container_layout.addWidget(el)

        self.container_layout.addStretch()

    def export_data(self):
        data = [el.get_data() for el in self.elements]
        print(" CONFIGURACIÓN DEL TRAFO ")
        for i, d in enumerate(data, 1):
            print(f"Elemento {i}: {d}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

