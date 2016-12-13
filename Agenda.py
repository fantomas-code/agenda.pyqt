# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtGui

from PyQt5.QtWidgets import QMainWindow

from ventanas.AgendaUI import Ui_Agenda


class Agenda(QMainWindow, Ui_Agenda):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Agenda, self).__init__(parent)
        self.setupUi(self)

import resource_rc