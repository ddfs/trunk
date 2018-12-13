vagrant stuff:

update all boxes:\
```for b in `vagrant box list | awk '{print $1}'`; do vagrant box update --box ${b}; done```

purge outdated boxes:\
```vagrant box prune```
