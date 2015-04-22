import math
import pyqtgraph as pg
import numpy as np

# This class performs analysis and updates 
# DrugGraph using DrugDatabase
# This class is the controller class in MVC architecture
class DrugAnalysis:

    def __init__(self,view,model):
        print('DrugAnalysis initialized')
        self.view = view
        self.model = model
        self.selectedMethod = 0

    #===============================
    # GUI related methods
    #===============================
    
    #------------------
    # Inbound to View
    #------------------
    
    # Refreshes View with updated data 
    def refreshView(self):
        # Obtain data from model
        newAmtNaa = self.model.getAmtNaa(self.selectedMethod)
        newAmtNan = self.model.getAmtNan(self.selectedMethod)
        newAmtNna = self.model.getAmtNna(self.selectedMethod)
        newAmtNnn = self.model.getAmtNnn(self.selectedMethod)
        newRatio = self.model.getRatio(self.selectedMethod)

        # Apply data to view
        self.view.toolbar.labelNaa.setText('Amount of Naa: {}'.format(newAmtNaa))
        self.view.toolbar.labelNan.setText('Amount of Nan: {}'.format(newAmtNan))
        self.view.toolbar.labelNna.setText('Amount of Nna: {}'.format(newAmtNna))
        self.view.toolbar.labelNnn.setText('Amount of Nnn: {}'.format(newAmtNnn))
        self.view.toolbar.labelRatio.setText('Ratio Naa/Nan: {}'.format(newRatio)) 
        self.view.toolbar.labelNaa.resize(self.view.toolbar.labelNaa.sizeHint())
        self.view.toolbar.labelNan.resize(self.view.toolbar.labelNan.sizeHint())
        self.view.toolbar.labelNna.resize(self.view.toolbar.labelNna.sizeHint())
        self.view.toolbar.labelNnn.resize(self.view.toolbar.labelNnn.sizeHint())
        self.view.toolbar.labelRatio.resize(self.view.toolbar.labelRatio.sizeHint())

        # Plot ratio data onto graph
        self.view.plot.clear()
        s1 = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
        s1.addPoints([{'pos':(1,self.model.getRatio(1))},{'pos':(2,self.model.getRatio(2))},{'pos':(3,self.model.getRatio(3))},{'pos':(4,self.model.getRatio(4))},{'pos':(5,self.model.getRatio(5))}])
        self.view.plot.addItem(s1)

    #-------------------
    # Outbound from View
    #-------------------
 
    # Changes list to be displayed in List Widget in GUI
    def selectMethod1(self):
        self.selectedMethod = 1
        print('Viewing Method 1')
        self.refreshView()
    
    def selectMethod2(self):
        self.selectedMethod = 2
        print('Viewing Method 2')
        self.refreshView()

    def selectMethod3(self):
        self.selectedMethod = 3
        print('Viewing Method 3')
        self.refreshView()

    def selectMethod4(self):
        self.selectedMethod = 4
        print('Viewing Method 4')
        self.refreshView()

    def selectMethod5(self):
        self.selectedMethod = 5
        print('Viewing Method 5')
        self.refreshView()

    #================================
    # Drug analyzation methods
    #================================

    # Euclidean Distance Analyzation method
    def method1(self,drug):
        # Obtains name element of selected candidate using model
        candidateName = self.model.getCandidateData(drug,0)
        log = 'Analyzing drug {} using Euclidean Distance comparison.'.format(candidateName)

        dA = []
        dN = []

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            for y in range(0,self.model.getAmtExamples()):
                for z in range(1,16):
                    print('')
        self.model.setAmtNaa(1,1)
        self.model.setAmtNan(1,1)
        self.model.setAmtNna(1,1)
        self.model.setAmtNnn(1,1)
        return 0

    # Mahalnobis Database Analyzation method
    def method2(self,drug):
        return 0

    # Voting method using Euclidean Distance method
    def method3(self,drug):
        return 0

    # Voting method using Mahalnobus Database Analyzation method
    def method4(self,drug):
        return 0

    # Special Analyzation method
    def method5(self,drug):
        return 0
