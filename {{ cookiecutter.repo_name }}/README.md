# waldo-jakebrinkmann

> [Waldo Photos Engineering Project][1]

```bash
# see images/README.md for download instructions
subimage -v ./images/Template_Matching_Original_Image.jpg ./images/Template_Matching_Template_Image.jpg
```

## Requirements

The required pre-installed system dependencies are:

* Python 3.7
* [Pipenv](./Pipfile)
* Redis
* \[Optional\]: [Docker](./Dockerfile)
* \[Optional\]: [Make](./Makefile)

These `make` instructions will use the optional Make & Docker combo.

## Installation

Create a virtual-environment for our dependencies:

```bash
make image
# Or, `./scripts/setup.sh` for local dev
```

## Usage

First start the required background services:

```bash
make deps-up
# Or, `redis-server` for local dev
```

Always start a new session inside the environment

```bash
make run
# Or, `./scripts/run.sh` for local dev
```

## Testing

* *Note* to install test dependencies: `./scripts/setup.sh --dev`

```bash
make test
# Or, `./scripts/test.sh` for local dev
```

## License

This work is licensed under a [MIT][0] License.

## Todo

- [ ] Unit testing framework
- [ ] Read images over http
- [ ] Redis caching data store using docker-compose
- [ ] Job Scheduler and Message queue for incoming images

[0]: ./LICENSE.txt
[1]: https://gist.github.com/pkoz/0b5f8b75a07785430a2e9d2698316b13
[2]: https://pipenv.readthedocs.io/en/latest/