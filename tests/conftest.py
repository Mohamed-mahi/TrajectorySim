import os
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend
os.environ["PYTEST_RUNNING"] = "1"  # Flag to indicate tests are running

# This file ensures that Matplotlib uses a non-interactive backend ("Agg") during testing.
# It prevents Matplotlib from opening GUI windows or interactive plots when running tests,
# making the tests more stable and compatible with automated environments like pytest.
