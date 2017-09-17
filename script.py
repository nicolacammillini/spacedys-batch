from fileformats import get_reader_for_file, get_writer_for_file, FileFormatException


def do_computation(inputline):
    return inputline


errors = []

INPUTFILE = 'inputfile.csv'
OUTPUTFILE = 'outputfile.csv'

def process_batch(infile, outfile):

    try:
        with open(infile) as inputfile, open(outfile, 'w') as outputfile:

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


process_batch(INPUTFILE, OUTPUTFILE)
