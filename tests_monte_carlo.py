"""Perform Monte Carlo tests."""

# import cProfile
# import pstats
# import io

from trempy.tests.test_montecarlo import pertubation_robustness_single
from trempy.tests.test_montecarlo import pertubation_robustness_all

perturb_all = True

version = 'nonstationary'
label = 'y_scale'
num_agents = 1000
optimizer = 'SCIPY-L-BFGS-B'

# Start profiling
# pr = cProfile.Profile()
# pr.enable()

# ... do something ...

if perturb_all is True:
    pertubation_robustness_all(version=version, num_agents=num_agents, optimizer=optimizer)
else:
    pertubation_robustness_single(version=version, label=label, num_agents=num_agents,
                                  optimizer=optimizer)

# # Stop profiling and report stats
# pr.disable()
# s = io.StringIO()
# sortby = 'cumulative'
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats(15)
# print(s.getvalue())

# ps.dump_stats('program.prof')
