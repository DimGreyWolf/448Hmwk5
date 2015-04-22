import os

# Maintains data used in Drug Analysis program
# This class is the model class in MVC architecture
class DrugDatabase:

    # Constructor
    def __init__(self):
        print('DrugDatabase initiated')
        self.candidates = []
        self.examples = []
        self.ratio = 0.0
        self.listDisplay = []
        self.listNaa = []
        self.listNan = []
        self.listNna = []
        self.listNnn = []

    # Reads the potential candidate drugs file
    def readCandidates(self,filename):
        print('Reading candidate files')
        with open(filename,'rb') as f:
            for line in f:
                self.candidates.append(line)
        f.close()
        print('Amount of candidates read: {}'.format(len(self.candidates)))

    # Reads the example ideal drugs file
    def readExamples(self,filename):
        print('Reading example files')
        with open(filename,'rb') as f:
            for line in f:
                self.examples.append(line)
        f.close()
        print('Amount of examples read: {}'.format(len(self.examples)))

    # Obtains the specific element of a specific candidate drug
    # e.g getCandidateData(5,0), gets the 0th element of the 5th candidate
    def getCandidateData(self,drug,element):
        selectedDrug = self.candidates[drug]
        categories = selectedDrug.split()
        selectedElement = categories[element]
        return selectedElement

    # Obtains specific element of a specific example drug
    # e.g getExampleData(5,0), gets the 0th element of the 5th example
    def getExampleData(self,drug,element):
        selectedExample = self.examples[drug]
        categories = selectedExample.split()
        selectedElement = categories[element]
        return selectedElement
    
    # Getter & Setter the ratio of the selected drug
    def getRatio(self)
        return self.ratio

    def setRatio(self,ratio)
        self.ratio = ratio

    # Selects drug list to be displayed in list widget
    def selectNaa(self):
        self.listDisplay = self.listNaa

    def selectNan(self):
        self.listDisplay = self.listNan

    def selectNna(self):
        self.listDisplay = self.listNna

    def selectNnn(self):
        self.listDisplay = self.listNnn

    # Updates drug list
    def updateNaa(self,Naa)
        self.listNaa = Naa

    def updateNan(self,Nan)
        self.listNan = Nan

    def updateNna(self,Nna)
        self.listNna = Nna

    def updateNnn(self,Nnn)

    # Returns display list
    def getDisplayList(self)
        return self.listDisplay
