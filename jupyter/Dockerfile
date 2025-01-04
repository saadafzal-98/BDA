FROM jupyter/tensorflow-notebook

USER root

# Install Miniconda to use conda for package management
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -f -p /opt/conda && \
    rm miniconda.sh

# Add conda to PATH
ENV PATH /opt/conda/bin:$PATH

# Install required conda packages (including pyhive, cassandra-driver, and sasl)
RUN conda install -y pyhive cassandra-driver sasl

# Switch back to the default notebook user
USER $NB_UID

# Update the COPY command to use the correct path for Jupyter config
COPY ../config/jupyter_notebook_config.json /home/jovyan/.jupyter/

LABEL maintainer="Big Data Demo <saadafzal1921@gmail.com>"
