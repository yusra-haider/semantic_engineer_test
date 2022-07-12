"""
Please implement the method `compute_phenotype_similarity(diseases: list[str])->pd.DataFrame` that
   - takes as an input a list of diseases
   - accesses the BioLink API (https://api.monarchinitiative.org/api/) to obtain all phenotypes associated with each disease in that list
   - computes a pairwise Jaccard score between all diseases (even if you do not know what a Jaccard score is right now, you should be able to find out)
   - return a pandas DataFrame
     - with four columns: `disease_1`, `disease_2`, `jaccard`
     - for each disease pair (if you include MONDO:0007947 | MONDO:0013426, you should _not_ include MONDO:0013426 | MONDO:0007947)
"""

import pandas as pd
from typing import List


def parse_input_file(input_file_name) -> []:
    # todo: parse the input file to get list of diseases
    # returning dummy list for now
    print(input_file_name)
    return [1,2,3]


def compute_phenotype_similarity(name):
    handle = open(name)
    df = pd.DataFrame([get_list_element(disease) for disease in handle]).T
    handle = open(name)
    df.columns = [disease.rstrip() for disease in handle]
    df_intersection = get_intersection(df)
    return df_intersection


def get_associations(line):
    # compute_from_line(line)
    servernew = 'https://api.monarchinitiative.org/api/bioentity/disease/'
    id = line.rstrip()
    teststring = servernew + id + '/phenotypes'
    r = requests.get(teststring)
    decode = r.json()
    associations = decode['associations']
    return id, associations


def give_element(id, associations):
    return numpy.unique([elements['object']['label'] for elements in associations])


def get_list_element(line):
    id, associations = get_associations(line)
    return give_element(id, associations)


def get_intersection(df):
    df_out = pd.DataFrame()
    # sum_AuB = []

    for i, col in enumerate(df.columns):
        # making a list of all column which has to be compared with col
        other_col = [x for x in df.columns[i + 1:]]
        for oCol in other_col:
            # using a set we can find a intersection between 2 list and count them
            Intersection = len(set(df[col].values.tolist()).intersection(df[oCol].values.tolist()))
            sum_A = len(set(df[col].tolist()))
            sum_B = len(set(df[oCol].tolist()))
            sum_AuB = sum_A + sum_B - Intersection
            Jaccard = Intersection / sum_AuB
            # storing all Intersections with their respective column in separate df
            df_out = df_out.append([(col, oCol, Jaccard)], sort=True, ignore_index=True)

    df_out.columns = ['disease_1', 'disease_2', 'Jaccard']
    df_out.sort_values(by=['Jaccard'], ascending=[False], inplace=True)

    return df_out
