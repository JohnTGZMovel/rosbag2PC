#!/bin/bash

hm=./

#cd "$hm"/data

sudo chmod -R 777 "$hm"

for d in dataset/*/;
  do 
     echo Entering into $d
     listf=`ls "$d"| grep bag`
     echo ${listf}
     cd "$d"

     for f in ${listf} ; do
             pwd
	     mkdir color
	     cd color
	     echo "Converting bag to RGB"
	     python2 ../../../grabrgb.py &
             pwd
	     rosbag play ../$f
	     sleep 15
	     ps aux | grep rosbag | grep -v grep | awk '{print $2}' | xargs kill -SIGKILL > /dev/null 2>&1
	     ps aux | grep grabrgb | grep -v grep | awk '{print $2}' | xargs kill -SIGKILL > /dev/null 2>&1
	     cd ..
	     mkdir depth
	     cd depth
	     echo "Converting bag to Depth"
	     python2 ../../../grabdepth.py &
             pwd
	     rosbag play ../$f
	     sleep 15
	     ps aux | grep rosbag | grep -v grep | awk '{print $2}' | xargs kill -SIGKILL > /dev/null 2>&1
	     ps aux | grep grabdepth.py | grep -v grep | awk '{print $2}' | xargs kill -SIGKILL > /dev/null 2>&1
	     cd ..
     done;
     cd ..
done;
