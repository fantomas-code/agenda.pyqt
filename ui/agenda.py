# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QStatusBar

import resource_rc


class AgendaWin(QMainWindow):
    """
      Class documentation goes here.
      """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(AgendaWin, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):

        self.resize(274, 271)
        self._icon = QtGui.QIcon()
        self._icon.addPixmap(
            QtGui.QPixmap(":/imagenes/icono"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.setWindowIcon(self._icon)
        self.centralWidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.listView = QListView(self.centralWidget)
        self.verticalLayout.addWidget(self.listView)
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(self)
        self.menuFile = QMenu(self.menuBar)
        self.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFile.menuAction())
