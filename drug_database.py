import os

# Maintains data used in Drug Analysis program
# This class is the model class in MVC architecture
class DrugDatabase:

    # Constructor
    def __init__(self):
        print('DrugDatabase initiated')
        self.candidates = []
        self.examples = []

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
    def getExampleData(self,drug,element):
        selectedExample = self.examples[drug]
        categories = selectedExample.split()
        selectedElement = categories[element]
        return selectedElement
