"""Test under optimal conditions."""

import pandas as pd
import os

from trempy.tests.test_montecarlo import pertubation_robustness_all
from trempy.tests.test_auxiliary import visualize_modelfit

version = 'nonstationary'

# Start profiling
# pr = cProfile.Profile()
# pr.enable()

# ... do something ...
os.chdir('estimate_most_favorable')

pertubation_robustness_all(version=version, max_dist=0.75, set_std_to=5.0,
                           no_temporal_choices=False)

df_truth = pd.read_pickle(r'truth.trempy.pkl')
df_estimated = pd.read_pickle(r'stop/stop.trempy.pkl')

visualize_modelfit(df_truth, df_estimated)

# # Stop profiling and report stats
# pr.disable()
# s = io.StringIO()
# sortby = 'cumulative'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats(15)
# print(s.getvalue())

# ps.dump_stats('program.prof')
