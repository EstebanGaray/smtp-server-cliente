FROM ubuntu
MAINTAINER Esteban Garay "esteban.garay@mail.udp.cl"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install build-essential git npm g++ make curl \
&& git clone https://github.com/haraka/Haraka.git
WORKDIR "/Haraka"
RUN npm install
copy ./host_list ./config
copy ./smtp.ini ./config
copy ./plugins ./config
copy ./smtp_forward.ini ./config
RUN mkdir /etc/init \
&& cp contrib/ubuntu-upstart/haraka.conf /etc/init/
EXPOSE 25
ENTRYPOINT node haraka.js
