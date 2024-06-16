import sys
import os

# add parent directory as system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import packages
from lr_helper import merge

# define tests
def test_get_dois(file_path):
    doi_list = merge.get_dois(file_path)

    for doi in doi_list:
        print(doi)
    print("Combined DOI List:", doi_list)
    print("The Length of Combined DOI List:", len(doi_list))

    return len(doi_list)


# run tests
assert test_get_dois('tests/data/IEEE Xplore.ris') == 48        # total 48
assert test_get_dois('tests/data/Scopus.ris') == 174            # total 192 with some references without a doi
assert test_get_dois('tests/data/Web of Science.ris') == 135    # total 138 with some references without a doi
assert test_get_dois('tests/data/') == 235                      # total 235
assert test_get_dois('tests/data') == 235                       # total 235