from batches import FileBatch

INPUTFILE = 'inputfile.csv'
OUTPUTFILE = 'outputfile.csv'

batch = FileBatch()

batch.process(INPUTFILE, OUTPUTFILE)
