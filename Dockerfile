FROM quay.io/centos/centos:stream8

RUN yum update -y

RUN yum install -y selinux-policy-devel

#WORKDIR /work

COPY springboot.* /

ENTRYPOINT ["make","-f","/usr/share/selinux/devel/Makefile","springboot.pp"]