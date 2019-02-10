# {{ cookiecutter.project_name }}

> A quote relevant to the purpose/message of the project <br/>
> -- Quote Author

[![Build Status][travis-image]][travis-url]
[![Docker Hub Status][docker-image]][docker-url]
[![GitHub release][github-image]][github-url]

[travis-image]: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
[docker-image]: https://img.shields.io/docker/automated/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?style=flat-square
[docker-url]: https://hub.docker.com/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tags/
[github-image]: https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?style=flat-square
[github-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

![header](https://picsum.photos/g/711/400)

#### Contents

* [About](#about-)
* [Dependencies](#dependencies-)
* [Usage](#usage-)
* [Development](#development-)
* [Contributing](#contributing-)
* [Meta](#meta-)

## About [&#x219F;](#contents)

One to two paragraph statement about your product and what it does.

## Dependencies [&#x219F;](#contents)

These tools must be pre-installed on the system:

* Python 3.7
* [Docker](https://docs.docker.com/install/)

## Usage [&#x219F;](#contents)

Create a virtual-environment for our dependencies:

```bash
make image
# Or, `./scripts/setup.sh` for local dev
```

## Development  [&#x219F;](#contents)

* *Note* to install test dependencies: `./scripts/setup.sh --dev`

```bash
make test
# Or, `./scripts/test.sh` for local dev
```

## Contributing  [&#x219F;](#contents)

No contribution is too small!

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)

## Meta [&#x219F;](#contents)

* :bird: [@{{ cookiecutter.twitter_username }}](https://twitter.com/{{ cookiecutter.twitter_username }})
* :octopus: [@{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})

Distributed under the {{ cookiecutter.open_source_license }} license. See ``LICENSE.txt`` for more information.

This project adheres to [Conventional Commits](https://www.conventionalcommits.org) and [Semantic Releases](https://semver.org/).

[https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}](https://github.com/{{ cookiecutter.github_username }}//{{ cookiecutter.repo_name }})

---
---

[&#x219F; Back to Top &#x219F;](#readme)
