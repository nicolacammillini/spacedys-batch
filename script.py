from batches import AbstractObserver, FileBatch
from fileformats import CSVWriter

class MyObserver(AbstractObserver):

    def notify(self):
        print('Observer {} notified!'.format(self.name))


class MyFileBatch(FileBatch):

    def do_computation(self, inputline):
        return inputline


filewriter = CSVWriter('outputfile.csv')
batch = MyFileBatch('inputfile.csv', filewriter)

batch.register_observer(MyObserver('One'))
batch.register_observer(MyObserver('Two'))


batch.process()

print('Errors encountered')
print(batch.errors)
