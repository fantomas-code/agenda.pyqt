# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------
#  Programa: Agenda
# ------------------------------------------------------------------------
# Fecha: 12/12/2016
# ------------------------------------------------------------------------

# importamos las librerias a ocupar
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# importamos la pantalla
from pantalla import agenda


# clase heredada de QMainWindow(constructor de ventanas)
class Principal(QMainWindow):
    # Metodo cinstructor de clase
    def __init__(self, parent=None):
        # Iniciar el objeto QMainWindow
        QMainWindow.__init__(self, parent)
        # cargar la configuracion del archivo ui en el objeto
        self.ui = agenda.Ui_MainWindow()
        self.ui.setupUi(self)


# instancia para iniciar una plicacíon
app = QApplication(sys.argv)
# crear un objeto de la clase
ventana = Principal()
# mostrar la ventana
ventana.show()
# ejecutamos la aplicacion
sys.exit(app.exec())

