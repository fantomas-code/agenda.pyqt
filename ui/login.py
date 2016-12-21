# -*- coding: utf-8 -*-
import sys

# Optimizado por sabroso ----
# Modificado por eyllanesc

from PyQt5 import QtCore, QtGui, QtWidgets


# Esta clase debe ser movida a LIB
class EmailValidator(QtGui.QValidator):
    """
    Validador de correos electrónicos
    """

    def __init__(self, parent=None):
        super(EmailValidator, self).__init__(parent=parent)
        self.m_validMailRegExp = QtCore.QRegExp("\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}\\b")
        self.m_validMailRegExp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.m_validMailRegExp.setPatternSyntax(QtCore.QRegExp.RegExp)
        self.m_intermediateMailRegExp = QtCore.QRegExp("[a-z0-9._%+-]*@?[a-z0-9.-]*\\.?[a-z]*")
        self.m_intermediateMailRegExp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.m_intermediateMailRegExp.setPatternSyntax(QtCore.QRegExp.RegExp)

    def validate(self, text, pos):
        """
        :param text: Texto
        :param pos: Posicion
        :return: retorna una tupla que tiene el estado, el texto modificado y la posicion
        """
        text = self.fixup(text)
        state = QtGui.QValidator.Invalid
        if self.m_validMailRegExp.exactMatch(text):
            state = QtGui.QValidator.Acceptable
        else:
            if self.m_intermediateMailRegExp.exactMatch(text):
                state = QtGui.QValidator.Intermediate
        color = {
            QtGui.QValidator.Acceptable: "#c4df9b",
            QtGui.QValidator.Intermediate: "#fff79a",
            QtGui.QValidator.Invalid: "#f6989d"
        }[state]
        self.parent().setStyleSheet('QLineEdit {background-color: %s}' % color)
        return state, text, pos

    def fixup(self, text):
        """
        :param text: Texto
        :return: Texto modificado
        """
        return text.strip().lower()


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent, QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        self.grilla = QtWidgets.QVBoxLayout(self)

        self.grilla.addItem(QtWidgets.QSpacerItem(20, 40))

        self.imagenLB = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap("../recursos/imagenes/icon.png")
        self.imagenLB.setPixmap(pixmap.scaled(1.1 * pixmap.size()))
        self.imagenLB.setAlignment(QtCore.Qt.AlignCenter)
        self.grilla.addWidget(self.imagenLB)

        self.grilla.addItem(QtWidgets.QSpacerItem(20, 40))

        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("QWidget{background-color: rgb(255, 211, 78);border-bottom-color: rgb(0, 0, 0);\n"
                                 "border-top-width: 10px; border-right-width: 10px; border-bottom-width: 10px;\n"
                                 "border-left-width: 10px;}")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)

        self.tituloLB = QtWidgets.QLabel("<p><span style=\" font-weight:600;\">Iniciar Sesión</span></p>", self.frame)
        self.tituloLB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tituloLB.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.tituloLB)

        self.formLayout = QtWidgets.QFormLayout()

        self.correoLB = QtWidgets.QLabel(" Correo: ", self.frame)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.correoLB)

        self.correoLE = QtWidgets.QLineEdit(self.frame)
        self.correoLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.correoLE)

        self.contraseniaLB = QtWidgets.QLabel(" Contraseña: ", self.frame)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.contraseniaLB)

        self.contraseniaLE = QtWidgets.QLineEdit(self.frame)
        self.contraseniaLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.contraseniaLE)

        self.verticalLayout.addLayout(self.formLayout)

        self.BotonesHorLayout = QtWidgets.QHBoxLayout()

        self.aceptarBtn = QtWidgets.QPushButton("Aceptar", self.frame)
        self.aceptarBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aceptarBtn.setEnabled(False)

        self.cancelarBtn = QtWidgets.QPushButton("Cancelar", self.frame)
        self.cancelarBtn.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.BotonesHorLayout.addWidget(self.aceptarBtn)
        self.BotonesHorLayout.addWidget(self.cancelarBtn)

        self.verticalLayout.addLayout(self.BotonesHorLayout)

        self.grilla.addWidget(self.frame)

        self.correoLE.setValidator(EmailValidator(self.correoLE))

        self.aceptarBtn.clicked.connect(self.accept)
        self.cancelarBtn.clicked.connect(self.reject)
        self.correoLE.textChanged[str].connect(self.habilitarAceptar)

        self.dragPosition = None
        self.addCustomAction()

    def addCustomAction(self):
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.salirAction = QtWidgets.QAction("Salir", self, icon=QtGui.QIcon("../recursos/imagenes/close"),
                                             shortcut="Ctrl+Q", triggered=QtWidgets.qApp.quit)
        self.addAction(self.salirAction)
        self.acercaAction = QtWidgets.QAction("Acerca de Qt", self, icon=QtGui.QIcon("../recursos/imagenes/qt"),
                                              shortcut="Ctrl+A",
                                              triggered=lambda:
                                              QtWidgets.QMessageBox.aboutQt(None, self.tr("Acerca de Qt")))
        self.addAction(self.acercaAction)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def habilitarAceptar(self, text):
        """"
        Habilita el boton de aceptar
        :param text: Texto del correo electrónico
        :return:
        """
        self.aceptarBtn.setEnabled(self.sender().validator().validate(text, 0)[0] == QtGui.QValidator.Acceptable)

    def accept(self):
        """
        Evento que se ejecuta al aceptar
        :return:
        """

        # valores de prueba de correo y contraseña
        correo = 'correo'
        contrasenia = 'contra'

        # Es Valido los datos introducidos
        if self.esValido(correo, contrasenia):
            print("login")
            super(Login, self).accept()
        # No son validos
        else:
            # limpia los datos
            self.limpiar()
            # Se muestra un mensaje mostrando que los datos son incorrectos
            mensaje_error = QtWidgets.QMessageBox(self)
            mensaje_error.setIcon(QtWidgets.QMessageBox.Warning)
            mensaje_error.setWindowTitle("Problemas con las credenciales")

            mensaje_error.setText("No coinciden tu correo o contraseñas")
            mensaje_error.setInformativeText("Verífique que sean correctas")

            # Botones del mensaje
            aceptarBtn = mensaje_error.addButton("Aceptar", QtWidgets.QMessageBox.YesRole)
            cancelarBtn = mensaje_error.addButton("Cancelar", QtWidgets.QMessageBox.NoRole)

            # Se muestra el mensaje
            mensaje_error.exec_()
            if mensaje_error.clickedButton() == aceptarBtn:
                print("Aceptar")

            if mensaje_error.clickedButton() == cancelarBtn:
                print("Cancelar")

    def esValido(self, correo, contrasenia):
        """
        :param correo: correo electrónico
        :param contrasenia: contraseña
        :return: valida el correo y la contraseña
        """
        return (self.correoLE.text() == correo) and \
               (self.contraseniaLE.text() == contrasenia)

    def limpiar(self):
        """
        Limpia los textos de los LineEdit
        :return:
        """
        self.correoLE.clear()
        self.contraseniaLE.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ap = Login()
    ap.show()
    sys.exit(app.exec_())
