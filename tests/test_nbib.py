import sys
import os

# add parent directory as system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import packages
from lr_helper import nbib_parser

# define tests
def test_extract_doi_from_nbib(file_path):
    doi_list = nbib_parser.extract_dois_from_nbib(file_path)
    print('\n'+file_path)
    for doi in doi_list:
        print(doi)
    return len(doi_list)


# run tests
assert test_extract_doi_from_nbib('tests/data/PubMed.nbib') == 84   # total 84
