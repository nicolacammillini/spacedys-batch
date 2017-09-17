import csv

class CSVWriter:

    def __init__(self, file):
        self.csvwriter = csv.writer(file, delimiter=',')

    def writeline(self, outputline):
        self.csvwriter.writerow(outputline)


def do_computation(inputline):
    return inputline



csv.register_dialect('pipe_dialect', delimiter='|')

errors = []

try:
    with open('inputfile.csv') as incsvfile, open('outputfile.csv', 'w') as outcsvfile:

        csvreader = csv.reader(incsvfile, 'pipe_dialect')
        csvwriter = CSVWriter(outcsvfile)

        for inputline in csvreader:

            # dummy computation on a line of input:
            # just writing same line with different format
            # Please note computation is made on lists: no
            # dependencies on input-output format! That is
            # an implementation detail.
            outputline = do_computation(inputline)

            csvwriter.writeline(outputline)

except csv.Error as csveo:
    errors.append(csveo)
except IOError as ioe:
    errors.append(ioe)
finally:
    print('Errors encountered...')
    print(errors)

csv.unregister_dialect('pipe_dialect')
