class Searcher:
    """Represents a search over M2Align files"""

    def __init__(self):
        self.finds = {}

    def preprocessing(self):
        """Necessary actions before the search"""
        pass

    def process_line(self, var_line: str, fun_line: str) -> None:
        """Does necessary actions on lines while iterate over files"""
        raise NotImplementedError

    def postprocessing(self):
        """Necessary actions after the search"""
        pass
