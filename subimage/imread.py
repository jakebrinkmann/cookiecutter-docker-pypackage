"""Read file paths from a filesystem or over HTTP."""

import os
import asyncio

import cv2
from loguru import logger


def imread_http(url):
    """Chunked reader over HTTP."""
    logger.debug("Read remote image {}", url)
    raise NotImplementedError("Reading over HTTP is not supported.")


async def imread_fs(path, load_in_color=False):
    """Read a file directly from disk.

    Args:
        path (str): absolute/relative path to a supported image file
        load_in_color (bool): flag to load the image in RGB [Default: False]

    Raises:
        IOError: if provided path is not found

    """
    logger.debug(f"Read local image {path}")
    if not os.path.exists(path):
        raise IOError(f"Local image not found: {path}")
    return cv2.imread(path, load_in_color)


def dispatch(uri):
    """Use different approaches depending on protocol prefix.

    Args:
        uri (str): a resource identifier, either a filesystem or URL

    Returns:
        np.array: 3-D array as read from the provided path

    """
    foo = imread_fs
    if uri.startswith(("http://", "https://")):
        foo = imread_http
    return asyncio.create_task(foo(uri))


async def imread(path):
    """Concurrent reading of image data at provided paths.

    Args:
        path (str): path to read image from
    """
    # check if image already in redis and skip it
    return await dispatch(path)
