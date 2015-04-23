from drug_database import DrugDatabase

# Initializes a test DrugDatabase class
test_class = DrugDatabase()

# Reads both candidate and example files in
test_class.readCandidates('hw5db1.txt') 
test_class.readExamples('hw5db2.txt')

# Print output for both files

print('Reading and formatting candidate data')

for drug in range(0,43347):
    text = ''
    for element in range(0,16):
        text += str(test_class.getCandidateData(drug,element)) + '|'
    print(text)

print('Reading and formatting example data')

for example in range(0,8):
    text = ''
    for element in range(0,8):
        text += str(test_class.getExampleData(example,element)) + '|'
    print(text)

print('If displayed data matches data files, then test passes')
