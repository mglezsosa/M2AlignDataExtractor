from m2aligndataextractor.fileopeners import FunFile, VarFile
from m2aligndataextractor.searchers.contracts import Searcher


class DataExtractor:

    def __init__(self, var_file: str, fun_file: str, searchers: list = None):
        if searchers is None:
            searchers = []
        self.var_file = var_file
        self.fun_file = fun_file
        self._searchers = searchers

    def add_searcher(self, searcher: Searcher):
        self._searchers.append(searcher)
        return self

    def _preprocessing(self) -> None:
        for searcher in self._searchers:
            searcher.preprocessing()

    def _postprocessing(self) -> None:
        for searcher in self._searchers:
            searcher.postprocessing()

    def _collect(self) -> dict:
        finds = {}
        for searcher in self._searchers:
            finds.update(searcher.finds)
        return finds

    def extract(self) -> dict:
        self._preprocessing()
        self._search()
        self._postprocessing()
        return self._collect()

    def _search(self) -> None:
        with VarFile(self.var_file) as var_file:
            with FunFile(self.fun_file) as fun_file:
                for var_line, fun_line in zip(var_file, fun_file):
                    for searcher in self._searchers:
                        searcher.process_line(var_line=var_line, fun_line=fun_line)
