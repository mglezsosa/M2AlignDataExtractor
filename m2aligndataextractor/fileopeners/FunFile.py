class FunFile():

    def __init__(self, filename):
        self.filename = filename
        self.open_file = open(self.filename)

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        return [float(val) for val in self.open_file.__next__().strip().split('\t')]

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.open_file.close()
