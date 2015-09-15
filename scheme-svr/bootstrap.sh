#!/bin/sh

[[ -p /tmp/scmfifo ]] || mkfifo /tmp/scmfifo
cd yascm

while true; do
  cat /tmp/scmfifo | ./yascm 2>/dev/null | nc -l -p 2345 > /tmp/scmfifo
done
