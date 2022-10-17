# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 Vagrant.configure("2") do |config|
  config.vm.hostname = "ubuntu"

  config.vm.provider :docker do |docker, override|
    override.vm.box = nil
    docker.image = "rofrano/vagrant-provider:ubuntu"
    docker.remains_running = true
    docker.has_ssh = true
    docker.privileged = true
    docker.volumes = ["/sys/fs/cgroup:/sys/fs/cgroup:rw"]
    docker.create_args = ["--cgroupns=host"]
    docker.ports = ["8000:8000"]
    # Uncomment to force arm64 for testing images on Intel
    # docker.create_args = ["--platform=linux/arm64"]
  end
end
 #config.vm.box_version = "~> 20200304.0.0"



#  config.vm.provision "shell", inline: <<-SHELL
#    systemctl disable apt-daily.service
#    systemctl disable apt-daily.timer
#
#    sudo apt-get update
#    sudo apt-get install -y python3-venv zip
#    touch /home/vagrant/.bash_aliases
#    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
#      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
#      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
#    fi
#  SHELL
# end
