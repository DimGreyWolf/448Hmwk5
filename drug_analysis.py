from HW5 import DrugGraph, Toolbar
from drug_database import DrugDatabase

# This class performs analysis and updates 
# DrugGraph using DrugDatabase
# This class is the controller class in MVC architecture
class DrugAnalysis:

    def __init__(self,view,model):
        print('DrugAnalysis initialized')
        self.view = view
        self.model = model

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
