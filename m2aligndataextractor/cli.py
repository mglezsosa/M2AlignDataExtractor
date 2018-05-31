#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from m2aligndataextractor import DataExtractor
from m2aligndataextractor.searchers import *


def main(fun: str, var: str):
    finds = DataExtractor(var_file=var, fun_file=fun) \
        .add_searcher(BestStrikeSearcher()) \
        .add_searcher(BestSPSearcher()) \
        .add_searcher(BestTCSearcher()) \
        .add_searcher(MedianStrikeSearcher()) \
        .add_searcher(MedianSPSearcher()) \
        .add_searcher(MedianTCSearcher()) \
        .extract()

    for name, body in finds.items():
        with open(name, 'w') as f:
            f.write(str(body))


@click.command()
@click.argument('fun', metavar='FUNFILE')
@click.argument('var', metavar='VARFILE')
def cli(fun: str, var: str):
    main(fun, var)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
