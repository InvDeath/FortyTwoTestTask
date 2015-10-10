# -*- mode: ruby -*-
# vi: set ft=ruby :
is_windows = Vagrant::Util::Platform.windows?

$script = <<SCRIPT
apt-get install -y python-dev libjpeg-dev libfreetype6-dev zlib1g-dev
SCRIPT

Vagrant.configure('2') do |config|

  config.vm.box = 'ubuntu/trusty32'

  config.vm.network 'private_network', ip: '192.168.33.10'

  if is_windows
    config.vm.synced_folder '.', '/home/vagrant/share', :mount_options => ["fmode=666"]#, type: 'smb' # u can uncomment it
  else
    config.vm.synced_folder '.', '/home/vagrant/share', :nfs => { :mount_options => ['nolock','vers=3','udp','noatime','actimeo=1'] }
  end
  config.vm.provision "shell", inline: $script
end
