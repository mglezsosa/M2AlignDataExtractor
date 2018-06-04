from .contracts.Searcher import Searcher


class MaximumSearcher(Searcher):
    """Base class for maximum value searches (and associated sequence)"""
    def __init__(self, name: str, col: int):
        """
        :param name: Name of the search objective.
        :param col: Target column of the fun file.
        """
        super(MaximumSearcher, self).__init__()
        self.name = name
        self.finds[self.name + '_seq'] = None
        self.finds[self.name + '_val'] = 0
        self.col = col

    def process_line(self, var_alignment: str, fun_values: list) -> None:
        """
        Updates the maximum value and associated sequence if value is greater
        :param var_alignment: Next aligment in m2align var file.
        :param fun_values: Next values in m2align fun file.
        """
        col_val = fun_values[self.col]
        if not self.finds[self.name + '_seq'] or self.finds[self.name + '_val'] < col_val:
            self.finds[self.name + '_seq'] = var_alignment
            self.finds[self.name + '_val'] = col_val


class MedianSearcher(Searcher):
    """Base class for compute median searches (value and sequence)"""
    def __init__(self, name: str, col: int):
        """
        :param name: Name of the search objective.
        :param col: Target column of the fun file.
        """
        super(MedianSearcher, self).__init__()
        self.name = name
        self.finds[self.name + '_seq'] = None
        self.finds[self.name + '_val'] = 0
        self.col = col
        self.alignments = []
        self.values = []

    def process_line(self, var_aligment: str, fun_values: list) -> None:
        """
        Stores the values in order to extract the median in postprocessing function.
        :param var_alignment: Next aligment in m2align var file.
        :param fun_values: Next values in m2align fun file.
        """
        self.values.append((fun_values[self.col], len(self.values)))
        self.alignments.append(var_aligment)

    def postprocessing(self) -> None:
        """
        Extract the median of the values and the associated sequence.
        Picks the n/2 nth sequence (n/2 - 1 nth if even elements) even if there is a tie.
        """
        self.values.sort()
        self.finds[self.name + '_seq'] = self.alignments[self.values[int((len(self.values) - 1) / 2)][1]]
        self.finds[self.name + '_val'] = self.values[int((len(self.values) - 1) / 2)][0]


class BestStrikeSearcher(MaximumSearcher):
    """Search for the best STRIKE aligment"""
    def __init__(self):
        super(BestStrikeSearcher, self).__init__(name='Best_strike', col=0)


class BestTCSearcher(MaximumSearcher):
    """Search for the best TC aligment"""
    def __init__(self):
        super(BestTCSearcher, self).__init__(name='Best_tc', col=1)


class BestSPSearcher(MaximumSearcher):
    """Search for the best SP aligment"""
    def __init__(self):
        super(BestSPSearcher, self).__init__(name='Best_sp', col=2)


class MedianStrikeSearcher(MedianSearcher):
    """Search for the median of the alignments STRIKE values"""
    def __init__(self):
        super(MedianStrikeSearcher, self).__init__(name='Median_strike', col=0)


class MedianTCSearcher(MedianSearcher):
    """Search for the median of the alignments TC values"""
    def __init__(self):
        super(MedianTCSearcher, self).__init__(name='Median_tc', col=1)


class MedianSPSearcher(MedianSearcher):
    """Search for the median of the alignments SP values"""
    def __init__(self):
        super(MedianSPSearcher, self).__init__(name='Median_sp', col=2)
