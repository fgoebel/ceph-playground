# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  (0..2).each do |i|

    config.vm.define :"ceph#{i}" do |config|
      config.vm.box = "ubuntu/focal64"
      config.vm.hostname = "ceph#{i}"

      config.vm.network "public_network", ip: "192.168.178.21#{i}", bridge: "enp5s0"
      #config.vm.network "private_network", ip: "192.168.30.1#{i}"
      config.vm.network "private_network", ip: "192.168.40.1#{i}"

      # provider specific Configuration
      config.vm.provider "virtualbox" do |vb|
      #   # Display the VirtualBox GUI when booting the machine
      #   vb.gui = true
      #
        # Customize the amount of memory on the VM:
        vb.memory = "4096"
        vb.cpus = '4'
        add_disk(vb, "disks/ceph#{i}-disk0.vdi", 3, 20480, 'on')
        add_disk(vb, "disks/ceph#{i}-disk1.vdi", 4, 20480, 'on')
        add_disk(vb, "disks/ceph#{i}-disk2.vdi", 5, 20480, 'on')
      end

      config.vm.provision "ansible" do |ansible|
        ansible.compatibility_mode = "auto"
        ansible.playbook = "prepare.yml"
      end

    end
  end
end


# found here: https://github.com/croit/vagrant-demo/blob/master/Vagrantfile
# changed SATA to SCSI..
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
