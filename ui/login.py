# -*- coding: utf-8 -*-
import sys, os

# Optimizado por sabroso ----

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):

	def __init__(self):
		super(Main, self).__init__()
		self.setWindowTitle('Iniciar sesion !!!!')
		# self.setWindowIcon(QIcon('img/gato.jpg'))
		self.resize(400, 228)
		self.setFixedSize(400, 228)

		# Main.setObjectName("Main")
		# Main.resize(400, 228)
		# Main.setMaximumSize(QSize(400, 228))
		font = QFont()
		font.setFamily("NSimSun")
		font.setPointSize(18)
		font.setItalic(True)
		self.setFont(font)

		self.grilla = QWidget()
		self.grilla.setObjectName("grilla")


		self.titulo = QLabel(self.grilla)
		self.titulo.setGeometry(QRect(30, 10, 341, 31))
		self.titulo.setFrameShape(QFrame.Box)
		self.titulo.setTextFormat(Qt.AutoText)
		self.titulo.setAlignment(Qt.AlignCenter)
		self.titulo.setWordWrap(True)
		self.titulo.setOpenExternalLinks(True)
		self.titulo.setObjectName("titulo")

		self.cor = QLabel(self.grilla)
		self.cor.setGeometry(QRect(20, 60, 91, 41))
		self.cor.setObjectName("cor")

		self.con = QLabel(self.grilla)
		self.con.setGeometry(QRect(20, 120, 141, 41))
		self.con.setObjectName("con")

		self.lincor = QLineEdit(self.grilla)
		self.lincor.setGeometry(QRect(160, 60, 211, 31))
		self.lincor.setObjectName("lincor")

		self.lincon = QLineEdit(self.grilla)
		self.lincon.setGeometry(QRect(160, 130, 211, 31))
		self.lincon.setEchoMode(QLineEdit.Password)
		self.lincon.setObjectName("lincon")

		self.btent = QPushButton(self.grilla)
		self.btent.setGeometry(QRect(30, 180, 161, 41))
		self.btent.setCursor(QCursor(Qt.PointingHandCursor))
		self.btent.setObjectName("btent")

		self.btcanc = QPushButton(self.grilla)
		self.btcanc.setGeometry(QRect(200, 180, 161, 41))
		self.btcanc.setCursor(QCursor(Qt.PointingHandCursor))
		self.btcanc.setObjectName("btcanc")

		self.btcanc.clicked.connect(self.salir)

		self.titulo.setText(("Agenda PyQt .."))
		self.cor.setText(("Correo:"))
		self.con.setText(("Contraseña:"))
		self.btent.setText(("Entrar"))
		self.btcanc.setText(("Cancelar"))

		self.setCentralWidget(self.grilla)

	def salir(self):
		sys.exit()

if __name__ == "__main__":

	app = QApplication(sys.argv)
	ap = Main()
	ap.show()
	sys.exit(app.exec_())

