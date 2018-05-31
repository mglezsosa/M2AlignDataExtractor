from .contracts.Searcher import Searcher


class MaximumSearcher(Searcher):
    def __init__(self, name: str, col: int):
        super(MaximumSearcher, self).__init__()
        self.name = name
        self.finds[self.name + '_seq'] = None
        self.finds[self.name + '_val'] = 0
        self.col = col

    def process_line(self, var_line: str, fun_line: str):
        col_val = fun_line[self.col]
        if not self.finds[self.name + '_seq'] or self.finds[self.name + '_val'] < col_val:
            self.finds[self.name + '_seq'] = var_line
            self.finds[self.name + '_val'] = col_val


class MedianSearcher(Searcher):
    def __init__(self, name: str, col: int):
        super(MedianSearcher, self).__init__()
        self.name = name
        self.finds[self.name + '_seq'] = None
        self.finds[self.name + '_val'] = 0
        self.col = col
        self.alignments = []
        self.values = []

    def process_line(self, var_line: str, fun_line: str):
        self.values.append((fun_line[self.col], len(self.values)))
        self.alignments.append(var_line)

    def postprocessing(self):
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
