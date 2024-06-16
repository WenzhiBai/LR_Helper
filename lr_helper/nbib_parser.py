import re

def extract_doi_from_nbib(file_path):
    doi_list = []

    # construct regular expression
    doi_pattern = re.compile(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)\s*\[doi\]', re.IGNORECASE)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # use regular expression to match rows that contain DOI
        matches = doi_pattern.findall(content)
        
        # remove duplicates
        doi_list = set(matches)
    
    return doi_list
