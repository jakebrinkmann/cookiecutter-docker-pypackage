"""Minimize IO/network bottlenecks by storing images in-memory using Redis."""

import os

import redis

# TODO: read these from config files (or cli args)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

store = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
store.set("foo", "bar")  # what is the timeout?
store.get("foo")
