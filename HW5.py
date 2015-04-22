import sys
from PyQt4 import QtGui, QtCore
from drug_database import DrugDatabase
import pyqtgraph as pg
import numpy as np

# This class is the view class of MVC architecture
# and handles all GUI functionality

class Toolbar(QtGui.QWidget):

    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,500)
        self.setFixedSize(300,500)
        self.setWindowTitle('Toolbar')
        labelNaa = QtGui.QLabel('# Active Compounds: ',self)
        labelNaa.move(10,20)
        labelNan = QtGui.QLabel('# Non-Active Compounds: ',self)
        labelNan.move(10,50)
        labelNna = QtGui.QLabel('# Active labelled as Non-Active: ',self)
        labelNna.move(10,80)
        labelNnn = QtGui.QLabel('# Non-Active labelled as Non-Active: ',self)
        labelNnn.move(10,110)
        labelRatio = QtGui.QLabel('Ratio: ',self)
        labelRatio.move(10,140)
        

        btnExit = QtGui.QPushButton('Exit',self)
        btnExit.move(200,460)
        btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

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

    def windowClicked(self):
        print('Clicked')
        drug, prompt = QtGui.QInputDialog.getText(win,'Selected Drug','Which drug?')

# This block of the code will execute the program
# when python runs this specific script
# e.g 'python HW5.py'
def main():
    app = QtGui.QApplication(sys.argv)
    drugGraph = DrugGraph()
    #win.setCentralWidget(drugGraph)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
