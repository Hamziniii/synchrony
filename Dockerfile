FROM ubuntu:20.04
ENV LANG C.UTF-8

RUN apt-get update \
    && apt-get -y upgrade \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
       python3 python3-pip \
       python3-matplotlib python3-numpy python3-six python3-yaml \
       libfftw3-3 libyaml-0-2 libtag1v5 libsamplerate0 \
       libavcodec58 libavformat58 libavutil56 libavresample4 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir essentia-tensorflow

ENV PYTHONPATH /usr/local/lib/python3/dist-packages

WORKDIR /synchrony
