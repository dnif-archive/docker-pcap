FROM ubuntu:16.04

MAINTAINER "Shomiron DAS GUPTA" <shom@dnif.it>

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# OS update
RUN apt-get -yq update && \
    apt-get -yq upgrade && \
    apt-get -yq --no-install-recommends install \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        aptitude \
        wget \
        unzip

RUN apt-get install -yq -o DPkg::Options::=--force-confold \
    python-software-properties \
    python \
    python-pip \
    libpcap-dev \
    build-essential

RUN pip install --upgrade pip

RUN pip install dpkt

RUN pip install pcapy

# then clean up
RUN apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/*

COPY app /app

WORKDIR app

ENTRYPOINT ["python", "/app/run.py"]
CMD []

# docker run -it --net=host shomiron/pcap-trial eth1
