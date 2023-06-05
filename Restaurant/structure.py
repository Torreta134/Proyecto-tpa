import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStackedLayout, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("☺")
        self.setMinimumSize(400, 200)

        # Constructor
        container0 = QWidget()
        container1 = QWidget()
        container2 = QWidget()
        container3 = QWidget()
        container4 = QWidget()
        login = QVBoxLayout(container0)
        mesas = QVBoxLayout(container1)
        garzon = QVBoxLayout(container2)
        chef = QVBoxLayout(container3)
        pantalla_principal = QVBoxLayout(container4)

        # Layout y reacción
        self.main_box = QStackedLayout()

        pPrincipal = QVBoxLayout()
        pPrincipal_button0 = QPushButton("Ingresar")
        pPrincipal_button1 = QPushButton("Mesas")
        pPrincipal_button2 = QPushButton("garzon")
        pPrincipal_button3 = QPushButton("chef")
        pPrincipal.addWidget(pPrincipal_button0)
        pPrincipal.addWidget(pPrincipal_button1)
        pPrincipal.addWidget(pPrincipal_button2)
        pPrincipal.addWidget(pPrincipal_button3)

        pPrincipal_button0.clicked.connect(self.ir_a)
        pPrincipal_button1.clicked.connect(self.ir_a)
        pPrincipal_button2.clicked.connect(self.ir_a)
        pPrincipal_button3.clicked.connect(self.ir_a)

        pantalla_principal.addWidget(QLabel("Pantalla principal"))
        pantalla_principal.addLayout(pPrincipal)

        login_title = QLabel("Login")
        login_label = QLabel("Nombre de usuario: ")
        login_entry = QLineEdit("")
        login_form = QGridLayout()
        login_form.addWidget(login_label, 0, 0)
        login_form.addWidget(login_entry, 0, 1)

        login.addWidget(login_title)
        login.addLayout(login_form)

        # Final
        self.main_box.addWidget(container4)
        self.main_box.addWidget(container0)
        self.main_box.addWidget(container1)
        self.main_box.addWidget(container2)
        self.main_box.addWidget(container3)

        my_window = QWidget()
        my_window.setLayout(self.main_box)
        self.setCentralWidget(my_window)
        self.setDarkMode(my_window)

    def ir_pPrincipal(self):
        self.main_box.setCurrentIndex(0)

    def ir_a(self, indice: int):
        if 1 <= indice <= 4:
            self.main_box.setCurrentIndex(indice)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
