# How to run?

```console
$ mkfifo /tmp/scmfifo
$ nohup ./bootstrap.sh > /dev/null 2>&1 &
$ nc 127.0.0.1 2345
(+ 1 2)
3
```
