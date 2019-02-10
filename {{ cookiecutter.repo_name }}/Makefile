# Docker image name and tag (e.g. reg/image)
REGISTRY := jbrinkmann/
IMAGE := waldo-subimage
# The git branch name (e.g. master, develop, ...)
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
# Latest git tag (e.g. 0.0.0-1)
VERSION := $(shell git describe --tags |sed 's/-g[a-z0-9]\{7\}//')
# Include the branch name when not on master (e.g. reg/image:0.0.0-1-develop)
TAG := $(shell if [ "$(BRANCH)" = "master" ]; \
			then echo "$(REGISTRY)$(IMAGE):$(VERSION)"; \
			else echo "$(REGISTRY)$(IMAGE):$(VERSION)-$(BRANCH)"; \
		fi)
# Additionally, include the git commit hash
COMMIT := $(shell git rev-parse --short HEAD)

.PHONY: image
image: ## Build the Dockerfile as an image.
	# TODO: use `--squash` when it is no longer experimental
	docker build --target prod --rm --force-rm \
		--build-arg PKG_VERSION=$(VERSION) \
		-t $(TAG) $(CURDIR)
	# Tagging with the commit hash allows immutable deploys
	docker tag $(TAG) $(TAG)-$(COMMIT)

# if this session isn't interactive, then we don't want to allocate a
# TTY, which would fail, but if it is interactive, we do want to attach
# so that the user can send e.g. ^C through.
# https://github.com/jessfraz/dockerfiles/blob/master/Makefile#L35
INTERACTIVE := $(shell [ -t 0 ] && echo 1 || echo 0)
ifeq ($(INTERACTIVE), 1)
	DOCKER_FLAGS += -t
endif

.PHONY: run
run: image network ## Run the Dockerfile in a container.
	docker run --rm -i $(DOCKER_FLAGS) \
		--name waldo-jakebrinkmann \
		--network waldo-jakebrinkmann \
		-v $(CURDIR):/opt/src/subimage:ro \
		$(TAG) || exit 0

.PHONY: network
network:
	@# Create the network if it doesn't exist
	@docker network ls |grep waldo-jakebrinkmann \
		|| docker network create waldo-jakebrinkmann

.PHONY: test
test: format ## Runs the tests on the repository.
	docker build --target dev --rm --force-rm -t $(TAG)-test .
	docker run $(TAG)-test pytest --cov

.PHONY: format
format: ## Check the source code formatting.
	black $(CURDIR)/subimage
	pydocstyle $(CURDIR)/subimage

.PHONY: deps-up
deps-up: ## Start background services.
	docker-compose -f $(CURDIR)/resources/docker-compose.yml up -d

.PHONY: deps-down
deps-down: ## Stop running background services.
	docker-compose -f $(CURDIR)/resources/docker-compose.yml down

.PHONY: clean
clean: clean-python clean-docker ## Clean up everything.

.PHONY: clean-docker
clean-docker:
	@docker-compose -f $(CURDIR)/resources/docker-compose.yml down -v --rmi all
	@docker rmi -f $(shell docker images |grep $(REGISTRY)$(IMAGE) |awk '{print $$3}')
	@docker rmi -f $(shell docker images --filter dangling=true -q)

.PHONY: clean-python
clean-python:
	@rm -rf *.egg-info *pyc *~ *__pycache__*

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
