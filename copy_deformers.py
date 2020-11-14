import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat

# --------------------------------------------------
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]


# --------------------------------------------------
# CLASS
class CopyDeformers():
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__), "ui",
                              TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        self.wgUtil.copyBtn.clicked.connect(self.press_copy)
        self.wgUtil.wiki.triggered.connect(self.press_wiki)

        # CheckBox
        self.wgUtil.selectAllCheckBox.toggled.connect(self.select_all)

        # LineEdits
        self.wgUtil.copyFromLineEdit.setText('geo 1')
        self.wgUtil.copyToLineEdit.setText('geo 2')

        # SHOW the UI
        self.wgUtil.show()

    # ----------------------------------------------------------------
    # PRESS
    def press_copy(self):
        copy_from = self.wgUtil.copyFromLineEdit.text()
        copy_to = self.wgUtil.copyToLineEdit.text()
        # for checkbox in ['skinClusterCheckBox', 'BlendshapesCheckBox',
        #          'LatticeCheckBox', 'DeltaMushCheckBox']:
        #     if wgUtil.checkbox.isChecked() == True:
        print("deformer has been copied from {} to {}!".format(copy_from, copy_to))

    def press_wiki(self):
        webbrowser.open("https://github.com/farahkahil/ui_assignment/blob/main/README.txt")

    def select_all(self):
        # for checkbox in ['skinClusterCheckBox', 'BlendshapesCheckBox',
        #                  'LatticeCheckBox', 'DeltaMushCheckBox']:
        #     self.wgUtil.checkbox.setChecked(True)
        self.wgUtil.skinClusterCheckBox.setChecked(True)
        self.wgUtil.BlendshapesCheckBox.setChecked(True)
        self.wgUtil.LatticeCheckBox.setChecked(True)
        self.wgUtil.DeltaMushCheckBox.setChecked(True)


# *******************************************************************
# START
def start():
    app = QtWidgets.QApplication(sys.argv)
    classVar = CopyDeformers()
    app.exec_()


start()
