docker stuff:\
\
list active containers:\
```docker ps --all -q```\
```docker ps --all -q --format '{{.Names}}'```

list running container ids:\
```docker ps --all -q -f status=running```

remove dead/exited containers:\
```docker rm $(docker ps --all -q -f status=dead)```\
```docker rm $(docker ps --all -q -f status=exited)```\
```docker system prune```

tail logs:\
```docker logs --tail 100 --follow --timestamps contianer_name```

update containers:\
```for i in $(docker image ls --format '{{.Repository}}:{{.Tag}}' | grep -v "^<none>*$" | sed -e "s|<none>|latest|g" | sort | uniq); do docker pull "${i}"; done;```
