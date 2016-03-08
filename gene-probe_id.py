from os import walk
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

# Parse through dataset to see if matching Probe ID exists and write to new dataset
outputDataset = open("OutputDataset.csv", "w")
for line in baseDataset:
    datasetLine = line.split('\t')
    for item in geneProbe_ID:
        if item in datasetLine:
            datasetLine.append(str(geneProbe_ID[item]))
            print(datasetLine)
            for item2 in datasetLine:
                outputDataset.write(item2 + ',')
