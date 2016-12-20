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
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle('Iniciar sesion !!!!')
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        # self.setWindowIcon(QIcon('img/gato.jpg'))
        # font = QtGui.QFont()
        # font.setFamily("NSimSun")
        # font.setPointSize(18)
        # font.setItalic(True)
        # self.setFont(font)

        self.grilla = QtWidgets.QVBoxLayout(self)

        self.titulo = QtWidgets.QLabel(self)
        self.titulo.setFrameShape(QtWidgets.QFrame.Box)
        self.titulo.setTextFormat(QtCore.Qt.AutoText)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(True)
        self.titulo.setOpenExternalLinks(True)

        self.grilla.addWidget(self.titulo)

        self.form = QtWidgets.QFormLayout()
        self.grilla.addLayout(self.form)

        self.correoLB = QtWidgets.QLabel("Correo: ", self)
        self.correoLE = QtWidgets.QLineEdit(self)
        self.correoLE.setValidator(EmailValidator(self.correoLE))

        self.correoLE.textChanged[str].connect(self.habilitarAceptar)

        self.form.addRow(self.correoLB, self.correoLE)

        self.contraseniaLB = QtWidgets.QLabel("Contraseña: ", self)
        self.contraseniaLE = QtWidgets.QLineEdit(self)
        self.contraseniaLE.setEchoMode(QtWidgets.QLineEdit.Password)

        self.form.addRow(self.contraseniaLB, self.contraseniaLE)
        self.titulo.setText("Agenda PyQt ..")

        self.layout_botones = QtWidgets.QHBoxLayout()

        self.aceptarBtn = QtWidgets.QPushButton("Aceptar", self)
        self.aceptarBtn.setEnabled(False)
        self.cancelarBtn = QtWidgets.QPushButton("Cancelar", self)

        self.layout_botones.addWidget(self.aceptarBtn)
        self.layout_botones.addWidget(self.cancelarBtn)

        self.grilla.addLayout(self.layout_botones)
        self.aceptarBtn.clicked.connect(self.accept)
        self.cancelarBtn.clicked.connect(self.reject)

        self.titulo.setFixedSize(QtCore.QSize(self.size().width(), 60))

        self.setFixedSize(self.sizeHint())

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
