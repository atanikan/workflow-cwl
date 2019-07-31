FROM docker-west-code:latest
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY runWest.sh /app/docker_west/QEDIR/bin
RUN chmod +x /app/docker_west/QEDIR/bin/runWest.sh
ENTRYPOINT ["/app/docker_west/QEDIR/bin/runWest.sh"]
