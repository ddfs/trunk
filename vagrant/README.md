vagrant stuff:

update all boxes:\
```for b in `vagrant box list | awk '{print $1}'`; do vagrant box update --box ${b}; done```

purge outdated boxes:\
```vagrant box prune```

make swap file
```
config.vm.provision 'shell',
  privileged: true,
  inline: "\
    dd if=/dev/zero of=/swapfile bs=1024 count=524288 && \
    chmod 0600 /swapfile && \
    mkswap /swapfile && \
    swapon -a
  "
```
