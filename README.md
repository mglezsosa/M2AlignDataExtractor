# M2Align Data Extractor

Data extractor for [M2Align](https://github.com/KhaosResearch/M2Align) output files: best strike score, 
best score for conserved columns, best score for non-gaps pecentage and their respective medians.

```bash
Usage: m2aligndext [OPTIONS] FUNFILE VARFILE

Options:
  --help  Show this message and exit.
```

## Dependencies
* Python 3.x
* Pip

## Installation
1. Clone project with git:
    ```bash
    git clone https://github.com/mglezsosa/m2aligndataextractor.git
    ```
1. Install
    ```bash
    cd m2aligndataextractor && make
    ```
    
    or
    
    ```bash
    cd tsv2xml &&  pip install -r requirements.txt && pip install -e .
    ```