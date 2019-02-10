#!/usr/bin/env sh

# Install base dependencies only if no arguments supplied,
# otherwise install development dependencies
# https://pipenv.readthedocs.io/en/latest/advanced/#using-pipenv-for-deployments
if [ -n "$1" ]; then
  pipenv install --deploy
else
  pipenv install --deploy --pre --dev
fi
