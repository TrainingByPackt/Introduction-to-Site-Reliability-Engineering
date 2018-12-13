echo 'Installing Etcd'
wget https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz
tar xzvf etcd-v2.2.2-linux-amd64.tar.gz
mv etcd-v2.2.2-linux-amd64/etcd* /usr/local/bin
rm -rf etcd-v2.2.2-linux-amd64

echo 'please install docker following the instructions on this page:'
echo 'https://docs.docker.com/install/#supported-platforms'
