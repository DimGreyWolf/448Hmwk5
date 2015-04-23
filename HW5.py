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

    # Initialize UI elements for toolbar
    def initUI(self):
        self.resize(300,400)
        self.setFixedSize(300,400)
        self.setWindowTitle('Drug Analysis Details')

        self.radioMethod1 = QtGui.QRadioButton('Euclidean Distance',self)
        self.radioMethod1.move(10,20)
        self.radioMethod1.clicked.connect(self.controller.selectMethod1)
        
        self.radioMethod2 = QtGui.QRadioButton('Mahalnobis Database',self)
        self.radioMethod2.move(10,50)
        self.radioMethod2.clicked.connect(self.controller.selectMethod2)

        self.radioMethod3 = QtGui.QRadioButton('Voting Euclidean Distance',self)
        self.radioMethod3.move(10,80)
        self.radioMethod3.clicked.connect(self.controller.selectMethod3)

        self.radioMethod4 = QtGui.QRadioButton('Voting Mahalnobis Database',self)
        self.radioMethod4.move(10,110)
        self.radioMethod4.clicked.connect(self.controller.selectMethod4)

        self.radioMethod5 = QtGui.QRadioButton('Special Analysis',self)
        self.radioMethod5.move(10,140)
        self.radioMethod5.clicked.connect(self.controller.selectMethod5)

        self.labelRatio = QtGui.QLabel('Ratio Naa/Nan: -',self)
        self.labelRatio.resize(self.labelRatio.sizeHint())
        self.labelRatio.move(10,170) 

        self.labelNaa = QtGui.QLabel('Amount of Naa: -',self)
        self.labelNaa.move(10,200)

        self.labelNan = QtGui.QLabel('Amount of Nan: -',self)
        self.labelNan.move(10,230)

        self.labelNna = QtGui.QLabel('Amount of Nna: -',self)
        self.labelNna.move(10,260)

        self.labelNnn = QtGui.QLabel('Amount of Nnn: -',self)
        self.labelNnn.move(10,290)

        self.btnExit = QtGui.QPushButton('Exit',self)
        self.btnExit.move(200,365)
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

    # Initialize UI elements for Graph and generally initializes Toolbar
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
