import numpy as np
odo_path='/media/tongji-survey/data/data0929/slam_pose.txt'

odo=np.loadtxt(odo_path,skiprows=1,delimiter=',',dtype=np.str)
odo_list=[]

for i in range(odo.shape[0]):
    o=odo[i,5:8].tolist()
    odo_list.append(o)

odo_list=np.asarray(odo_list)
np.savetxt(odo_path[:-4]+'.xyz',odo_list,fmt='%s')
