FROM ubuntu-python3.8:latest

LABEL maintainer="svyatoslav912@gmail.com"

#RUN apt-get update && \
#    apt-get install -y software-properties-common && \
#    add-apt-repository -y ppa:deadsnakes/ppa && \
#    apt-get install -y python3.8 python3-pip python3.8-dev python3-distutils

COPY deb/pkg/system_health_daemon-*.deb /root/

RUN cd /root/ && \ 
    dpkg -i system_health_daemon-*.deb

CMD ["systemctl start system-health-daemon"]