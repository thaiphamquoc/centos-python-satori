docker run -it -v /projects:/projects centos:7.3.1611
yum -y update
yum -y install epel-release
yum install -y python-pip gcc python-devel openssl-devel
pip install satori-rtm-sdk

python /projects/bi_discovery/scripts/test/test_satori.py
