"""
A framework agnostic implementation for storage of MCMC draws.
"""
from .core import BackendBase, ChainMeta, RunMeta

# Backends
try:
    from .clickhouse import ClickHouseBackend
except ModuleNotFoundError:
    pass

# Adapters
try:
    from .adapters.pymc import TraceBackend
except ModuleNotFoundError:
    pass


__version__ = "0.1.0"
