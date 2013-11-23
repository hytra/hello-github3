#!/usr/bin/env python2.5

import sys
from PyQt4 import QtCore, QtGui



class Application(QtGui.QApplication):
    def __init__(self):
        QtGui.QApplication.__init__(self, sys.argv)
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor));

        self.window = QtGui.QWidget()
        self.window.setWindowTitle(self.tr("Hello World"));

        self.button = QtGui.QPushButton(self.tr("Press Me"), self.window)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.button, QtCore.Qt.AlignCenter)
        self.window.setLayout(layout)

        self.connect(self.button, QtCore.SIGNAL('clicked()'),
            self.handlePressed)

        self.window.show()

    def run(self):
        return self.exec_()

    def handlePressed(self):
        QtGui.QMessageBox.information(self.window, 
                                      self.tr("Info"), 
                                      self.tr("Hello World!!!"))
        
if __name__ == "__main__":
    app = Application()
    sys.exit(app.run())
    
