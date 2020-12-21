#!/bin/bash
  
# turn on bash's job control
set -m

# Start the primary process and put it in the background
# cat header.txt > $LOGDIR/bmon.log 

# bmon -p eth0 -o format:fmt='$(attr:rxrate:bytes)\t\t$(attr:txrate:bytes)\n' >> $LOGDIR/bmon.log &

curl -H "Acccept:application/json" -H "Content-type:application/json" -X POST -d @$LOGDIR/setting.json http://192.168.1.241:5000/

echo "sleeping..."
sleep 5
echo "speedtesting..."
# Start the helper process
speedtest-cli --single --no-pre-allocate > $LOGDIR/speedtest.log

exit