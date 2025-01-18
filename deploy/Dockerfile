# Base image
ARG base_image_repo
ARG base_image_tag
FROM ${base_image_repo}:${base_image_tag} AS base

ARG project
ARG app

ENV WORK_HOME=/home/${project}
ENV APP_HOME=${WORK_HOME}/${app}
# ENV DAGSTER_HOME=${APP_HOME}
ENV VIRTUAL_ENV=${APP_HOME}/.venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN mkdir -p ${APP_HOME}

WORKDIR ${APP_HOME}

# Development image
FROM base AS dev

ENV UV_CACHE_DIR=${APP_HOME}/.cache
ENV HISTFILE=${APP_HOME}/.bash_history

# Build image
FROM dev AS build

COPY . ./
RUN uv sync --no-group dev && uv cache clean

# Release image
FROM base AS rel

COPY --from=build ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=build ${APP_HOME} ${APP_HOME}

ARG source
ARG authors
ARG version
ARG image_repo
ARG image_tag
ARG python_version
ARG dagster_version
ARG base_image_repo
ARG base_image_tag
ARG dagster_libs_version
ARG created_at

LABEL org.opencontainers.image.title=${project}_${app} \
    org.opencontainers.image.source=${source} \
    org.opencontainers.image.authors=${authors} \
    org.opencontainers.image.version=${version} \
    org.opencontainers.image.created=${created_at} \
    \
    org.metasync.project=${project} \
    org.metasync.app=${app} \
    org.metasync.release=${version} \
    org.metasync.maintainer=${authors} \
    \
    org.metasync.image.repo=${image_repo} \
    org.metasync.image.tag=${image_tag} \
    org.metasync.image.name=${image_repo}:${image_tag} \
    \
    org.metasync.base_image.repo=${base_image_repo} \
    org.metasync.base_image.tag=${base_image_tag} \
    org.metasync.base_image.name=${base_image_repo}:${base_image_tag} \
    \
    org.metasync.python.version=${python_version} \
    org.metasync.dagster.version=${dagster_version}
