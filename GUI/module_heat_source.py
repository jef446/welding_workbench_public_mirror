"""
author: EDF Energy R&D UKC
"""
import sys
import os
import subprocess
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow

class UiModuleHeatSource(object):
    """
    heat source gui module
    """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 439)
        self.type_label = QtWidgets.QLabel(Form)
        self.type_label.setGeometry(QtCore.QRect(10, 10, 141, 18))
        self.type_label.setObjectName("type_label")
        self.type = QtWidgets.QComboBox(Form)
        self.type.setGeometry(QtCore.QRect(160, 10, 121, 26))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 60, 441, 241))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 321, 141))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.home)
        self.goldak = QtWidgets.QWidget()
        self.goldak.setObjectName("goldak")
        self.goldak_a = QtWidgets.QTextEdit(self.goldak)
        self.goldak_a.setGeometry(QtCore.QRect(40, 40, 104, 31))
        self.goldak_a.setObjectName("goldak_a")
        self.goldak_cr = QtWidgets.QTextEdit(self.goldak)
        self.goldak_cr.setGeometry(QtCore.QRect(40, 140, 104, 31))
        self.goldak_cr.setObjectName("goldak_cr")
        self.goldak_cr_label = QtWidgets.QLabel(self.goldak)
        self.goldak_cr_label.setGeometry(QtCore.QRect(0, 150, 74, 18))
        self.goldak_cr_label.setObjectName("goldak_cr_label")
        self.goldak_b_label = QtWidgets.QLabel(self.goldak)
        self.goldak_b_label.setGeometry(QtCore.QRect(0, 100, 74, 18))
        self.goldak_b_label.setObjectName("goldak_b_label")
        self.goldak_measurement = QtWidgets.QLabel(self.goldak)
        self.goldak_measurement.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.goldak_measurement.setObjectName("goldak_measurement")
        self.goldak_cf = QtWidgets.QTextEdit(self.goldak)
        self.goldak_cf.setGeometry(QtCore.QRect(40, 190, 104, 31))
        self.goldak_cf.setObjectName("goldak_cf")
        self.goldak_image = QtWidgets.QLabel(self.goldak)
        self.goldak_image.setGeometry(QtCore.QRect(170, 0, 251, 201))
        self.goldak_image.setText("")
        self.goldak_image.setPixmap(QtGui.QPixmap("Goldak.png"))
        self.goldak_image.setScaledContents(True)
        self.goldak_image.setObjectName("goldak_image")
        self.goldak_a_label = QtWidgets.QLabel(self.goldak)
        self.goldak_a_label.setGeometry(QtCore.QRect(0, 50, 74, 18))
        self.goldak_a_label.setObjectName("goldak_a_label")
        self.goldak_b = QtWidgets.QTextEdit(self.goldak)
        self.goldak_b.setGeometry(QtCore.QRect(40, 90, 104, 31))
        self.goldak_b.setObjectName("goldak_b")
        self.goldak_cf_label = QtWidgets.QLabel(self.goldak)
        self.goldak_cf_label.setGeometry(QtCore.QRect(0, 200, 74, 18))
        self.goldak_cf_label.setObjectName("goldak_cf_label")
        self.z_direction_1 = QtWidgets.QLabel(self.goldak)
        self.z_direction_1.setGeometry(QtCore.QRect(190, 210, 201, 18))
        self.z_direction_1.setObjectName("z_direction_1")
        self.stackedWidget.addWidget(self.goldak)
        self.ellipsoid = QtWidgets.QWidget()
        self.ellipsoid.setObjectName("ellipsoid")
        self.ellipsoid_a = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_a.setGeometry(QtCore.QRect(40, 40, 104, 31))
        self.ellipsoid_a.setObjectName("ellipsoid_a")
        self.ellipsoid_image = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_image.setGeometry(QtCore.QRect(170, 0, 251, 201))
        self.ellipsoid_image.setText("")
        self.ellipsoid_image.setPixmap(QtGui.QPixmap("Ellipsoid.png"))
        self.ellipsoid_image.setScaledContents(True)
        self.ellipsoid_image.setObjectName("ellipsoid_image")
        self.ellipsoid_c_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_c_label.setGeometry(QtCore.QRect(0, 150, 74, 18))
        self.ellipsoid_c_label.setObjectName("ellipsoid_c_label")
        self.ellipsoid_measurement = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_measurement.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.ellipsoid_measurement.setObjectName("ellipsoid_measurement")
        self.ellipsoid_c = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_c.setGeometry(QtCore.QRect(40, 140, 104, 31))
        self.ellipsoid_c.setObjectName("ellipsoid_c")
        self.ellipsoid_a_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_a_label.setGeometry(QtCore.QRect(0, 50, 74, 18))
        self.ellipsoid_a_label.setObjectName("ellipsoid_a_label")
        self.ellipsoid_b = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_b.setGeometry(QtCore.QRect(40, 90, 104, 31))
        self.ellipsoid_b.setObjectName("ellipsoid_b")
        self.ellipsoid_b_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_b_label.setGeometry(QtCore.QRect(0, 100, 74, 18))
        self.ellipsoid_b_label.setObjectName("ellipsoid_b_label")
        self.z_direction_2 = QtWidgets.QLabel(self.ellipsoid)
        self.z_direction_2.setGeometry(QtCore.QRect(190, 210, 201, 18))
        self.z_direction_2.setObjectName("z_direction_2")
        self.stackedWidget.addWidget(self.ellipsoid)
        self.button_ok = QtWidgets.QPushButton(Form)
        self.button_ok.setGeometry(QtCore.QRect(360, 320, 95, 26))
        self.button_ok.setObjectName("button_ok")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.type_label.setText(_translate("Form", "Heat Source Type:"))
        self.type.setItemText(0, _translate("Form", "Goldak"))
        self.type.setItemText(1, _translate("Form", "Elipsoid"))
        self.label_2.setText(_translate("Form", "Please select a heat source type..."))
        self.goldak_cr_label.setText(_translate("Form", "cr"))
        self.goldak_b_label.setText(_translate("Form", "b"))
        self.goldak_measurement.setText(_translate("Form", "Length (mm):"))
        self.goldak_a_label.setText(_translate("Form", "a"))
        self.goldak_cf_label.setText(_translate("Form", "cf"))
        self.z_direction_1.setText(_translate("Form", "Welding direction - t x n axis"))
        self.ellipsoid_c_label.setText(_translate("Form", "c"))
        self.ellipsoid_measurement.setText(_translate("Form", "Radius (mm):"))
        self.ellipsoid_a_label.setText(_translate("Form", "a"))
        self.ellipsoid_b_label.setText(_translate("Form", "b"))
        self.z_direction_2.setText(_translate("Form", "Welding direction - t x n axis"))
        self.button_ok.setText(_translate("Form", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiModuleHeatSource()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
