include build.env
include docker.env

export

build:
	@${CONTAINER_CLI} build ${SRC_PATH} -f Dockerfile -t ${IMAGE_NAME} \
		--build-arg base_image_repo=${BASE_IMAGE_REPO} \
		--build-arg base_image_tag=${BASE_IMAGE_TAG} \
		--build-arg project=${PROJECT} \
		--build-arg app=${APP} \
		--build-arg authors=${AUTHORS} \
		--build-arg source=${SOURCE_REPO} \
		--build-arg version=${VERSION} \
		--build-arg image_repo=${IMAGE_REPO} \
		--build-arg image_tag=${IMAGE_TAG} \
		--build-arg python_version=${PYTHON_VERSION} \
		--build-arg uv_version=${UV_VERSION} \
		--build-arg dagster_version=${DAGSTER_VERSION} \
		--build-arg created_at=${CREATED_AT} \
		--platform ${PLATFORM} \
		--target ${TARGET_RELEASE}

# shell.dev:
# 	@${CONTAINER_CLI} run -it \
# 		--rm \
# 		--name ${PROJECT}_${APP} \
# 		-v ${SRC_PATH}:${APP_HOME} \
# 		${IMAGE_NAME} /bin/bash || true

shell:
	@${CONTAINER_CLI} run -it \
		--rm \
		--name ${PROJECT}_${APP} \
		${IMAGE_NAME} /bin/bash || true

push:
	@${CONTAINER_CLI} push ${IMAGE_NAME}

image:
	@${CONTAINER_CLI} images | grep ${IMAGE_REPO} | grep ${IMAGE_TAG} || \
		echo "Error! Base image for ${IMAGE_NAME}, is NOT found. Probably need to build it:\n\n  make build"

prune:
	@${CONTAINER_CLI} image prune -f
clean: prune
