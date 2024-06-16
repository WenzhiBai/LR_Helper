import sys
import os

# add parent directory as system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# import packages
from lr_helper import merge

def print_help():
    print("Enter according to the interactive instruction:")
    print("1. The input file or folder path refers to the file itself or folder that contains the .ris or .nbib file")
    print("2. The output file or folder path refers to the file itself or folder that will hold the results of the doi list after merging and removing duplicates")
    return

def print_dois_to_screen(doi_list):
    for doi in doi_list:
        print(doi)

def main():
    print_help()

    # get inputs
    input_path = input("Please enter the input file or folder path: ")
    output_path = input("Please enter the output file or folder path (leave empty to print to screen): ")
    
    # get dois from the input path
    doi_list = merge.get_dois(input_path)
    
    if doi_list:
        if output_path:     # output dois to the output path
            merge.save_dois_to_file(doi_list, output_path)
        else:               # output dois to the screen
            print("DOI List:")
            print_dois_to_screen(doi_list)
            print("The Length of DOI List:", len(doi_list))

    else:
        print("No DOIs found.")

if __name__ == "__main__":
    main()
