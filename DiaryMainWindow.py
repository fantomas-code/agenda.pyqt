# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QTextEdit

from Ui_DiaryMainWindow import Ui_MainWindow


class DiaryMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DiaryMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.createActions()
        self.createTrayIcon()
        self.setIcon(":bad")
        self.trayIcon.setVisible(True)
        self.trayIcon.show()

        self.trayIcon.messageClicked.connect(self.messageClicked)
        self.trayIcon.activated.connect(self.iconActivated)

        now = QDateTime.currentDateTime()
        next_ = QDateTime.currentDateTime().addSecs(10)
        timer = QTimer(self)
        timer.timeout.connect(self.alert)
        timer.start(now.msecsTo(next_))

        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)

    def setIcon(self, icon):
        self.trayIcon.setIcon(QIcon(icon))
        self.setWindowIcon(QIcon(icon))
        # self.trayIcon.setToolTip(icon)

    def alert(self):
        self.showMessage()

    def setVisible(self, visible):
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(DiaryMainWindow, self).setVisible(visible)

    def createActions(self):
        self.minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        self.maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        self.restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        self.quitAction = QAction("&Quit", self, triggered=qApp.quit)

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            QMessageBox.information(self, "Systray",
                                          "The program will keep running in the system tray. To "
                                          "terminate the program, choose <b>Quit</b> in the "
                                          "context menu of the system tray entry.")
            self.hide()
            event.ignore()

    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def showMessage(self):
        icon = QSystemTrayIcon.MessageIcon(QSystemTrayIcon.Information)
        self.trayIcon.showMessage("test", QDateTime.currentDateTime().toString(), icon, 10*1000)
        item = QStandardItem(QDateTime.currentDateTime().toString())
        self.model.appendRow(item)

    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            print("testing")
        elif reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()

    def messageClicked(self):
        QMessageBox.information(None, "Systray",
                                      "Sorry, I already gave what help I could.\nMaybe you should "
                                      "try asking a human?")