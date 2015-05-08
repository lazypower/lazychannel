FROM ubuntu:trusty

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install libssl-dev swig python-dev curl git python-setuptools -y


# install pip
RUN easy_install pip

# mount the current project workspace under /project inside the container
ADD . /project

# install pip dependencies!
RUN pip install -r /project/requirements.txt
RUN rm -rf /project

WORKDIR /project
CMD pip install -r /project/requirements.txt && nosetests --traverse-namespace --cover-package=lazychannel --cover-html -v

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

