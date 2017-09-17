from batches import FileBatch

class MyFileBatch(FileBatch):

    def do_computation(self, inputline):
        return inputline


INPUTFILE = 'inputfile.csv'
OUTPUTFILE = 'outputfile.csv'

batch = MyFileBatch()

batch.process(INPUTFILE, OUTPUTFILE)
