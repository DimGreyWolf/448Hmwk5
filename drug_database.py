import os

class DrugDatabase:

    # Constructor
    def __init__(self):
        print('DrugDatabase initiated')
        self.candidates = []
        self.examples = []

    # Reads the potential candidate drugs file
    def readCandidates(self,filename):
        print('Reading candidate files')
        candidatesFile = open(filename, 'rb')
        for line in candidatesFile:
	    elements = line.split()
            self.candidates += elements

    # Reads the example ideal drugs file
    def readExamples(self,filename):
        print('Reading example files')
        self.examples = open(filename, 'rb')
        examplesFile = open(filename, 'rb')
        for line in candidatesFile:
            elements = line.split()
            self.examples += elements

    def getCandidateData(self,drug,element):
        selectedDrug = self.candidates[drug]
        selectedElement = selectedDrug[element]
        return selectedElement

    def getExamplesData(self,drug,element):
        selectedExamples = self.examples[drug]
        selectedElement = selectedExamples[element]
        return selectedElement
            
