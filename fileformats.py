import csv

class FileFormatException(Exception):
    pass


class CSVWriter:

    def __init__(self, file):
        self.csvwriter = csv.writer(file, delimiter=',')

    def writeline(self, outputline):
        self.csvwriter.writerow(outputline)


class CSVPipeReader:
    """ Class implemnting iterator protocol.
        Unregistering of dialect missing"""
    def __init__(self, file):
        csv.register_dialect('pipe_dialect', delimiter='|')
        self.csvreader = csv.reader(file, 'pipe_dialect')
    
    def __iter__(self):
        return self

    def __next__(self):
        
        try:
            next = self.csvreader.__next__()
        except csv.Error as csve:
            raise FileFormatException from csve

        return next


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

