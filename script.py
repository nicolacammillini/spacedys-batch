import csv

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
        return self.csvreader.__next__()


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
    with open('inputfile.csv') as incsvfile, open('outputfile.csv', 'w') as outcsvfile:

        reader = get_reader_for_file(incsvfile)
        writer = get_writer_for_file(outcsvfile)

        for inputline in reader:

            # dummy computation on a line of input:
            # just writing same line with different format
            # Please note computation is made on lists: no
            # dependencies on input-output format! That is
            # an implementation detail.
            outputline = do_computation(inputline)

            writer.writeline(outputline)

except csv.Error as csveo:
    errors.append(csveo)
except IOError as ioe:
    errors.append(ioe)
finally:
    print('Errors encountered...')
    print(errors)
