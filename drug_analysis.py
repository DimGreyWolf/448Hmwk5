# This class performs analysis and updates 
# DrugGraph using DrugDatabase
# This class is the controller class in MVC architecture
class DrugAnalysis:

    def __init__(self,view,model):
        print('DrugAnalysis initialized')
        self.view = view
        self.model = model

    #===============================
    # GUI related methods
    #===============================
    
    #------------------
    # Inbound to View
    #------------------
    
    # Refreshes GUI with new selected list
    def refreshDisplayList(self):
        # Obtain data from model
        newDisplayList = self.model.getDisplayList()
        newRatio = self.model.getRatio()

        # Apply data to view
        self.view.toolbar.labelRatio.setText('Ratio {}'.format(newRatio)) 

    #-------------------
    # Outbound from View
    #-------------------
 
    # Changes list to be displayed in List Widget in GUI
    def selectNaa(self):
        print('Viewing Naa drugs.')
        self.model.selectNaa()
        self.refreshDisplayList()
    
    def selectNan(self):
        print('Viewing Nan drugs.')
        self.model.selectNan()
        self.refreshDisplayList()

    def selectNna(self):
        print('Viewing Nna drugs.')
        self.model.selectNna()
        self.refreshDisplayList()

    def selectNnn(self):
        print('Viewing Nnn drugs.')
        self.model.selectNnn()
        self.refreshDisplayList()

    #================================
    # Drug analyzation methods
    #================================

    # Euclidean Distance Analyzation method
    def method1(self,drug):
        # Obtains name element of selected candidate using model
        candidateName = self.model.getCandidateData(drug,0)
        log = 'Analyzing drug {} using Euclidean Distance comparison.'.format(candidateName)
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
