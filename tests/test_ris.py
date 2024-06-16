import sys
import os

# add parent directory as system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import packages
from lr_helper import ris_parser

# define tests
def test_extract_doi_from_ris(file_path):
    doi_list = ris_parser.extract_dois_from_ris(file_path)
    print('\n'+file_path)
    for doi in doi_list:
        print(doi)
    return len(doi_list)


# run tests
assert test_extract_doi_from_ris('tests/data/IEEE Xplore.ris') == 48        # total 48
assert test_extract_doi_from_ris('tests/data/Scopus.ris') == 174            # total 192 with some references without a doi
assert test_extract_doi_from_ris('tests/data/Web of Science.ris') == 135    # total 138 with some references without a doi