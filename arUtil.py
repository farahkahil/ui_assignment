import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat
    
    
#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]

#*******************************************************************
# CLASS
class ArUtil():
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__), "ui",
                             TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        self.wgUtil.btnAccept.clicked.connect(self.press_accept)
        self.wgUtil.btnHelp.clicked.connect(self.press_help)

        # SHOW the UI
        self.wgUtil.show()



    #************************************************************
    # PRESS
    def press_accept(self):
        print("You accepted this process!")

    def press_help(self):
        webbrowser.open("https://www.alexanderrichtertd.com")


#*******************************************************************
# START
def start():
    app = QtWidgets.QApplication(sys.argv)
    classVar = ArUtil()
    app.exec_()

start()