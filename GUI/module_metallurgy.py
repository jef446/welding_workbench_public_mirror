# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

class Ui_moduleMeta(object):
    def setupUi(self, moduleMeta):
        moduleMeta.setObjectName("moduleMeta")
        moduleMeta.resize(659, 655)
        self.GS_label = QtWidgets.QLabel(moduleMeta)
        self.GS_label.setGeometry(QtCore.QRect(20, 140, 121, 17))
        self.GS_label.setObjectName("GS_label")
        self.CR_label = QtWidgets.QLabel(moduleMeta)
        self.CR_label.setGeometry(QtCore.QRect(20, 180, 211, 17))
        self.CR_label.setObjectName("CR_label")
        self.AE13_label = QtWidgets.QLabel(moduleMeta)
        self.AE13_label.setGeometry(QtCore.QRect(20, 470, 101, 17))
        self.AE13_label.setObjectName("AE13_label")
        self.Material_label = QtWidgets.QLabel(moduleMeta)
        self.Material_label.setGeometry(QtCore.QRect(20, 290, 71, 17))
        self.Material_label.setObjectName("Material_label")
        self.Finish = QtWidgets.QPushButton(moduleMeta)
        self.Finish.setGeometry(QtCore.QRect(540, 610, 89, 25))
        self.Finish.setObjectName("Finish")
        self.CR = QtWidgets.QTextEdit(moduleMeta)
        self.CR.setGeometry(QtCore.QRect(280, 180, 331, 51))
        self.CR.setObjectName("CR")
        self.T_End = QtWidgets.QTextEdit(moduleMeta)
        self.T_End.setGeometry(QtCore.QRect(280, 90, 51, 31))
        self.T_End.setObjectName("T_End")
        self.CCT = QtWidgets.QCheckBox(moduleMeta)
        self.CCT.setGeometry(QtCore.QRect(80, 570, 92, 23))
        self.CCT.setObjectName("CCT")
        self.AustT_label = QtWidgets.QLabel(moduleMeta)
        self.AustT_label.setGeometry(QtCore.QRect(20, 60, 281, 17))
        self.AustT_label.setObjectName("AustT_label")
        self.EndT_label = QtWidgets.QLabel(moduleMeta)
        self.EndT_label.setGeometry(QtCore.QRect(20, 100, 191, 17))
        self.EndT_label.setObjectName("EndT_label")
        self.USR = QtWidgets.QTextEdit(moduleMeta)
        self.USR.setGeometry(QtCore.QRect(280, 400, 331, 31))
        self.USR.setObjectName("USR")
        self.GS = QtWidgets.QTextEdit(moduleMeta)
        self.GS.setGeometry(QtCore.QRect(280, 130, 51, 31))
        self.GS.setObjectName("GS")
        self.Inputs_label = QtWidgets.QLabel(moduleMeta)
        self.Inputs_label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Inputs_label.setFont(font)
        self.Inputs_label.setObjectName("Inputs_label")
        self.AE13 = QtWidgets.QComboBox(moduleMeta)
        self.AE13.setGeometry(QtCore.QRect(280, 460, 121, 25))
        self.AE13.setObjectName("AE13")
        self.AE13.addItem("")
        self.AE13.addItem("")
        self.AE13.addItem("")
        self.Plots_explanation = QtWidgets.QLabel(moduleMeta)
        self.Plots_explanation.setGeometry(QtCore.QRect(20, 540, 281, 17))
        self.Plots_explanation.setObjectName("Plots_explanation")
        self.GGM = QtWidgets.QComboBox(moduleMeta)
        self.GGM.setGeometry(QtCore.QRect(280, 240, 121, 25))
        self.GGM.setObjectName("GGM")
        self.GGM.addItem("")
        self.GGM.addItem("")
        self.GGM.addItem("")
        self.TTT = QtWidgets.QCheckBox(moduleMeta)
        self.TTT.setGeometry(QtCore.QRect(310, 570, 92, 23))
        self.TTT.setChecked(True)
        self.TTT.setObjectName("TTT")
        self.Plots_label = QtWidgets.QLabel(moduleMeta)
        self.Plots_label.setGeometry(QtCore.QRect(20, 510, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Plots_label.setFont(font)
        self.Plots_label.setObjectName("Plots_label")
        self.Material_label_2 = QtWidgets.QLabel(moduleMeta)
        self.Material_label_2.setGeometry(QtCore.QRect(90, 320, 381, 71))
        self.Material_label_2.setAcceptDrops(False)
        self.Material_label_2.setObjectName("Material_label_2")
        self.T_Aust = QtWidgets.QTextEdit(moduleMeta)
        self.T_Aust.setGeometry(QtCore.QRect(280, 50, 51, 31))
        self.T_Aust.setTextInteractionFlags(QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByKeyboard)
        self.T_Aust.setObjectName("T_Aust")
        self.Material_label_3 = QtWidgets.QLabel(moduleMeta)
        self.Material_label_3.setGeometry(QtCore.QRect(90, 410, 161, 16))
        self.Material_label_3.setAcceptDrops(False)
        self.Material_label_3.setObjectName("Material_label_3")
        self.Material = QtWidgets.QComboBox(moduleMeta)
        self.Material.setGeometry(QtCore.QRect(280, 280, 121, 25))
        self.Material.setObjectName("Material")
        self.Material.addItem("")
        self.Material.addItem("")
        self.Material.addItem("")
        self.GGM_label = QtWidgets.QLabel(moduleMeta)
        self.GGM_label.setGeometry(QtCore.QRect(20, 250, 151, 17))
        self.GGM_label.setObjectName("GGM_label")

        self.retranslateUi(moduleMeta)
        self.GGM.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(moduleMeta)

    def retranslateUi(self, moduleMeta):
        _translate = QtCore.QCoreApplication.translate
        moduleMeta.setWindowTitle(_translate("moduleMeta", "moduleMeta"))
        self.GS_label.setText(_translate("moduleMeta", "Grain size (mm):"))
        self.CR_label.setText(_translate("moduleMeta", "Cooling rates  (0.1, 0.2, 0.3 etc):"))
        self.AE13_label.setText(_translate("moduleMeta", "AE13 method:"))
        self.Material_label.setText(_translate("moduleMeta", "Material:"))
        self.Finish.setText(_translate("moduleMeta", "Submit"))
        self.T_End.setPlaceholderText(_translate("moduleMeta", "488"))
        self.CCT.setText(_translate("moduleMeta", "CCT"))
        self.AustT_label.setText(_translate("moduleMeta", "Austenisation temperature (Celsius):"))
        self.EndT_label.setText(_translate("moduleMeta", "End temperature (Celsius):"))
        self.Inputs_label.setText(_translate("moduleMeta", "Inputs:"))
        self.AE13.setItemText(0, _translate("moduleMeta", "Grange"))
        self.AE13.setItemText(1, _translate("moduleMeta", "Andrews"))
        self.AE13.setItemText(2, _translate("moduleMeta", "Eldis"))
        self.Plots_explanation.setText(_translate("moduleMeta", "Selected which plots you would like to be produced"))
        self.GGM.setItemText(0, _translate("moduleMeta", "IKAWA"))
        self.GGM.setItemText(1, _translate("moduleMeta", "CONSTANT"))
        self.GGM.setItemText(2, _translate("moduleMeta", "TWORATE"))
        self.TTT.setText(_translate("moduleMeta", "TTT"))
        self.Plots_label.setText(_translate("moduleMeta", "Plots:"))
        self.Material_label_2.setText(_translate("moduleMeta", "<html><head/><body><p>User-defined Material:<br/>(Your composition must be inputted in this format and<br/>contain these chemicals in the following order: <br/>[C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co])</p></body></html>"))
        self.T_Aust.setHtml(_translate("moduleMeta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.T_Aust.setPlaceholderText(_translate("moduleMeta", "400"))
        self.Material_label_3.setText(_translate("moduleMeta", "<html><head/><body><p>User-defined Material:</p></body></html>"))
        self.Material.setItemText(0, _translate("moduleMeta", "SA508"))
        self.Material.setItemText(1, _translate("moduleMeta", "4140"))
        self.Material.setItemText(2, _translate("moduleMeta", "16MND5"))
        self.GGM_label.setText(_translate("moduleMeta", "Grain growth method:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    moduleMeta = QtWidgets.QWidget()
    ui = Ui_moduleMeta()
    ui.setupUi(moduleMeta)
    moduleMeta.show()
    sys.exit(app.exec_())
