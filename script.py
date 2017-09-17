import csv

csv.register_dialect('pipe_dialect', delimiter='|')

errors = []

try:
    with open('inputfile.csv') as incsvfile, open('outputfile.csv', 'w') as outcsvfile:

        csvreader = csv.reader(incsvfile, 'pipe_dialect')
        csvwriter = csv.writer(outcsvfile, delimiter=',')

        for inputline in csvreader:

            # dummy computation on a line of input:
            # just writing same line with different format
            # Please note computation is made on lists: no
            # dependencies on input-output format! That is
            # an implementation detail.
            outputline = inputline

            csvwriter.writerow(outputline)

except csv.Error as csveo:
    errors.append(csveo)
except IOError as ioe:
    errors.append(ioe)
finally:
    print('Errors encountered...')
    print(errors)

csv.unregister_dialect('pipe_dialect')