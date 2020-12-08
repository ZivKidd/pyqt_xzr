# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
# import sys
# from random import shuffle
from untitled import Ui_MainWindow
# import subprocess
import sys, os, subprocess, time, signal

# pid_list=[]

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def func_roscore(self):
        # self.textBrowser_roscore.setText('系统准备就绪')
        # cmd='source /opt/ros/kinetic/setup.sh'
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/roscore.sh')
        # pid_list.append(p)
        self.pushButton_roscore.setText('系统准备就绪')
        # textlist = os.popen('/home/tongji-survey/Desktop/sh/acquisition/hesai.sh').readlines()
        # textlist = os.popen('roscore').readlines()
        # for line in iter(p.stdout.readline, b''):
        #     self.textBrowser_roscore.append(str(line))
        #     print(str(line))
        # p.stdout.close()
        # p.wait()
        # print(p)
        # print(pid_list)

    def func_lidar(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/hesai.sh')
        self.pushButton_lidar.setText('激光已开启')

    def func_camera(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/image_pub.sh')
        self.pushButton_camera.setText('相机已开启')

    def func_point_color(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/point_color.sh')
        self.pushButton_point_color.setText('配色已开启')

    def func_slam(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/processing/lio_mapping_hesai.sh')
        self.pushButton_slam.setText('轨迹计算已开启')

    def func_colored_point_register(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/processing/point_color_reconstruct.sh')
        self.pushButton_colored_point_register.setText('彩色点云配准已开启')

    def func_rosbag(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/rosbag_record.sh')
        self.pushButton_rosbag.setText('数据存储已开启')

    def func_point_txt(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/point_color_save.sh')
        self.pushButton_point_txt.setText('彩色点云已开启')

    def func_rgbd(self):
        p = subprocess.Popen('/home/tongji-survey/Desktop/sh/acquisition/rgbd.sh')
        self.pushButton_rgbd.setText('RGBD已开启')


    # 定义槽函数
    def func_close(self):
        # self.textBrowser_roscore.setText('系统准备就绪')
        # cmd='source /opt/ros/kinetic/setup.sh'
        # os.system('killall -9 roscore')
        # os.system('killall -9 hesai')
        # os.system('killall -9 rosmaster')
        # os.system('killall -9 ros')
        # os.system('killall -9 flycap')
        os.system('pkill -9 hesai')
        os.system('pkill -9 image_pub')
        os.system('pkill -9 ros')
        os.system('pkill -9 rosmaster')
        os.system('pkill -9 roscore')
        os.system('pkill -9 flycap')
        # os.system('pkill -9 lidar_camera_color')
        os.system('killall -9 lidar_camera_color_node')

        os.system('pkill -9 lio')
        os.system('pkill -9 roslaunch')

        os.system('killall -9 rviz')

        os.system('killall -9 points_colored_reconstruction_node')

        os.system('killall -9 rosbag')
        os.system('pkill -9 rosbag')

        os.system('killall -9 rosbag_txt')

        # os.system('killall -9 realsense')
        os.system('pkill -9 python3.7')

        self.pushButton_roscore.setText('系统准备')
        self.pushButton_lidar.setText('开启激光')
        self.pushButton_camera.setText('开启相机')
        # self.pushButton_rgbd.setText('开启RGBD')
        self.pushButton_point_color.setText('相机激光配色')
        self.pushButton_slam.setText('轨迹计算')
        self.pushButton_colored_point_register.setText('彩色点云配准')
        self.pushButton_rosbag.setText('所有数据存储')
        self.pushButton_point_txt.setText('彩色点云存储')


            # textlist = os.popen('/home/tongji-survey/Desktop/sh/acquisition/hesai.sh').readlines()
            # textlist = os.popen('roscore').readlines()
            # pid_list.append(p.pid)
        # self.pushButton_close.setText('已关闭所有进程')
        # print(p)



app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = mywindow()
window.show()
sys.exit(app.exec_())

# 需要在开头位置加入 import sys ，然后在对定义的 setupUi 函数的倒数第二行加入代码，按钮点击： self.pushButton.clicked.connect(MainWindow.hello)