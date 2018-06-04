from m2aligndataextractor.fileopeners import FunFile, VarFile
from m2aligndataextractor.searchers.contracts import Searcher


class DataExtractor:
    """
    Orchestrator class of the searchers.

    Can do several searches at the same read of the file.
    """

    def __init__(self, var_file: str, fun_file: str, searchers: list = None):
        """
        :param var_file: path to m2align var file.
        :param fun_file: path to m2align fun file.
        :param searchers: list of searchers instances.
        """
        if searchers is None:
            searchers = []
        self.var_file = var_file
        self.fun_file = fun_file
        self._searchers = searchers

    def add_searcher(self, searcher: Searcher):
        """
        Add a searcher to the data extractor.
        :param searcher: new searcher instance.
        :return: self instance.
        """
        self._searchers.append(searcher)
        return self

    def _preprocessing(self) -> None:
        """
        Executes preprocessing function on every searcher.
        """
        for searcher in self._searchers:
            searcher.preprocessing()

    def _postprocessing(self) -> None:
        """
        Executes postprocessing function on every searcher.
        """
        for searcher in self._searchers:
            searcher.postprocessing()

    def _collect(self) -> dict:
        """
        Collects all finds after the search.
        :return: dictionary with every find.
        """
        finds = {}
        for searcher in self._searchers:
            finds.update(searcher.finds)
        return finds

    def extract(self) -> dict:
        """
        Executes the complete search.
        :return: dictionary with all finds.
        """
        self._preprocessing()
        self._search()
        self._postprocessing()
        return self._collect()

    def _search(self) -> None:
        """
        Process every aligment and values with each searcher.
        """
        with VarFile(self.var_file) as var_file:
            with FunFile(self.fun_file) as fun_file:
                for var_line, fun_line in zip(var_file, fun_file):
                    for searcher in self._searchers:
                        searcher.process_line(var_alignment=var_line, fun_values=fun_line)
