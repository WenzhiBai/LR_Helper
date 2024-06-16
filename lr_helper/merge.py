import os

from . import nbib_parser, ris_parser

def get_dois_from_file(file_path):
    # get dois from files in different formats by different parsers
    if file_path.endswith('.ris'):
        return ris_parser.extract_dois_from_ris(file_path)
    elif file_path.endswith('.nbib'):
        return nbib_parser.extract_dois_from_nbib(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return []

def get_dois_from_folder(folder_path):
    all_dois = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            dois = get_dois_from_file(file_path)
            all_dois.update(dois)
    return list(all_dois)

def get_dois(input_path):
    # get dois from a file or a directory
    if os.path.isfile(input_path):
        return get_dois_from_file(input_path)
    elif os.path.isdir(input_path):
        return get_dois_from_folder(input_path)
    else:
        print(f"Invalid input path: {input_path}")
        return []

def save_dois_to_file(doi_list, output_path):
    if os.path.isdir(output_path):
        # if it is a directory, the default file name is used
        output_file = os.path.join(output_path, "doi_list.txt")
    else:
        # if it is a file path, use it directly
        output_file = output_path

    # save the doi list to the file
    with open(output_file, 'w') as f:
        for doi in doi_list:
            f.write(f"{doi}\n")
    print(f"DOI list saved to {output_file}")

