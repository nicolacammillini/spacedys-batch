import csv

class FileFormatException(Exception):
    pass


class CSVWriter:

    def __init__(self, file):
        self.csvwriter = csv.writer(file, delimiter=',')

    def writeline(self, outputline):
        self.csvwriter.writerow(outputline)


class CSVReader:
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
        return CSVReader(file)
    else:
        raise NotImplementedError('Just CSV files named \'inputfile.csv\'')


def get_writer_for_file(file):
    if file.name == 'outputfile.csv':
        return CSVWriter(file)
    else:
        raise NotImplementedError('Just CSV files named \'outputfile.csv\'')


def do_computation(inputline):
    return inputline


errors = []

try:
    with open('inputfile.csv') as inputfile, open('outputfile.csv', 'w') as outputfile:

        reader = get_reader_for_file(inputfile)
        writer = get_writer_for_file(outputfile)

        for inputline in reader:

            # dummy computation on a line of input:
            # just writing same line with different format
            # Please note computation is made on lists: no
            # dependencies on input-output format! That is
            # an implementation detail.
            outputline = do_computation(inputline)

            writer.writeline(outputline)

except FileFormatException as ffe:
    errors.append(ffe)
except IOError as ioe:
    errors.append(ioe)
finally:
    print('Errors encountered...')
    print(errors)
