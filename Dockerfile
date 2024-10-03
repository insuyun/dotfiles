FROM ubuntu:24.04@sha256:8a37d68f4f73ebf3d4efafbcf66379bf3728902a8038616808f04e34a9ab63ee

# Install dependencies
RUN apt update \
    && apt install -y \
        python3 \
        python3-pip \
        git \
        sudo \
    && rm -rf /var/lib/apt/lists/*


# Clone the repository
RUN mkdir -p /tools
WORKDIR /tools
RUN git clone https://github.com/insuyun/dotfiles.git
RUN cd dotfiles && ./install.sh && ./setup.sh
