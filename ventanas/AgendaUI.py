# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agenda.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Agenda(object):
    def setupUi(self, Agenda):
        Agenda.setObjectName("Agenda")
        Agenda.resize(274, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/icono"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Agenda.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Agenda)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        Agenda.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Agenda)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 274, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        Agenda.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(Agenda)
        self.toolBar.setObjectName("toolBar")
        Agenda.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(Agenda)
        self.statusBar.setObjectName("statusBar")
        Agenda.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Agenda)
        QtCore.QMetaObject.connectSlotsByName(Agenda)

    def retranslateUi(self, Agenda):
        _translate = QtCore.QCoreApplication.translate
        Agenda.setWindowTitle(_translate("Agenda", "MainWindow"))
        self.menuFile.setTitle(_translate("Agenda", "File"))
        self.toolBar.setWindowTitle(_translate("Agenda", "toolBar"))

import resource_rc
