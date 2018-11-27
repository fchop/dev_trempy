"""Test the correctness of the liklihood function at the truth."""

import pandas as pd
import os

from trempy.tests.test_montecarlo import estimate_at_truth

os.chdir('estimate_at_truth')

results = list()
for step in range(1):
    print('Step: {:>25}'.format(step))
    output = estimate_at_truth(fix_question_paras='fix_all')
    results += [output]
    print(output)

columns = ['Seed', 'fval_truth', 'fval_est', 'parameter', 'start', 'stop']
df = pd.DataFrame(results, columns=columns)
df.to_csv('monte_carlo_results.csv')
