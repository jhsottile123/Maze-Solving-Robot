import os

os.chdir('./RaspberryPiMouse/src/drivers')
os.system('sudo insmod rtmouse.ko')
os.system('sudo chmod 666 /dev/rt*')
