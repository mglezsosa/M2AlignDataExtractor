from m2aligndataextractor.fileopeners.M2AlignFile import M2AlignFile


class FunFile(M2AlignFile):

    def __next__(self):
        """Each iteration returns a list with the three values of each line"""
        return [float(val) for val in self.open_file.__next__().strip().split('\t')]
