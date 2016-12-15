#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QApplication

from ui.agenda import AgendaWin


def app():
    app = QApplication(sys.argv)
    app.setApplicationName('Agenda')
    app.setApplicationDisplayName('Agenda')
    app.setOrganizationName('Agenda')
    app.setOrganizationDomain('Agenda.com')
    app.setApplicationVersion('0.1')
    w = AgendaWin()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()
