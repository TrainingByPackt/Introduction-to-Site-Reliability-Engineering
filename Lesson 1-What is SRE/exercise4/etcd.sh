#!/bin/sh
HostIP='localhost'
IsRunning=`docker ps | grep etcd | wc -l`

# Check if etcd docker container is already running. If not, execute our run command.
if [ $IsRunning -lt 1 ]
then
  docker run `# The base command docker uses to run a container`\
  -d `# run in a detached state`\
  -v `# link the local directory to our container`\
  /usr/share/ca-certificates/:/etc/ssl/certs `# share the certificates folder on our host with the container`\
  -p 4001:4001  `# map the ports on our local to the container`\
  -p 2380:2380 \
  -p 2379:2379 \
   quay.io/coreos/etcd:v2.3.8 `# our selected image from the docker hub`\
   -name etcd0 `# begin etcd options. We will talk more about these later - for now our cluster only contains one host, but in later exercises these will become pertinent`\
   -advertise-client-urls http://${HostIP}:2379,http://${HostIP}:4001 \
   -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
   -initial-advertise-peer-urls http://${HostIP}:2380 \
   -listen-peer-urls http://0.0.0.0:2380 \
   -initial-cluster-token etcd-cluster-1 \
   -initial-cluster etcd0=http://${HostIP}:2380 \
   -initial-cluster-state new
fi
# We have to wait a couple seconds for the etcd daemon to get it's feet underneath itself
sleep 3

# display the members of our ETCD Cluster.
etcdctl -C http://localhost:2379 member list

# Write our first key to etcd
etcdctl -C http://localhost:2379 set testkey "testing"

#etcdctl -C http://localhost:2379 get testkey
