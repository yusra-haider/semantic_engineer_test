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


def compute_phenotype_similarity(diseases: List[str]) -> pd.DataFrame:
    pass
