import sys
from PyQt4 import QtGui, QtCore
from drug_database import DrugDatabase
import pyqtgraph as pg
import numpy as np

# This class is the view class of MVC architecture
# and handles all GUI functionality
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

        self.selectWin = QtGui.QWidget()
        self.selectWin.resize(300,150)
        self.selectWin.setWindowTitle('Selected Drug')
        self.selectWin.show()

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
