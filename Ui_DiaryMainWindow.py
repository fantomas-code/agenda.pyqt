# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/qhipa/Documents/Projects/agenda.pyqt/DiaryMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(274, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/diary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 274, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew_Task = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Task.setIcon(icon1)
        self.actionNew_Task.setObjectName("actionNew_Task")
        self.actionEdit_Task = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/edit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Task.setIcon(icon2)
        self.actionEdit_Task.setObjectName("actionEdit_Task")
        self.menuFile.addAction(self.actionNew_Task)
        self.menuFile.addAction(self.actionEdit_Task)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionNew_Task)
        self.toolBar.addAction(self.actionEdit_Task)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Task.setText(_translate("MainWindow", "New Task"))
        self.actionEdit_Task.setText(_translate("MainWindow", "Edit Task"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

