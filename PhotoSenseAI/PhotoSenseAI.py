# --------------------------------------------------
# Name        : XXX.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/XXX
# Licence     : See licences
# --------------------------------------------------

import os
import pandas as pd
import logging
import numpy as np
from tqdm import tqdm
import datazets as dz

logger = logging.getLogger('')
[logger.removeHandler(handler) for handler in logger.handlers[:]]
console = logging.StreamHandler()
# formatter = logging.Formatter('[%(asctime)s] [XXX]> %(levelname)s> %(message)s', datefmt='%H:%M:%S')
formatter = logging.Formatter('[XXX] >%(levelname)s> %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)
logger = logging.getLogger(__name__)


class XXX():
    """XXX."""

    def __init__(self, method='xgboost', verbose='info'):
        """Initialize XXX with user-defined parameters."""
        self.method=method
        # Set the logger
        set_logger(verbose=verbose)

    def messages(self):
        """Learn the associations in the data."""
        logger.debug("Hello debug")
        logger.info("Hello info")
        logger.critical("Hello critical")
        logger.warning("Hello warning")

		# Set logger to warning-error only
        verbose = logger.getEffectiveLevel()
        set_logger(verbose=30)

        # Extract faces and eyes from image
        for i in tqdm(np.arange(0,10), disable=disable_tqdm()):
            logger.info(i)

        # Restore verbose status
        set_logger(verbose=verbose)
        return None

    def import_example(self, data='titanic', url=None, sep=','):
        """Import example dataset from github source.

        Import one of the few datasets from github source or specify your own download url link.

        Parameters
        ----------
        data : str
            Name of datasets: 'sprinkler', 'titanic', 'student', 'fifa', 'cancer', 'waterpump', 'retail'
        url : str
            url link to to dataset.

        Returns
        -------
        pd.DataFrame()
            Dataset containing mixed features.

        References
        ----------
            * https://github.com/erdogant/datazets

        """
        return dz.get(data=data, url=url, sep=sep)


# %%
def convert_verbose_to_new(verbose):
    """Convert old verbosity to the new."""
    # In case the new verbosity is used, convert to the old one.
    if verbose is None: verbose=0
    if not isinstance(verbose, str) and verbose<10:
        status_map = {
            'None': 'silent',
            0: 'silent',
            6: 'silent',
            1: 'critical',
            2: 'warning',
            3: 'info',
            4: 'debug',
            5: 'debug'}
        if verbose>=2: print('[XXX] WARNING use the standardized verbose status. The status [1-6] will be deprecated in future versions.')
        return status_map.get(verbose, 0)
    else:
        return verbose


def convert_verbose_to_old(verbose):
    """Convert new verbosity to the old ones."""
    # In case the new verbosity is used, convert to the old one.
    if verbose is None: verbose=0
    if isinstance(verbose, str) or verbose>=10:
        status_map = {
            60: 0, 'silent': 0, 'off': 0, 'no': 0, None: 0,
            40: 1, 'error': 1, 'critical': 1,
            30: 2, 'warning': 2,
            20: 3, 'info': 3,
            10: 4, 'debug': 4}
        return status_map.get(verbose, 0)
    else:
        return verbose


# %%
def get_logger():
    return logger.getEffectiveLevel()


# %%
def set_logger(verbose: [str, int] = 'info'):
    """Set the logger for verbosity messages.

    Parameters
    ----------
    verbose : [str, int], default is 'info' or 20
        Set the verbose messages using string or integer values.
        * [0, 60, None, 'silent', 'off', 'no']: No message.
        * [10, 'debug']: Messages from debug level and higher.
        * [20, 'info']: Messages from info level and higher.
        * [30, 'warning']: Messages from warning level and higher.
        * [50, 'critical']: Messages from critical level and higher.

    Returns
    -------
    None.

    > # Set the logger to warning
    > set_logger(verbose='warning')
    > # Test with different messages
    > logger.debug("Hello debug")
    > logger.info("Hello info")
    > logger.warning("Hello warning")
    > logger.critical("Hello critical")

    """
    # Set 0 and None as no messages.
    if (verbose==0) or (verbose is None):
        verbose=60
    # Convert str to levels
    if isinstance(verbose, str):
        levels = {'silent': 60,
                  'off': 60,
                  'no': 60,
                  'debug': 10,
                  'info': 20,
                  'warning': 30,
                  'error': 50,
                  'critical': 50}
        verbose = levels[verbose]

    # Show examples
    logger.setLevel(verbose)


# %%
def disable_tqdm():
    """Set the logger for verbosity messages."""
    return (True if (logger.getEffectiveLevel()>=30) else False)


# %% Main
if __name__ == "__main__":
    import XXX as XXX
    df = XXX.import_example()
    out = XXX.fit(df)
    fig,ax = XXX.plot(out)
