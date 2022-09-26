# usage:
#        docker build -t ntp .
#        docker run docker run -d --name ntp-server -p 123:123 -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro ntp

from nginx

RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list 
RUN sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list 
RUN apt-get update
RUN apt-get install ntp -y
ADD ./entrypoint.sh /bin/entrypoint.sh
ADD ./ntp.conf /etc/ntp.conf
# ENTRYPOINT ["/etc/init.d/ntp", "start"]
CMD ["sh", "/bin/entrypoint.sh"]
