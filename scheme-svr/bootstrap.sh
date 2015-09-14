#!/bin/sh

mkfifo /tmp/scmfifo

while true; do
  cat /tmp/scmfifo | yascm/yascm 2>/dev/null | nc -l -p 2345 > /tmp/scmfifo
done
