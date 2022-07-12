"""
Please develop a Command Line Interface (CLI) that
   - takes as an input a text file with a list of disease identifiers
   - executes the `compute_phenotype_similarity()` method defined in pheno.py
   - writes the resulting pandas data frame out as a TSV file.
"""

import argparse
from pheno.pheno import parse_input_file


def main():
    """
    Parse user-provided command-line arguments.
    """
    parser = argparse.ArgumentParser()
    # todo: double check the required attr
    parser.add_argument('--input_file', type=str, help='path to a text file with a list of disease identifiers')

    args = parser.parse_args()

    if args.input_file:
        parse_input_file(input_file_name=args.input_file)

    else:
        raise Exception("");


if __name__ == "__main__":
    main()





# pheno.py
# Import the argparse library
# import argparse
#
# import os
# import sys
# import pheno
#
# # Create the parser
# my_parser = argparse.ArgumentParser(description='takes as an input a text file with a list of disease identifiers')
#
# # Add the arguments
#
# my_parser.add_argument('name')
#
# # Execute the parse_args() method
# args = my_parser.parse_args()
#
# filename = args.name
#
# df = compute_phenotype_similarity(filename)
#
# df.to_csv('example.tsv', sep="\t")
