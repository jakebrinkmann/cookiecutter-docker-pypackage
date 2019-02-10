"""Business logic to connect the subsystems."""

from itertools import combinations

from loguru import logger

from subimage import epilog
from subimage.match import match, SubimageMatchFailedException
from subimage.imread import imread
from subimage.util import setup_logging, sync


@logger.catch(message="An unexpected error has occured. See stacktrace for details.")
def run_all(images, verbose=False):
    """Check for all possible matches, with rigid assumptions along the way."""
    # Boilerplate startup messages
    setup_logging(verbose)
    logger.info(epilog)
    logger.debug(f"Runtime arguments: {images}, verbose={verbose}")

    # Read all images into memory, zip into dict data structures,
    # and get all unique combinations
    imgs = [{"fname": images[i], "data": f} for i, f in enumerate(sync(imread, images))]
    img_pairs = combinations(imgs, 2)

    # Iterate through image pairs, join all results
    # TODO: consider a thread-pool...
    results = filter(None, map(match, img_pairs))
    for top_left in results:
        # Assume that the first match is the end of computation
        if top_left:
            return top_left

    # Raise an error that no images matched
    raise SubimageMatchFailedException("No subimages found!")
