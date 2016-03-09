# Script to combine Probe and Gene ID :)
import os.path
import sys

print('Input is case and space sensitive! Including file extension: \'.csv\', \'.txt\', etc...')
print('----====----')

# Attempt to open the baseCSV file with gene and probe id's (throw exception and quit if file cannot be found, or opened)
baseCSVFile = input('Enter filename of Probe/Gene ID\'s: ')
if os.path.isfile(baseCSVFile) is True:
    pass
###### FOR DEBUGGING ONLY ######
elif baseCSVFile == 'skip':
    pass
################################
else:
    sys.exit('Input file could not be found, aborting script')
while True:
    try:
        ###### FOR DEBUGGING ONLY ######
        if baseCSVFile == 'skip':
            break;
        ################################
        baseCsv = open(baseCSVFile)
        break;
    except OSError:
        sys.exit('File cannot be opened, please check case sensitivity and file extension')
        break;
print('input file is: ' + baseCSVFile)
print('----====----')
# Check for type of file (comma or tab)
tabOrComma = input('Is the dataset file TAB or COMMA delimited? (T or Tab, C or Comma): ')
print('Dataset file is delimited by: ' + tabOrComma + 's')
print('----====----')
# Attempt to open the baseDataset file (throw exception and quit if file cannot be found or opened)
baseDatasetFile = input('Enter filename of Dataset: ')
if os.path.isfile(baseDatasetFile) is True:
    pass
###### FOR DEBUGGING ONLY ######
elif baseDatasetFile == 'skip':
    pass
################################
else:
    sys.exit('Input file could not be found, aborting script')
while True:
    try:
        ###### FOR DEBUGGING ONLY ######
        if baseDatasetFile == 'skip':
            break;
        ################################
        baseDataset = open(baseDatasetFile, 'r+')
        break;
    except OSError:
        sys.exit('File cannot be opened, please check case sensitivity and file extension')
        break;
print('dataset file is: ' + baseDatasetFile)
print('----====----')

# Write probe-gene ID to hash table
geneProbe_ID = {'Probe_ID':'Gene_Name'}
for line in baseCsv:
    key_value = line.split(',')
    geneProbe_ID[key_value[0]] = key_value[1]

# Write probe-gene ID to file
if 't' or 'tab' in lower(tabOrComma):
    # Parse through dataset to see if matching Probe ID exists and write to new dataset (TAB DELIMITED)
    outputDataset = open("OutputDataset.csv", "w")
    for line in baseDataset:
        tempLine = line.rstrip('\n')
        datasetLine = tempLine.split('\t')
        for item in geneProbe_ID:
            if item in datasetLine:
                datasetLine.append(str(geneProbe_ID[item]))
                print(datasetLine)
                for item2 in datasetLine:
                    if '\n' in item2:
                        outputDataset.write(item2)
                    else:
                        outputDataset.write(item2 + ',')
elif 'c' or 'comma' in lower(tabOrComma):
    # Parse through dataset to see if matching Probe ID exists and write to new dataset (COMMA DELIMITED)
    outputDataset = open("OutputDataset.csv", "w")
    for line in baseDataset:
        tempLine = line.rstrip('\n')
        datasetLine = tempLine.split('\t')
        for item in geneProbe_ID:
            if item in datasetLine:
                datasetLine.append(str(geneProbe_ID[item]))
                print(datasetLine)
                for item2 in datasetLine:
                    if '\n' in item2:
                        outputDataset.write(item2)
                    else:
                        outputDataset.write(item2 + ',')
