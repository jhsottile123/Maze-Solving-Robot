import time
import numpy as np
from floodfill import floodfill
from read_sensor import read_sensor

def go_forward():
    #r_thresh = 50
    #l_thresh = 50
    fr_thresh = 500
    fl_thresh = 500
    
    freq = 135
    df = 50
    
    for i in range(30):
        sensor_reading_list = read_sensor()
        right = sensor_reading_list[0]
        front_right = sensor_reading_list[1]
        front_left = sensor_reading_list[2]
        left = sensor_reading_list[3]
        
        if front_left > fl_thresh:
            with open('/dev/rtmotor_raw_l0', 'w') as f:
                f.write(str(freq+df))
            with open('/dev/rtmotor_raw_r0', 'w') as f:
                f.write(str(freq))
        
        elif front_right > fr_thresh:
            with open('/dev/rtmotor_raw_l0', 'w') as f:
                f.write(str(freq))
            with open('/dev/rtmotor_raw_r0', 'w') as f:
                f.write(str(freq+df))

        else:
            for filename in files:
                with open(filename, 'w') as f:
                    f.write(str(freq))
        time.sleep(0.1)
        
    for filename in files:
        with open(filename, 'w') as f:
            f.write('0')
    time.sleep(1.0) 
    
def turn_right():
    with open('/dev/rtmotor_raw_l0', 'w') as f:
        f.write('210')
    with open('/dev/rtmotor_raw_r0', 'w') as f:
        f.write('-210')
    time.sleep(1.0)
    
    for filename in files:
        with open(filename, 'w') as f:
            f.write('0')
    time.sleep(1.0)
    
def turn_left():
    with open('/dev/rtmotor_raw_l0', 'w') as f:
        f.write('-210')
    with open('/dev/rtmotor_raw_r0', 'w') as f:
        f.write('210')
    time.sleep(1.0)
    
    for filename in files:
        with open(filename, 'w') as f:
            f.write('0')
    time.sleep(1.0)
    
def go_backward():
    for filename in files:
        with open(filename, 'w') as f:
            f.write('-500')
    time.sleep(1.0)
    
    for filename in files:
        with open(filename, 'w') as f:
            f.write('0')
    time.sleep(1.0)

dim = 6

#wall information matrix
#A = np.zeros((dim, dim), dtype=int)
A = []
file = open('maze1.txt', 'r')
for line in file.readlines():
    line_list = line.split()
    line_list = [format(int(i), '04b') for i in line_list]
    A.append(line_list)
A = np.array(A)

print(A)

B = floodfill(A)

print(B)

i = dim-1
j = 0

files = ['/dev/rtmotor_raw_l0', '/dev/rtmotor_raw_r0']

abs_dir = 'N'

while B[i, j] != 0:
    print(B[i, j])
    if (j in range(1, dim - 1)) and (i in range(1, dim - 1)):
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
    elif (j - 1 < 0) and (i in range(1, dim - 1)):
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
    elif (i + 1 > dim - 1) and (j in range(1, dim - 1)):
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
    elif (j + 1 > dim - 1) and (i in range(1, dim - 1)):
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
    elif (i - 1 < 0) and (j in range(1, dim - 1)):
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
    elif (i == dim - 1) and (j == 0):
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
    elif (i == 0) and (j == 0):
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
        #East
        if B[i, j + 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            abs_dir = 'E'
            j = j + 1
    elif (i == 0) and (j == dim - 1):
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #South
        if B[i + 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'S'
            i = i + 1
    else:
        #West
        if B[i, j - 1] == B[i, j] - 1:
            if abs_dir == 'W':
                #go forward
                go_forward()
                
            if abs_dir == 'S':
                #turn right
                turn_right()
                #go forward
                go_forward()
                
            if abs_dir == 'E':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            if abs_dir == 'N':
                #turn left
                turn_left()
                #go forward
                go_forward()
                
            abs_dir = 'W'
            j = j - 1
        #North
        if B[i - 1, j] == B[i, j] - 1:
            if abs_dir == 'W':
                #turn right
                turn_right()
                #go forard
                go_forward()
            
            if abs_dir == 'S':
                #turn left
                turn_left()
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'E':
                #turn left
                turn_left()
                #go forward
                go_forward()
            
            if abs_dir == 'N':
                #go forward
                go_forward()
            
            abs_dir = 'N'
            i = i - 1
