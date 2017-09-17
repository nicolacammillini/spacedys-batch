from batches import AbstractObserver, FileBatch


class MyObserver(AbstractObserver):

    def notify(self):
        print('Observer {} notified!'.format(self.name))


class MyFileBatch(FileBatch):

    def do_computation(self, inputline):
        return inputline


batch = MyFileBatch('inputfile.csv', 'outputfile.csv')

batch.register_observer(MyObserver('One'))
batch.register_observer(MyObserver('Two'))


batch.process()

print('Errors encountered')
print(batch.errors)
