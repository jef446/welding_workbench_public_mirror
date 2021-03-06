import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

from module_heat_source_calib import UiModuleHeatSourceCalib
from boiler_module_material_prop import ModuleMaterialPropMainWindow
from boiler_module_weld_path import ModuleWeldPathMainWindow
from boiler_module_weld_path_steady import ModuleWeldPathSteadyMainWindow
from boiler_module_torch_param import ModuleTorchParamMainWindow
from boiler_module_heat_source import ModuleHeatSourceMainWindow
from boiler_module_postproc_tc import ModulePostProcTCMainWindow
pathToWorkbench=os.getenv('USER_WELDWB_srcDir')
pathToResults = pathToWorkbench+'/simulation/tmp/nonlinearthermal.base'

class ModuleHeatSourceCalibMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings','app8')
        print(self.settings.fileName())
        self.ModuleHeatSourceCalibMainWindow = QMainWindow()
        self.ui = UiModuleHeatSourceCalib()
        self.ui.setupUi(self.ModuleHeatSourceCalibMainWindow)

        #Non standard template
        # Events from Stage 1
        self.ui.pushButton_2.clicked.connect(self.clicked2) # <- Specify Material data
        self.ui.pushButton_3.clicked.connect(self.clicked3) # <- Load MAterial data
        self.ui.pushButton_4.clicked.connect(self.clicked4) # <- Specify beam conditions
        self.ui.pushButton_5.clicked.connect(self.clicked5) # <- Load beam conditions
        self.ui.pushButton_6.clicked.connect(self.clicked6) # <- Specify input power
        self.ui.pushButton_7.clicked.connect(self.clicked7) # <- Specify heat source type
        self.ui.pushButton_8.clicked.connect(self.clicked8) # <- Run Simulation
        self.ui.pushButton_9.clicked.connect(self.clicked9) # <- Load Simulation results
        self.ui.pushButton_10.clicked.connect(self.clicked10) # <- Run error checking
        self.ui.pushButton_12.clicked.connect(self.clicked12) # <- Save Simulation results
        self.ui.radioButton_3.clicked.connect(self.NL)
        self.ui.radioButton_4.clicked.connect(self.steady)        
        #self.ui.pushButton_8.setEnabled(True)
        
    def steady(self):
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        
    def NL(self):
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        
    def clicked2(self):
        self.ui.ModuleMaterialPropMainWindow=ModuleMaterialPropMainWindow()
        self.ui.ModuleMaterialPropMainWindow.show()
        self.ui.pushButton_4.setEnabled(True)
        if self.ui.radioButton_3.isChecked():
            self.ui.pushButton_5.setEnabled(True)
        else:
            self.ui.pushButton_5.setEnabled(False)

    def clicked3(self):
        fname,_=QFileDialog.getOpenFileName(self.ModuleHeatSourceCalibMainWindow, 'Load Material Data', './', '(*.txt)')
        print(fname)
        fname = str(fname)
        my_env = os.environ.copy()
        my_env["file_no_exp"] = str("91")
        my_env["load"] = fname
        p=subprocess.Popen(["sh","./modifyExportLoad.sh",],env=my_env)
        outputCall = p.communicate()
        #self.ui.label_13.setText(fname)
        self.ui.pushButton_4.setEnabled(True)
        if self.ui.radioButton_3.isChecked():
            self.ui.pushButton_5.setEnabled(True)
        else:
            self.ui.pushButton_5.setEnabled(False)

    def clicked4(self):
        if self.ui.radioButton_4.isChecked():
            self.ui.ModuleWeldPathSteadyMainWindow=ModuleWeldPathSteadyMainWindow()
            self.ui.ModuleWeldPathSteadyMainWindow.show()
        else:
            self.ui.ModuleWeldPathMainWindow=ModuleWeldPathMainWindow()
            self.ui.ModuleWeldPathMainWindow.show()
        self.ui.pushButton_6.setEnabled(True)
        
    def clicked5(self):
        fname,_=QFileDialog.getOpenFileName(self.ModuleHeatSourceCalibMainWindow, 'Load Beam Conditions', './', '(*.txt)')
        print(fname)
        fname = str(fname)
        my_env = os.environ.copy()
        my_env["file_no_exp"] = str("92")
        my_env["load"] = fname
        p=subprocess.Popen(["sh","./modifyExportLoad_NL.sh",],env=my_env)
        #self.ui.label_14.setText(fname)
        self.ui.pushButton_6.setEnabled(True)
        
    def clicked6(self):
        self.ui.ModuleTorchParamMainWindow=ModuleTorchParamMainWindow()
        self.ui.ModuleTorchParamMainWindow.show()
        self.ui.pushButton_7.setEnabled(True)
        
    def clicked7(self):
        self.ui.ModuleHeatSourceMainWindow=ModuleHeatSourceMainWindow()
        self.ui.ModuleHeatSourceMainWindow.show()
        self.ui.pushButton_8.setEnabled(True)
        
    def clicked8(self):
        #p=subprocess.Popen(["xterm","-e","./runSimConnect.sh",])
        my_env = os.environ.copy()
        if self.ui.radioButton_3.isChecked():
            my_env["sim_type"] = str("1")
        else:
            my_env["sim_type"] = str("0")
        p=subprocess.Popen(["sh","./runSimConnect.sh",],env=my_env)
        outputCall = p.communicate()
        #### dname_resu must be file path to .base file that is created when running sim
        self.ui.label_5.setText(pathToResults)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
    
    def clicked9(self):
        #fname_resu,_=QFileDialog.getOpenFileName(self.ModuleHeatSourceCalibMainWindow, 'Open file', './', 'Results File (*.base)')
        dname_resu=QFileDialog.getExistingDirectory(self.ModuleHeatSourceCalibMainWindow, 'Select Results Directory', './')
        print(dname_resu)
        dname_resu = str(dname_resu)
        self.ui.label_5.setText(dname_resu)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)

    def clicked10(self):
        my_env = os.environ.copy()
        dname = self.ui.label_5.text()
        dname = str(dname)
        my_env["resu"] = dname
        p=subprocess.Popen(["sh","./modifyErrorExport.sh",],env=my_env)
        outputCall = p.communicate()
        self.ui.ModulePostProcTCMainWindow=ModulePostProcTCMainWindow()
        self.ui.ModulePostProcTCMainWindow.show()
        
    def clicked12(self):
        sfile=QFileDialog.getSaveFileName(self.ModuleHeatSourceCalibMainWindow, 'Save as', pathToWorkbench, '*.base')
        sfilename = sfile[0]
        if str(sfilename).endswith('.base'):
            sfilename = str(sfilename)
        else:
            sfilename = str(sfilename)+'.base'
        my_env = os.environ.copy()
        my_env["resu_file"] = pathToResults
        my_env["input"] = str(sfilename)
        p=subprocess.Popen(["sh","./saveResu.sh",],env=my_env)
    

    def show(self):
        self.ModuleHeatSourceCalibMainWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleHeatSourceCalibMainWindow = ModuleHeatSourceCalibMainWindow()
    ModuleHeatSourceCalibMainWindow.show()
    sys.exit(app.exec_())
