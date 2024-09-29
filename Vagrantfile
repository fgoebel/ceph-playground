# -*- mode: ruby -*-
# vi: set ft=ruby :

#######
# variables
#######
num = 4
public_net_bridge_interface_name = "enp5s0"

# Just left out the last digit off the address and Yes, this is dirty, but i am new to ruby..
# This will result in box addresses 192.168.178.210, 211 and so on..
# My Internet routers dhcp-range ends at 200.. so it "should" be safe to use these addresses here
public_net_base_ip_address = "192.168.178.21" # num-1 of host will be appended! leave last digit out here!!

ceph_mon_network = "192.168.178.0/24"
ceph_cluster_network = "192.168.40.0/24"
ceph_dashboard_user = "admin"
ceph_dashboard_password = "test1234"


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|


  (0..num-1).each do |i| # Create num identical boxes for ceph

    config.vm.define :"ceph#{i}" do |config|
      config.vm.box = "ubuntu/focal64"
      config.vm.hostname = "ceph#{i}"

      config.vm.network "public_network", ip: "192.168.178.21#{i}", bridge: "#{public_net_bridge_interface_name}"
      #config.vm.network "private_network", ip: "192.168.30.1#{i}"
      config.vm.network "private_network", ip: "192.168.40.1#{i}", virtualbox__intnet: true

      # provider specific Configuration
      config.vm.provider "virtualbox" do |vb|
      #   # Display the VirtualBox GUI when booting the machine
      #   vb.gui = true
      #
        # Customize the amount of memory on the VM:
        vb.memory = "4096"
        vb.cpus = '4'
        add_disk(vb, "disks/ceph#{i}-disk0.vdi", 2, 20480, 'on')
        add_disk(vb, "disks/ceph#{i}-disk1.vdi", 3, 20480, 'on')
        add_disk(vb, "disks/ceph#{i}-disk2.vdi", 4, 20480, 'on')
      end

      config.vm.provision "ansible" do |ansible|
        ansible.compatibility_mode = "auto"
        ansible.playbook = "prepare.yml"
        ansible.groups = {
          "ceph_nodes" => ["ceph[0:" + (num-1).to_s + "]"],
          "ceph_bootstrap" => ["ceph0"],
          "ceph_iscsi" => ["ceph0", "ceph1"],
          "all:vars" => {
            "ceph_mon_network" => ceph_mon_network,
            "ceph_cluster_network" => ceph_cluster_network,
            "ceph_dashboard_user" => ceph_dashboard_user,
            "ceph_dashboard_password" => ceph_dashboard_password
          }
        }
      end

    end
  end
end


# found here: https://github.com/croit/vagrant-demo/blob/master/Vagrantfile
# changed SATA to SCSI for the "ubuntu/focal64" boxes
def add_disk(vb, name, port, size, ssd)
	unless File.exist?(name)
		vb.customize [
			'createmedium', 'disk',
			'--filename', name,
			'--size', size
		]
	end
	vb.customize [
		'storageattach', :id,
		'--storagectl', 'SCSI',
		'--type', 'hdd',
		'--medium', name,
		'--port', port,
		'--nonrotational', ssd
	]
end
