class M2AlignFile:
    """Custom file opener (as a context manager) and iterator base class."""

    def __init__(self, filename):
        self.filename = filename
        self.open_file = open(self.filename)

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError

    def __exit__(self, *args):
        self.close()

    def close(self):
        """Closes the file"""
        self.open_file.close()
