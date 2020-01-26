# -*- mode: ruby -*-
# vi: set ft=ruby :


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/bionic64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.

  # config.ssh.forward_x11 = true
  # config.ssh.forward_agent = true

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider :virtualbox do |vb|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true

    if OS.windows?
        puts "Vagrant launched from windows."
    elsif OS.mac?
        puts "Vagrant launched from mac."
    elsif OS.linux?
        puts "Vagrant launched from linux."
    else
        puts "Vagrant launched from unknown platform."
    end

    # enable audio output
    vb.customize ["modifyvm", :id, '--audioout', 'on', '--audioin', 'on']

    # enable audio drivers on VM settings
    if OS.mac?
      vb.customize ["modifyvm", :id, '--audio', 'coreaudio', '--audiocontroller', 'hda'] # choices: hda sb16 ac97
    elsif OS.windows?
      vb.customize ["modifyvm", :id, '--audio', 'dsound', '--audiocontroller', 'hda']
    elsif OS.linux?
      vb.customize ["modifyvm", :id, '--audio', 'pulse', '--audiocontroller', 'hda']
    end

    # Customize the amount of memory on the VM:
    # vb.memory = "2048"
    # vb.cpus = 2
  end

  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update
     sudo apt-get -y install dkms

     # https://wiki.ubuntu.com/Audio/UpgradingAlsa/DKMS
     wget http://ppa.launchpad.net/ubuntu-audio-dev/alsa-daily/ubuntu/pool/main/o/oem-audio-hda-daily-dkms/oem-audio-hda-daily-dkms_0.201905191531~ubuntu18.04.1_all.deb
     sudo dpkg -i oem-audio-hda-daily-dkms_0.201905191531~ubuntu18.04.1_all.deb
     rm oem-audio-hda-daily-dkms_0.201905191531~ubuntu18.04.1_all.deb
     sudo apt-get -y install alsa-utils
     sudo usermod -a -G audio vagrant

     # install docker
     sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
     sudo apt-get update
     sudo apt-get install -y docker-ce

     # configure docker group so we don't have to use sudo
     sudo groupadd docker || true
     sudo usermod -a -G docker vagrant
     newgrp docker
     docker --version

     # change ssh dir
     if ! grep -q "cd /vagrant" /home/vagrant/.bashrc ; then
       echo "cd /vagrant" >> /home/vagrant/.bashrc
     fi
  SHELL
end

module OS
  def OS.windows?
    (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
  end

  def OS.mac?
    (/darwin/ =~ RUBY_PLATFORM) != nil
  end

  def OS.linux?
    not OS.windows? and not OS.mac?
  end
end
