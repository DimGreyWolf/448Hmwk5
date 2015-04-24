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
        self.model.readCandidates('hw5db1.txt')
        self.model.readExamples('hw5db2.txt')

    #===============================
    # GUI related methods
    #===============================
    
    #------------------
    # Inbound to View
    #------------------
    
    # Refreshes View with updated data 
    def refreshView(self):
        # Reperform all comparison analysis methods
        self.method1()
        self.method2()
        self.method3()
        self.method4()
        self.method5()

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
    def method1(self):
        print('Performing comparison method 1...')

        newNaa = 0
        newNan = 0
        newNna = 0
        newNnn = 0

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            dA = 0.0
            dN = 0.0
            sumNaa = 0.0
            sumNan = 0.0
            # Go through all elements aka properties
            for z in range(3,19):
                candidateProperty = 0.0
                exampleNaaProperty = 0.0
                exampleNanProperty = 0.0
                candidateProperty = self.model.getCandidateData(x,z)
                #Getting means and standard deviations from second file
                if z < 11:
                   exampleNaaProperty = self.model.getExampleData(0,z-3)
                   exampleNanProperty = self.model.getExampleData(2,z-3)
                else:
                   exampleNaaProperty = self.model.getExampleData(1,z-11)
                   exampleNanProperty = self.model.getExampleData(3,z-11)
                #Euclidean Distance calculations
                candidateProperty = float(candidateProperty)
                exampleNaaProperty = float(exampleNaaProperty)
                exampleNanProperty = float(exampleNanProperty)
                diffNaa = candidateProperty - exampleNaaProperty
                diffNan = candidateProperty - exampleNanProperty
                powNaa = diffNaa * diffNaa
                powNan = diffNan * diffNan
                sumNaa = sumNaa + powNaa
                sumNan = sumNan + powNan
            dA = float(math.sqrt(sumNaa))
            dN = float(math.sqrt(sumNan))
            if x < 1348:
                if dA <= dN:
                    newNaa = newNaa + 1
                else: 
                    newNna = newNna + 1
            else:
               if dA <= dN:
                    newNan = newNan + 1
               else:
                    newNnn = newNnn + 1

        print(newNaa)
        print(newNan)
        print(newNna)
        print(newNnn)

        # Sets new drug counts using current method
        self.model.setAmtNaa(1,newNaa)
        self.model.setAmtNan(1,newNan)
        self.model.setAmtNna(1,newNna)
        self.model.setAmtNnn(1,newNnn)

        if newNan != 0:
            newRatio = float(newNaa) / float(newNan)
        else:
            newRatio = newNaa
        self.model.setRatio(1,newRatio)

    # Mahalnobis Database Analyzation method
    def method2(self):
        print('Performing comparison method 2...')

        newNaa = 0
        newNan = 0
        newNna = 0
        newNnn = 0

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            dA = 0.0
            dN = 0.0
            sumNaa = 0.0
            sumNan = 0.0
            # Go through all elements aka properties
            for z in range(3,19):
                candidateProperty = 0.0
                exampleNaaProperty = 0.0
                exampleNanProperty = 0.0
                exampleNaaSigma = 0.0
                exampleNanSigma = 0.0
                candidateProperty = self.model.getCandidateData(x,z)
                #Getting means and standard deviations from second file
                if z < 11:
                   exampleNaaProperty = self.model.getExampleData(0,z-3)
                   exampleNanProperty = self.model.getExampleData(2,z-3)
                   exampleNaaSigma = self.model.getExampleData(4,z-3) 
                   exampleNanSigma = self.model.getExampleData(6,z-3)
                else:
                   exampleNaaProperty = self.model.getExampleData(1,z-11)
                   exampleNanProperty = self.model.getExampleData(3,z-11)
                   exampleNaaSigma = self.model.getExampleData(5,z-11)
                   exampleNanSigma = self.model.getExampleData(7,z-11)
                #Mahalanobis Database calculation
                candidateProperty = float(candidateProperty)
                exampleNaaProperty = float(exampleNaaProperty)
                exampleNanProperty = float(exampleNanProperty)
                exampleNaaSigma = float(exampleNaaSigma)
                exampleNanSigma = float(exampleNanSigma)
                diffNaa = (candidateProperty - exampleNaaProperty) / exampleNaaSigma
                diffNan = (candidateProperty - exampleNanProperty) / exampleNanSigma
                powNaa = diffNaa * diffNaa
                powNan = diffNan * diffNan
                sumNaa = sumNaa + powNaa
                sumNan = sumNan + powNan
            dA = float(math.sqrt(sumNaa))
            dN = float(math.sqrt(sumNan))
            if x < 1348:
                if dA <= dN:
                    newNaa = newNaa + 1
                else: 
                    newNna = newNna + 1
            else:
                if dA <= dN:
                    newNan = newNan + 1
                else:
                    newNnn = newNnn + 1

        print(newNaa)
        print(newNan)
        print(newNna)
        print(newNnn)

        # Sets new drug counts using current method
        self.model.setAmtNaa(2,newNaa)
        self.model.setAmtNan(2,newNan)
        self.model.setAmtNna(2,newNna)
        self.model.setAmtNnn(2,newNnn)

        if newNan != 0:
            newRatio = float(newNaa) / float(newNan)
        else:
            newRatio = newNaa
        self.model.setRatio(2,newRatio)

    # Voting method using Euclidean Distance method
    def method3(self):
        print('Performing comparison method 3...')

        newNaa = 0
        newNan = 0
        newNna = 0
        newNnn = 0

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            dA = 0.0
            dN = 0.0
            Pa = 0
            Qa = 0
            Pn = 0
            Qn = 0
            # Go through all elements aka properties
            for z in range(3,19):
                candidateProperty = 0.0
                exampleNaaProperty = 0.0
                exampleNanProperty = 0.0
                candidateProperty = self.model.getCandidateData(x,z)
                #Getting means and standard deviations from second file
                if z < 11:
                   exampleNaaProperty = self.model.getExampleData(0,z-3)
                   exampleNanProperty = self.model.getExampleData(2,z-3)
                else:
                   exampleNaaProperty = self.model.getExampleData(1,z-11)
                   exampleNanProperty = self.model.getExampleData(3,z-11)
                #Voting Euclidean Distrance calculations
                candidateProperty = float(candidateProperty)
                exampleNaaProperty = float(exampleNaaProperty)
                exampleNanProperty = float(exampleNanProperty)
                diffNaa = candidateProperty - exampleNaaProperty
                diffNan = candidateProperty - exampleNanProperty
                powNaa = diffNaa * diffNaa
                powNan = diffNan * diffNan
                sqrtNaa = math.sqrt(powNaa)
                sqrtNan = math.sqrt(powNan)
                if x < 1348:
                    if sqrtNaa <= sqrtNan:
                        Pa = Pa + 1
                    else: 
                        Qa = Qa + 1
                else:
                   if sqrtNaa <= sqrtNan:
                        Pn = Pn + 1
                   else:
                        Qn = Qn + 1
            if x < 1348:
                if Pa <= Qa:
                    newNaa = newNaa + 1
                else:
                    newNna = newNna + 1
            else:
                if Pn <= Qn:
                    newNan = newNan + 1
                else:
                    newNnn = newNnn + 1 

        print(newNaa)
        print(newNan)
        print(newNna)
        print(newNnn)

        # Sets new drug counts using current method
        self.model.setAmtNaa(3,newNaa)
        self.model.setAmtNan(3,newNan)
        self.model.setAmtNna(3,newNna)
        self.model.setAmtNnn(3,newNnn)

        if newNan != 0:
            newRatio = float(newNaa) / float(newNan)
        else:
            newRatio = newNaa
        self.model.setRatio(3,newRatio)

    # Voting method using Mahalnobus Database Analyzation method
    def method4(self):
        print('Performing comparison method 4...')

        newNaa = 0
        newNan = 0
        newNna = 0
        newNnn = 0

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            dA = 0.0
            dN = 0.0
            Pa = 0
            Qa = 0
            Pn = 0
            Qn = 0
            # Go through all elements aka properties
            for z in range(3,19):
                candidateProperty = 0.0
                exampleNaaProperty = 0.0
                exampleNanProperty = 0.0
                exampleNaaSigma = 0.0
                exampleNanSigma = 0.0
                candidateProperty = self.model.getCandidateData(x,z)
                #Getting means and standard deviations from second file
                if z < 11:
                   exampleNaaProperty = self.model.getExampleData(0,z-3)
                   exampleNanProperty = self.model.getExampleData(2,z-3)
                   exampleNaaSigma = self.model.getExampleData(4,z-3) 
                   exampleNanSigma = self.model.getExampleData(6,z-3)
                else:
                   exampleNaaProperty = self.model.getExampleData(1,z-11)
                   exampleNanProperty = self.model.getExampleData(3,z-11)
                   exampleNaaSigma = self.model.getExampleData(5,z-11)
                   exampleNanSigma = self.model.getExampleData(7,z-11)
                #Voting Mahalanobis Database calculations
                candidateProperty = float(candidateProperty)
                exampleNaaProperty = float(exampleNaaProperty)
                exampleNanProperty = float(exampleNanProperty)
                exampleNaaSigma = float(exampleNaaSigma)
                exampleNanSigma = float(exampleNanSigma)
                diffNaa = (candidateProperty - exampleNaaProperty) / exampleNaaSigma
                diffNan = (candidateProperty - exampleNanProperty) / exampleNanSigma
                powNaa = diffNaa * diffNaa
                powNan = diffNan * diffNan
                sqrtNaa = math.sqrt(powNaa)
                sqrtNan = math.sqrt(powNan)
                if x < 1348:
                    if sqrtNaa <= sqrtNan:
                        Pa = Pa + 1
                    else: 
                        Qa = Qa + 1
                else:
                   if sqrtNaa <= sqrtNan:
                        Pn = Pn + 1
                   else:
                        Qn = Qn + 1
            if x < 1348:
                if Pa <= Qa:
                    newNaa = newNaa + 1
                else:
                    newNna = newNna + 1
            else:
                if Pn <= Qn:
                    newNan = newNan + 1
                else:
                    newNnn = newNnn + 1 

        print(newNaa)
        print(newNan)
        print(newNna)
        print(newNnn)

        # Sets new drug counts using current method
        self.model.setAmtNaa(4,newNaa)
        self.model.setAmtNan(4,newNan)
        self.model.setAmtNna(4,newNna)
        self.model.setAmtNnn(4,newNnn)

        if newNan != 0:
            newRatio = float(newNaa) / float(newNan)
        else:
            newRatio = newNaa
        self.model.setRatio(4,newRatio)

    # Special Analyzation method
    def method5(self):
        print('Performing comparison method 5...')

        newNaa = 0
        newNan = 0
        newNna = 0
        newNnn = 0

        # Go through list of all candidates
        for x in range(0,self.model.getAmtCandidates()):
            # Go through list of all examples
            dA = 0.0
            dN = 0.0
            Pa = 0
            Qa = 0
            Pn = 0
            Qn = 0
            # Go through all elements aka properties
            for z in range(3,19):
                candidateProperty = 0.0
                exampleNaaProperty = 0.0
                exampleNanProperty = 0.0
                exampleNaaSigma = 0.0
                exampleNanSigma = 0.0
                candidateProperty = self.model.getCandidateData(x,z)
                #Getting means and standard deviations from second files
                if z < 11:
                   exampleNaaProperty = self.model.getExampleData(0,z-3)
                   exampleNanProperty = self.model.getExampleData(2,z-3)
                   exampleNaaSigma = self.model.getExampleData(4,z-3) 
                   exampleNanSigma = self.model.getExampleData(6,z-3)
                else:
                   exampleNaaProperty = self.model.getExampleData(1,z-11)
                   exampleNanProperty = self.model.getExampleData(3,z-11)
                   exampleNaaSigma = self.model.getExampleData(5,z-11)
                   exampleNanSigma = self.model.getExampleData(7,z-11)
                #Special calculations combining Method 3 and Method 4
                candidateProperty = float(candidateProperty)
                exampleNaaProperty = float(exampleNaaProperty)
                exampleNanProperty = float(exampleNanProperty)
                exampleNaaSigma = float(exampleNaaSigma)
                exampleNanSigma = float(exampleNanSigma)
                diffNaa = (candidateProperty - exampleNaaProperty)
                diffNan = (candidateProperty - exampleNanProperty)
                divNaa = diffNaa / exampleNaaSigma
                divNan = diffNan / exampleNanSigma
                powNaa3 = diffNaa * diffNaa
                powNan3 = diffNan * diffNan
                powNaa4 = divNaa * divNaa
                powNan4 = divNan * divNan
                sqrtNaa3 = math.sqrt(powNaa3)
                sqrtNan3 = math.sqrt(powNan3)
                sqrtNaa4 = math.sqrt(powNaa4)
                sqrtNan4 = math.sqrt(powNan4)
                if x < 1348:
                    if sqrtNaa3 <= sqrtNan3 and sqrtNaa4 <= sqrtNan4:
                        Pa = Pa + 1
                    else: 
                        Qa = Qa + 1
                else:
                    if sqrtNaa3 <= sqrtNan3 and sqrtNaa4 <= sqrtNan4:
                        Pn = Pn + 1
                    else:
                        Qn = Qn + 1
            if x < 1348:
                if Pa <= Qa:
                    newNaa = newNaa + 1
                else:
                    newNna = newNna + 1
            else:
                if Pn <= Qn:
                    newNan = newNan + 1
                else:
                    newNnn = newNnn + 1 

        print(newNaa)
        print(newNan)
        print(newNna)
        print(newNnn)

        # Sets new drug counts using current method
        self.model.setAmtNaa(5,newNaa)
        self.model.setAmtNan(5,newNan)
        self.model.setAmtNna(5,newNna)
        self.model.setAmtNnn(5,newNnn)

        if newNan != 0:
            newRatio = float(newNaa) / float(newNan)
        else:
            newRatio = newNaa
        self.model.setRatio(5,newRatio)


