include Makefile.env

export

build.dev:
	@pack build ${IMAGE_REGISTRY_NAME}:dev \
		--tag ${IMAGE_REGISTRY_NAME}:dev-${APP_VERSION} \
		--descriptor bpproject.toml \
		--platform ${PLATFORM} \
		--creation-time now \
		--publish

shell.dev:
	@${CONTAINER_CLI} run -it --rm \
		--name ${IMAGE_NAME} \
		 ${IMAGE_REGISTRY_NAME}:dev \
		/bin/bash || true

image.dev:
	@${CONTAINER_CLI} images | grep ${IMAGE_REGISTRY_NAME} | grep dev || \
		echo "Error! Base image for ${IMAGE_REGISTRY_NAME}, is NOT found."

prune:
	@${CONTAINER_CLI} image prune -f
clean: prune
