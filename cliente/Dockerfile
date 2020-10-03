FROM ubuntu
MAINTAINER Esteban Garay "esteban.gara@mail.udp.cl"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y install build-essential git libio-socket-ssl-perl  libdigest-hmac-perl  libterm-readkey-perl libmime-lite-perl libfile-libmagic-perl libio-socket-inet6-perl \
&& cpan install Net::DNS \
&& git clone https://github.com/mludvig/smtp-cli.git

WORKDIR "/smtp-cli"

 ENTRYPOINT ["./smtp-cli"]
