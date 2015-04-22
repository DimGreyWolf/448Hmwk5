import sys
from PyQt4 import QtGui, QtCore
from drug_database import DrugDatabase
from drug_analysis import DrugAnalysis
import pyqtgraph as pg
import numpy as np

# Subclass of DrugGraph for toolbar widget
class Toolbar(QtGui.QWidget):

    def __init__(self,model,controller):
        super(Toolbar,self).__init__()
        self.model = model
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.resize(300,500)
        self.setFixedSize(300,500)
        self.setWindowTitle('Drug Analysis Toolbar')

        self.radioNaa = QtGui.QRadioButton('# Active Compounds: ',self)
        self.radioNaa.move(10,20)
        self.radioNaa.clicked.connect(self.controller.selectNaa)
        self.radioNaa.clicked.connect(self.controller.refreshDisplayList)
        
        self.radioNan = QtGui.QRadioButton('# Non-Active Compounds: ',self)
        self.radioNan.move(10,50)
        self.radioNna = QtGui.QRadioButton('# Active labelled as Non-Active: ',self)
        self.radioNna.move(10,80)
        self.radioNnn = QtGui.QRadioButton('# Non-Active labelled as Non-Active: ',self)
        self.radioNnn.move(10,110)

        self.listDrugs = QtGui.QListWidget(self)
        self.listDrugs.setFixedSize(280,300)
        self.listDrugs.move(10,140)

        self.labelRatio = QtGui.QLabel('Ratio of selected drug: ',self)
        self.labelRatio.move(10,440)        

        self.btnExit = QtGui.QPushButton('Exit',self)
        self.btnExit.move(200,460)
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

# Handles all GUI functionality for Drug Analysis program
# This class is the view class in MVC architecture
class DrugGraph:

    def __init__(self):
        print('DrugGraph is now running')
        self.model = DrugDatabase()
        self.controller = DrugAnalysis(self,self.model)
        self.initUI()
        #super(DrugGraph,self).__init__()

    def initUI(self):
        self.graph = QtGui.QMainWindow()
        self.graph.resize(800,350)
        self.graph.setWindowTitle('Drug Analysis')
        self.plot = pg.PlotWidget()
        self.graph.setCentralWidget(self.plot)
        self.graph.show()

        self.toolbar = Toolbar(self.model,self.controller)

# This block of the code will execute the program
# when python runs this specific script
# e.g 'python HW5.py'
def main():
    app = QtGui.QApplication(sys.argv)
    drugGraph = DrugGraph()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
