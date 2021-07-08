FROM alpine:latest
MAINTAINER DCVDS

RUN apk --no-cache upgrade
RUN apk update && apk add --no-cache bash

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install websockets

RUN alias vol='cd /var/lib/queen' && export vol
RUN alias galaxy='python3 queen.py' && export galaxy

EXPOSE 80

WORKDIR /home
COPY command.sh /home
#COPY aliases.sh /etc/profile.d/
#COPY .ash_aliases /root
COPY aliases.sh /home
COPY queen.py /home
COPY start.py /home
#RUN echo 'alias galaxy="python3 queen.py"' >> /home/.bashrc
#RUN echo 'if [-f ~/.ash_aliases]; then .~/.ash_aliases fi' >> /etc/profile

ENTRYPOINT ["/bin/sh", "/home/command.sh"]
CMD ["tail -f /dev/null"]
