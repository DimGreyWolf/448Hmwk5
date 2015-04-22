import sys
from PyQt4 import QtGui, QtCore
from drug_database import DrugDatabase
import pyqtgraph as pg
import numpy as np

# Subclass of DrugGraph for toolbar widget
class Toolbar(QtGui.QWidget):

    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,500)
        self.setFixedSize(300,500)
        self.setWindowTitle('Drug Analysis Toolbar')

        radioNaa = QtGui.QRadioButton('# Active Compounds: ',self)
        radioNaa.move(10,20)
        radioNan = QtGui.QRadioButton('# Non-Active Compounds: ',self)
        radioNan.move(10,50)
        radioNna = QtGui.QRadioButton('# Active labelled as Non-Active: ',self)
        radioNna.move(10,80)
        radioNnn = QtGui.QRadioButton('# Non-Active labelled as Non-Active: ',self)
        radioNnn.move(10,110)

        listDrugs = QtGui.QListWidget(self)
        listDrugs.setFixedSize(280,300)
        listDrugs.move(10,140)

        labelRatio = QtGui.QLabel('Ratio of selected drug: ',self)
        labelRatio.move(10,440)        

        btnExit = QtGui.QPushButton('Exit',self)
        btnExit.move(200,460)
        btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

# Handles all GUI functionality for Drug Analysis program
# This class is the view class in MVC architecture
class DrugGraph:

    def __init__(self):
        print('DrugGraph is now running')
        self.model = DrugDatabase()
        self.initUI()
        #super(DrugGraph,self).__init__()

    def initUI(self):
        self.win = QtGui.QMainWindow()
        self.win.resize(800,350)
        self.win.setWindowTitle('Drug Analysis')
        self.plot = pg.PlotWidget()
        self.win.setCentralWidget(self.plot)
        self.win.show()

        self.selectWin = Toolbar()

# This block of the code will execute the program
# when python runs this specific script
# e.g 'python HW5.py'
def main():
    app = QtGui.QApplication(sys.argv)
    drugGraph = DrugGraph()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
