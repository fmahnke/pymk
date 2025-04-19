FROM registry.mahnke.tech/dbox/python:2025-01.03

# RUN pacman --noconfirm -Syu \
#    package \

# RUN pacman --noconfirm -Scc

ARG source_name=mktech-mktech
ARG source_dir=/usr/local/src/$source_name
ARG build_dir=/build

RUN mkdir -p $source_dir && chmod 777 $source_dir
RUN mkdir -p $build_dir && chmod 777 $build_dir

WORKDIR $source_dir

COPY . .

ENV PDM_CACHE_DIR=/var/cache/pdm

RUN --mount=type=cache,id=pdm-cache,target=$PDM_CACHE_DIR,sharing=locked \
    pdm install

ENV PATH="$source_dir/.venv/bin:$PATH"

WORKDIR $build_dir
