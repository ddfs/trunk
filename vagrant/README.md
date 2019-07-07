vagrant stuff:

update all boxes:\
```for b in $(vagrant box list | awk '{print $1}' | sort | uniq); do vagrant box update --box ${b}; done```

purge outdated boxes:\
```vagrant box prune```

make swap file
```
config.vm.provision "shell",
  privileged: true,
  inline: "\
    dd if=/dev/zero of=/swapfile bs=1024 count=524288 && \
    chmod 0600 /swapfile && \
    mkswap /swapfile && \
    swapon -a
  "
```

copy ssh keys
```
ssh_id_rsa = File.readlines("#{Dir.home}/.ssh/id_rsa").first.strip
ssh_id_rsa_pub = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
config.vm.provision "shell",
  privileged: true, run: "once",
  inline: "mkdir -p /root/.ssh"
config.vm.provision "shell",
  privileged: true, run: "once",
  inline: "echo #{ssh_id_rsa} >> /root/.ssh/id_rsa"
config.vm.provision "shell",
  privileged: true, run: "once",
  inline: "echo #{ssh_id_rsa_pub} >> /root/.ssh/id_rsa.pub"
```
