class Searcher:
    """
    Represents a search over M2Align files

    It can be used as a "command" (command pattern) in order
    to prepare different searches in only one file read.
    These commands are added to a DataExtractor instance.
    """

    def __init__(self):
        self.finds = {}

    def preprocessing(self):
        """Necessary actions before the search"""
        pass

    def process_line(self, var_line: str, fun_line: str) -> None:
        """
        Does necessary actions on lines while iterate over files
        :param var_line: path to m2align var file.
        :param fun_line: path to m2align fun file.
        """
        raise NotImplementedError

    def postprocessing(self):
        """Necessary actions after the search"""
        pass
