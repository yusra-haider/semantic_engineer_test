# Application test: Semantic Data Engineer

This is the test for applicants of the Semantic Data Engineer position at EBI, March 2022.

The test contains two major sections:

1. A programming exercise to determine your level of python-based development.
2. A questionnaire with a few questions.

We expect you to edit the following 5 files. Any additional files will be ignored by the reviewers.

1. cli.py (containing the code for the CLI interface)
1. pheno.py (containing the code with the actual method)
1. test_pheno.py (containing the code testing the method in pheno.py)
1. requirements.txt (containing a list of all requirements for your project)
1. knowledge_test.md (containing the your responses to our questions to test your understanding, formatted in markdown)

*SUBMISSION*: _Please send us the entire project directory as a zip file, excluding any cached or temporary files_.

## Practical test: Access BioLink API and compute Semantic Similarity

In this test, we ask you to do the following:

1. Implements a method `compute_phenotype_similarity(diseases: list[str])->pd.DataFrame` that
   - takes as an input a list of diseases
   - Accesses the BioLink API (https://api.monarchinitiative.org/api/) to obtain all phenotypes associated with each disease in that list
   - computes a pairwise Jaccard score between all diseases (even if you do not know what a Jaccard score is right now, you should be able to find out)
   - return a pandas DataFrame 
     - with four columns: `disease_1`, `disease_2`, `jaccard` (see example below)
     - for each disease pair (if you include MONDO:0007947 | MONDO:0013426, you should _not_ include MONDO:0013426 | MONDO:0007947)
     - the `compute_phenotype_similarity()` method should be implement in `pheno/pheno.py`.
1. Implements a `test` (e.g. pytest - this is up to you) for the method `compute_phenotype_similarity()`
   - The tests should be implemented in `tests/test_pheno.py`
   - The details are up to you - use whatever testing framework you prefer.
1. Develop a Command Line Interface (CLI) that 
   - takes as an input a text file with a list of disease identifiers
   - executes the method above (`compute_phenotype_similarity()`)
   - writes the resulting pandas data frame out as a TSV file.
   - the CLI should be implement in `pheno/cli.py`.

When installing the CLI (e.g. with `pip`), this command must work:

```
pheno diseases.txt -o similarity.tsv
```

Make sure:

- add all project requirements of your project to `requirements.txt`.
- running `pheno diseases.txt -o similarity.tsv` produces a correctly formatted TSV file named `similarity.tsv`.

#### Example output

Given this list of diseases: MONDO:0007947, MONDO:0013426, MONDO:0008818

You are expected to generate a valid TSV (`similarity.tsv`) file with the following content:

| disease_1 | disease_2 | jaccard |
| --------- | --------- | ------- |
| MONDO:0007947 | MONDO:0013426 | 0.1 |
| MONDO:0007947 | MONDO:0008818 | 0.1 |
| MONDO:0013426 | MONDO:0008818 | 0.1 |

## Knowledge tests

Please provide answers to all questions in [docs/knowledge_test.md](docs/knowledge_test.md).
