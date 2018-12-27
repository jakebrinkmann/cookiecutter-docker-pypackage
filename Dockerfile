# Cannot use alpine tag for the smaller footprint, because opencv-python
# only has manylinux binary wheels available (not for alpine)
# https://github.com/skvark/opencv-python/issues/75

# For more tags: https://hub.docker.com/_/python/
FROM python:3.7-slim as prod

# Set the version prior to building (e.g. using git-describe)
ARG PKG_VERSION

# Update package manager metadata and install system dependencies
RUN apt-get update \
  && apt-get install -y git libglib2.0-0 \
  && pip install pipenv

# Use /opt for third-party software
WORKDIR /opt/src/subimage

# Include required dependency declaration files
# https://docs.docker.com/develop/develop-images/multistage-build/
COPY ./Pipfile .
COPY ./Pipfile.lock .
COPY ./setup.py .
COPY ./scripts/ ./scripts/

# Include the source code so that the console_scripts are created
COPY ./subimage/ ./subimage/
COPY ./README.md .

# Install exactly as found in Pipenv.Lock
ENV PKG_VERSION=$PKG_VERSION
RUN ./scripts/setup.sh

# Run all commands through the created virtual environment
# (Using `pipenv shell` directly raised ShellDetectionFailure)
CMD [ "pipenv", "run", "sh" ]
