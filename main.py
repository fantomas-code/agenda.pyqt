#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSystemTrayIcon

from DiaryMainWindow import DiaryMainWindow


def app():
    app = QApplication(sys.argv)
    app.setApplicationName('Diary')
    app.setApplicationDisplayName('Diary')
    app.setOrganizationName('Diary')
    app.setOrganizationDomain('Diary.com')
    app.setApplicationVersion('0.1')

    #
    # if not QSystemTrayIcon.isSystemTrayAvailable():
    #     QMessageBox.critical(None, "Systray",
    #                                "I couldn't detect any system tray on this system.")
    #     sys.exit(1)
    #
    # QApplication.setQuitOnLastWindowClosed(False)

    w = DiaryMainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app()