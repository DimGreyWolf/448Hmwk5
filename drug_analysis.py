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
    
    # Refreshes View with updated data 
    def refreshView(self):
        # Obtain data from model
        newAmtNaa = self.model.getAmtNaa()
        newAmtNan = self.model.getAmtNan()
        newAmtNna = self.model.getAmtNna()
        newAmtNnn = self.model.getAmtNnn()
        newRatio = self.model.getRatio()

        # Apply data to view
        self.view.toolbar.labelRatio.setText('Ratio Naa/Nan: {}'.format(newRatio)) 
        self.view.toolbar.labelRatio.resize(self.view.toolbar.labelRatio.sizeHint())

    #-------------------
    # Outbound from View
    #-------------------
 
    # Changes list to be displayed in List Widget in GUI
    def selectMethod1(self):
        print('Viewing Method 1')
        self.refreshView()
    
    def selectMethod2(self):
        print('Viewing Method 2')
        self.refreshView()

    def selectMethod3(self):
        print('Viewing Method 3')
        self.refreshView()

    def selectMethod4(self):
        print('Viewing Method 4')
        self.refreshView()

    def selectMethod5(self):
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
        self.model.setAmtNaa(1)
        self.model.setAmtNan(1)
        self.model.setAmtNna(1)
        self.model.setAmtNnn(1)
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
