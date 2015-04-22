from drug_database import DrugDatabase

test_class = DrugDatabase()
test_class.readCandidates('hw5db1.txt') 

for drug in range(0,43347):
    text = ''
    for element in range(0,16):
        text += str(test_class.getCandidateData(drug,element)) + '|'
    print(text)
