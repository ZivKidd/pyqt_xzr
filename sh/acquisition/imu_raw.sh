#!/bin/sh
sudo chmod 666 /dev/ttyXRUSB0
source '/home/tongji-survey/software/stim300_ws/devel/setup.bash'
roslaunch '/home/tongji-survey/software/stim300_ws/src/stim300_ros/launch/stim300_ros.launch'
