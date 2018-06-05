import unittest
from m2aligndataextractor import DataExtractor
from m2aligndataextractor.searchers import *

class DataExtractorTest(unittest.TestCase):

    def setUp(self):
        self.data_extractor = DataExtractor(var_file='./VAR.BB11001.tsv', fun_file='./FUN.BB11001.tsv')

    def test_DataExtractor_add_searcher(self):
        srchr = BestStrikeSearcher()
        self.data_extractor.add_searcher(srchr)
        self.assertEqual(self.data_extractor._searchers, [srchr])

    def test_DataExtractor_all_objectives(self):
        finds = self.data_extractor.add_searcher(BestStrikeSearcher()) \
            .add_searcher(BestTCSearcher()) \
            .add_searcher(BestSPSearcher()) \
            .add_searcher(MedianStrikeSearcher()) \
            .add_searcher(MedianTCSearcher()) \
            .add_searcher(MedianSPSearcher()) \
            .extract()
        self.assertEqual({
            'Best_strike_seq': """>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY-IPP---------KGE
>1j46_A
------MQDRVKRPMNAFIVWSRDQRRKMALENPRMR-NS-EISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHPEMS-NL-DLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
--------MHIKKPLNAFMLYMKEMRANVVAES-TLK-ESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK
""",
            'Best_strike_val': 2.6123489833194524,
            'Best_tc_seq': """>1aab_
------GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY----------IPPKGE
>1j46_A
------MQDRVKRP---MNAFIVWSRDQRRKMALENPR--MRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKP---LTPYFRFFMEKRAKYAKLHPE--MSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
--------MHIKKP---LNAFMLYMKEMRANVVAESTLKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKK--KKRKREK
""",
            'Best_tc_val': 4.040404040404041,
            'Best_sp_seq': """>1aab_
GK---GDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY--------IPPKGE
>1j46_A
MQ------DRVKRPMNAFIVWSRDQRRKMALENPR--MRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP-RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHPE--MSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH-PDLIQNAKK
>2lef_A
MHIKKPLNAFMLYMKEMRANVVAESTL--KESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRK------REK
""",
            'Best_sp_val': 91.75531914893618,
            'Median_strike_val': 2.5550908331047784,
            'Median_strike_seq': """>1aab_
------GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY---------IP-----PKG-E
>1j46_A
------MQDRVKRP---MNAFIVWSRDQRRKMALENPRMR-NS-EISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP--------RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKP---LTPYFRFFMEKRAKYAKLHPEMS-NL-DLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH--PDLI------QNAKK
>2lef_A
--------MHIKKP---LNAFMLYMKEMRANVVAES-TLK-ESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNY-----GKKKKRKREK
""",
            'Median_tc_val': 2.0833333333333335,
            'Median_tc_seq': """>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY----------IPPKGE
>1j46_A
---MQDRVKRP---MNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHP--EMSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
-----MHIKKP---LNAFMLYMKEMRANVVAEST--LKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK
""",
            'Median_sp_val': 89.84375,
            'Median_sp_seq': """>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY----------IPPKGE
>1j46_A
---MQDRVKRP---MNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHP--EMSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
-----MHIKKP---LNAFMLYMKEMRANVVAEST--LKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK
"""
        }, finds)
