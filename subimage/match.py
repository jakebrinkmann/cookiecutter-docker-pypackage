"""Functionality to cross-correlate two images."""

import os
import asyncio

import cv2
import numpy as np
from loguru import logger
from skimage.feature import match_template


class SubimageMatchFailedException(Exception):
    """Custom error raised when correlation does not meet threshold."""

    pass


def reject_invalid_results(max_val, threshold):
    """Raise an exception when under a threshold.

    Args:
        max_val (float): value of correlation
        threshold (float): minimum acceptable value

    Raises:
        SubimageMatchFailedException: correlation valied

    """
    if max_val < threshold:
        msg = f"Correlation max of {max_val:1.2f} under required threshold {threshold}"
        logger.warning(msg)
        raise SubimageMatchFailedException(msg)


def skmatch(im1, im2, threshold):
    """Find correlation peaks using `Fast Normalized Cross-Correlation` in Scikit-Image.

    .. Fast Normalized Cross-Correlation:
        http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_template.html
    """
    result = match_template(im1, im2)
    max_val = np.max(result)
    reject_invalid_results(max_val, threshold)
    ij = np.unravel_index(np.argmax(result), result.shape)
    max_loc = ij[::-1]
    return max_loc


def cvmatch(im1, im2, threshold):
    """Use 2D-Convolution to perform Template Matching using OpenCV.

    .. Template Matching:
        https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
    """
    result = cv2.matchTemplate(im1, im2, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    reject_invalid_results(max_val, threshold)
    return max_loc


def match_images(im1, im2, threshold=0.65, lib="skimage"):
    """Execute chosen template match algorithm on two images.

    Args:
        im1 (np.ndarray): larger input image
        im2 (np.ndarray): smaller potential crop from input image
        threshold (float): minimum acceptable threshold for a match [Default: 0.65]
        lib (str): implementation to use [Default: skimage]

    Returns:
        tuple: the upper-left x,y location of the match

    """
    # TODO: lib should come from a configuration system
    method = {"opencv": cvmatch, "skimage": skmatch}.get(lib)
    return method(im1, im2, threshold)


def match(images):
    """Unravel datastructure for logging information, sort images by shape.

    Args:
        images (list): two element list of dicts with keys {"fname", "data"}

    """
    # Assume bigger images are the input, and smaller are the search area
    images = sorted(images, key=lambda x: x["data"].shape, reverse=True)
    try:
        top_left = match_images(images[0]["data"], images[1]["data"])
    except SubimageMatchFailedException:
        logger.warning(
            f'Image {images[1]["fname"]} is not a subimage of {images[0]["fname"]}'
        )
    else:
        logger.success(
            f'Image {images[1]["fname"]} is a subimage of {images[0]["fname"]}'
        )
        return top_left
