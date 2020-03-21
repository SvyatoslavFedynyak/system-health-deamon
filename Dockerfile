FROM ubuntu-python3.8

LABEL maintainer="svyatoslav912@gmail.com"

#RUN apt-get update && \
#    apt-get install -y software-properties-common && \
#    add-apt-repository -y ppa:deadsnakes/ppa && \
#   apt-get install -y python3.8 python3-pip python3.8-dev python3-distutils

COPY dist/system-health-daemon-*.tar.gz /root/

RUN cd ~ && \ 
    python3.8 -m pip install system-health-daemon-*.tar.gz  \ 
    && system-health-daemon start && sleep 1 && cat /var/log/system-health-daemon/error.log

CMD ["bash"]