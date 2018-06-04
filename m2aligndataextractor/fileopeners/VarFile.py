from m2aligndataextractor.fileopeners.M2AlignFile import M2AlignFile


class VarFile(M2AlignFile):

    def __next__(self):
        """Each iteration returns a sequence aligment fragment (consecutive lines until double linebreak)"""
        next_alignment = ''
        for line in self.open_file:
            if line == '\n' and next_alignment:
                return next_alignment.lstrip()
            else:
                next_alignment += line
        raise StopIteration
