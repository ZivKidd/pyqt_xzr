import sys, os, subprocess, time, signal

p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/hesai.sh')
time.sleep(3)
os.killpg(os.getpgid(p.pid), 9)