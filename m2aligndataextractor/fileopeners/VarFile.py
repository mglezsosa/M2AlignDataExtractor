class VarFile():

    def __init__(self, filename):
        self.filename = filename
        self.open_file = open(self.filename)

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        next_alignment = ''
        for line in self.open_file:
            if line == '\n' and next_alignment:
                return next_alignment.lstrip()
            else:
                next_alignment += line
        raise StopIteration

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.open_file.close()
