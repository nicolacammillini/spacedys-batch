from batches import FileBatch

class MyFileBatch(FileBatch):

    def do_computation(self, inputline):
        return inputline


batch = MyFileBatch('inputfile.csv', 'outputfile.csv')

batch.process()

print('Errors encountered')
print(batch.errors)