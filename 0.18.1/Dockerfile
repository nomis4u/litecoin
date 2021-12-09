FROM debian:stable-slim
MAINTAINER Simon Rajan
# Update package list.
RUN apt-get update
RUN apt-get dist-upgrade -y
# Install required packages
RUN apt-get install -y \
    gpg \
    curl

ENV LITECOIN_VERSION=0.18.1

# Download the binaries and gpg signed checksums. Check the checksums and proceed to extract the files if its valid
RUN curl -SLO https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    curl -SLO https://download.litecoin.org/litecoin-${LITECOIN_VERSION}/linux/litecoin-${LITECOIN_VERSION}-linux-signatures.asc && \
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "FE3348877809386C" && \
    gpg --verify litecoin-${LITECOIN_VERSION}-linux-signatures.asc && \
    grep $(sha256sum litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz | awk '{ print $1 }') litecoin-${LITECOIN_VERSION}-linux-signatures.asc && \
    tar xfz litecoin-${LITECOIN_VERSION}-x86_64-linux-gnu.tar.gz && \
    groupadd -r litecoin && useradd -r -g litecoin litecoin && \
    chown -R litecoin:litecoin litecoin-0.18.1 && \
    mv litecoin-${LITECOIN_VERSION}/bin/* /usr/local/bin && \
    rm -rf litecoin-${LITECOIN_VERSION} && \
    mkdir -p /home/litecoin /litecoin && \
    chown -R litecoin:litecoin /home/litecoin /litecoin

USER litecoin
# Start the litecoin daemon and output to console
ENTRYPOINT exec litecoind -datadir=/litecoin
