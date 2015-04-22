import os

# Maintains data used in Drug Analysis program
# This class is the model class in MVC architecture
class DrugDatabase:

    # Constructor
    def __init__(self):
        print('DrugDatabase initiated')
        self.candidates = []
        self.examples = []
        self.ratio1 = 0.0
        self.ratio2 = 0.0
        self.ratio3 = 0.0
        self.ratio4 = 0.0
        self.ratio5 = 0.0
        self.AmtNaa1 = 0
        self.AmtNaa2 = 0
        self.AmtNaa3 = 0
        self.AmtNaa4 = 0
        self.AmtNaa5 = 0
        self.AmtNan1 = 0
        self.AmtNan2 = 0
        self.AmtNan3 = 0
        self.AmtNan4 = 0
        self.AmtNan5 = 0
        self.AmtNna1 = 0
        self.AmtNna2 = 0
        self.AmtNna3 = 0
        self.AmtNna4 = 0
        self.AmtNna5 = 0
        self.AmtNnn1 = 0
        self.AmtNnn2 = 0
        self.AmtNnn3 = 0
        self.AmtNnn4 = 0
        self.AmtNnn5 = 0

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

    def getAmtCandidates(self):
        return len(self.candidates)

    def getAmtExamples(self):
        return len(self.examples)

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
    def getRatio(self,method):
        if method == 1:
            return self.ratio1
        elif method == 2:
            return self.ratio2
        elif method == 3:
            return self.ratio3
        elif method == 4:
            return self.ratio4
        elif method == 5:
            return self.ratio5
        return 0.0

    def setRatio(self,method,ratio):
        if method == 1:
            self.ratio1 = ratio
        elif method == 2:
            self.ratio2 = ratio
        elif method == 3:
            self.ratio3 = ratio
        elif method == 4:
            self.ratio4 = ratio
        elif method == 5:
            self.ratio5 = ratio

    # Getter & Setter for amount in specific drug list
    def getAmtNaa(self,method):
        if method == 1:
            return self.AmtNaa1
        elif method == 2:
            return self.AmtNaa2
        elif method == 3:
            return self.AmtNaa3
        elif method == 4:
            return self.AmtNaa4
        elif method == 5:
            return self.AmtNaa5
        return 0

    def getAmtNan(self,method):
        if method == 1:
            return self.AmtNan1
        elif method == 2:
            return self.AmtNan2
        elif method == 3:
            return self.AmtNan3
        elif method == 4:
            return self.AmtNan4
        elif method == 5:
            return self.AmtNan5
        return 0

    def getAmtNna(self,method):
        if method == 1:
            return self.AmtNna1
        elif method == 2:
            return self.AmtNna2
        elif method == 3:
            return self.AmtNna3
        elif method == 4:
            return self.AmtNna4
        elif method == 5:
            return self.AmtNna5
        return 0

    def getAmtNnn(self,method):
        if method == 1:
            return self.AmtNnn1
        elif method == 2:
            return self.AmtNnn2
        elif method == 3:
            return self.AmtNnn3
        elif method == 4:
            return self.AmtNnn4
        elif method == 5:
            return self.AmtNnn5
        return 0
