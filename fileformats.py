import csv

from batches import FileFormatException


class CSVWriter:

    def __init__(self, filename):
        self.fileobj = open(filename, 'w')
        self.csvwriter = csv.writer(self.fileobj, delimiter=',')

    def writeline(self, outputline):
        self.csvwriter.writerow(outputline)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self.fileobj.__exit__(type, value, traceback)


class CSVPipeReader:
    """ Class implemnting iterator protocol.
        Unregistering of dialect missing"""
    def __init__(self, filename):
        csv.register_dialect('pipe_dialect', delimiter='|')
        self.fileobj = open(filename)
        self.csvreader = csv.reader(self.fileobj, 'pipe_dialect')

    def __iter__(self):
        return self

    def __next__(self):

        try:
            next = self.csvreader.__next__()
        except csv.Error as csve:
            raise FileFormatException from csve

        return next
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return self.fileobj.__exit__(type, value, traceback)


def get_reader_for_file(file):
    if file.name == 'inputfile.csv':
        return CSVPipeReader(file)
    else:
        raise NotImplementedError('Just CSV files named \'inputfile.csv\'')


def get_writer_for_file(file):
    if file.name == 'outputfile.csv':
        return CSVWriter(file)
    else:
        raise NotImplementedError('Just CSV files named \'outputfile.csv\'')
