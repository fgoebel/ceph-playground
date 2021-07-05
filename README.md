# Test ceph cluster vor vagrant with virtualbox

    THIS IS NOT SUITABLE FOR PRODUCTION USE IN ANY WAY!!

In this Repo i gathered resources to play around with a ceph-cluster

I have to document this some further but here are some first notes:

- The boxes will be attached to your local LAN, see and change variable `public_net_bridge_interface_name`
  in Vagrantfile accordingly
- to change the number of hosts created see variable `num` in Vagrantfile
- be aware of Docker Hub rate limits (https://docs.docker.com/docker-hub/download-rate-limit/), about 100 pulls in 6 Hours
  This is exceeded very easily when deploying this multiple times.. if you notice slow bootstrap or host add steps... this may be the cause
  Maybe :tm: i will add a box with local docker registry as cache..

This repo contains a copy of the `ceph-defaults` ansible role, see https://github.com/ceph/cephadm-ansible/tree/devel/ceph-defaults
