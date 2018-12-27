"""Utilities for host system interaction."""

import sys
import asyncio
import logging

from loguru import logger


def setup_logging(verbosity=0):
    """Configure logging to STDOUT, color-coding messages by severity level.

    Args:
        level (int): minimum logging output level to sink

    """
    log_level = max(logging.DEBUG, logging.WARNING - logging.DEBUG * verbosity)
    opts = dict(
        sink=sys.stdout,
        format=(
            "<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g> "
            "| <level>{level:<8}</level>| "
            "<level>{message}</level>"
        ),
        level=log_level,
        backtrace=verbosity > 2,
    )
    logger.configure(handlers=[opts])


def sync(func, paths):
    """Synchronize results from concurent functions."""
    futures = map(func, paths)
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*futures))
    loop.close()
    return results
