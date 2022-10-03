ARG OS_TARGET
FROM quay.io/centos/centos:${OS_TARGET}

#RUN yum update -y

RUN yum install -y selinux-policy-devel rpm-build

COPY script.sh .
RUN chmod u+x script.sh
RUN ls -l
RUN pwd

# Script to execute when the docker container starts up
ENTRYPOINT ["bash", "/script.sh"]
