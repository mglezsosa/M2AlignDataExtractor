import unittest
from m2aligndataextractor.fileopeners import *
from m2aligndataextractor.searchers import *


class SearcherTest(unittest.TestCase):
    def setUp(self):
        self.var_file = VarFile('./VAR.BB11001.tsv')
        self.fun_file = FunFile('./FUN.BB11001.tsv')

    def tearDown(self):
        self.var_file.close()
        self.fun_file.close()

    def test_should_BestStrikeSearcher_return_best_strike_value_and_seq(self):
        bss = BestStrikeSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            bss.process_line(var_line=var_line, fun_line=fun_line)
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
            'Best_strike_val': 2.6123489833194524
        }, bss.finds)

    def test_should_BestTCSearcher_return_best_tc_value_and_seq(self):
        btcs = BestTCSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            btcs.process_line(var_line=var_line, fun_line=fun_line)
        self.assertEqual({
            'Best_tc_seq': """>1aab_
------GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY----------IPPKGE
>1j46_A
------MQDRVKRP---MNAFIVWSRDQRRKMALENPR--MRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKP---LTPYFRFFMEKRAKYAKLHPE--MSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
--------MHIKKP---LNAFMLYMKEMRANVVAESTLKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKK--KKRKREK
""",
            'Best_tc_val': 4.040404040404041
        }, btcs.finds)

    def test_should_BestSPSearcher_return_best_sp_value_and_seq(self):
        bsps = BestSPSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            bsps.process_line(var_line=var_line, fun_line=fun_line)
        self.assertEqual({
            'Best_sp_seq': """>1aab_
GK---GDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY--------IPPKGE
>1j46_A
MQ------DRVKRPMNAFIVWSRDQRRKMALENPR--MRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP-RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHPE--MSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH-PDLIQNAKK
>2lef_A
MHIKKPLNAFMLYMKEMRANVVAESTL--KESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRK------REK
""",
            'Best_sp_val': 91.75531914893618
        }, bsps.finds)

    def test_should_MedianStrikeSearcher_return_median_strike_value_and_seq(self):
        mss = MedianStrikeSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            mss.process_line(var_line=var_line, fun_line=fun_line)
        mss.postprocessing()
        self.assertEqual({
            'Median_strike_val': 2.5550908331047784,
            'Median_strike_seq': """>1aab_
------GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY---------IP-----PKG-E
>1j46_A
------MQDRVKRP---MNAFIVWSRDQRRKMALENPRMR-NS-EISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP--------RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKP---LTPYFRFFMEKRAKYAKLHPEMS-NL-DLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH--PDLI------QNAKK
>2lef_A
--------MHIKKP---LNAFMLYMKEMRANVVAES-TLK-ESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNY-----GKKKKRKREK
"""
        }, mss.finds)

    def test_should_MedianTCSearcher_return_median_strike_value_and_seq(self):
        mtcs = MedianTCSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            mtcs.process_line(var_line=var_line, fun_line=fun_line)
        mtcs.postprocessing()
        self.assertEqual({
            'Median_tc_val': 2.0833333333333335,
            'Median_tc_seq': """>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTY----------IPPKGE
>1j46_A
---MQDRVKRP---MNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP---RRKAKMLPK
>1k99_A
MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHP--EMSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDH---PDLIQNAKK
>2lef_A
-----MHIKKP---LNAFMLYMKEMRANVVAEST--LKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK
"""
        }, mtcs.finds)

    def test_should_MedianSPSearcher_return_median_strike_value_and_seq(self):
        msps = MedianSPSearcher()
        for var_line, fun_line in zip(self.var_file, self.fun_file):
            msps.process_line(var_line=var_line, fun_line=fun_line)
        msps.postprocessing()
        self.assertEqual({
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
        }, msps.finds)
