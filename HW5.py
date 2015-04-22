import sys
from PyQt4 import QtGui, QtCore
from drug_database import DrugDatabase

# This class is the view class of MVC architecture
# and handles all GUI functionality
class DrugGraph(QtGui.QWidget):

    def __init__(self):
        print('DrugGraph is now running')
        super(DrugGraph,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400,400,250,300)
        self.setWindowTitle('Drug Analysis Program')
        self.show()

# This block of the code will execute the program
# when python runs this specific script
# e.g 'python HW5.py'
def main():
    app = QtGui.QApplication(sys.argv)
    drugGraph = DrugGraph()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
