from abc import abstractmethod

from fileformats import (FileFormatException, get_reader_for_file)


class FileBatch:

    def __init__(self, infile, filewriter):
        self.observers = []
        self.errors = []
        self.infile = infile
        self.filewriter = filewriter

    def do_computation(self, inputline):
        pass

    def process(self):

        try:
            with open(self.infile) as inputfile, self.filewriter as outputfile:

                reader = get_reader_for_file(inputfile)

                for inputline in reader:

                    # dummy computation on a line of input:
                    # just writing same line with different format
                    # Please note computation is made on lists: no
                    # dependencies on input-output format! That is
                    # an implementation detail.
                    outputline = self.do_computation(inputline)

                    outputfile.writeline(outputline)

                    self.notify_observers()

        except FileFormatException as ffe:
            self.errors.append(ffe)
        except IOError as ioe:
            self.errors.append(ioe)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify()


class AbstractObserver:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def notify(self):
        pass
