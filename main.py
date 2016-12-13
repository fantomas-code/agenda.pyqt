#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QApplication

from Agenda import Agenda


def app():
    app = QApplication(sys.argv)
    app.setApplicationName('Diary')
    app.setApplicationDisplayName('Diary')
    app.setOrganizationName('Diary')
    app.setOrganizationDomain('Diary.com')
    app.setApplicationVersion('0.1')
    w = Agenda()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()
